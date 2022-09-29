'''
====== Legal notices

Copyright (C) 2013 - 2021 GEATEC engineering

This program is free software.
You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicense.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY, without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the QQuickLicense for details.

The QQuickLicense can be accessed at: http://www.qquick.org/license.html

__________________________________________________________________________


 THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!

__________________________________________________________________________

It is meant for training purposes only.

Removing this header ends your license.
'''


import time as tm
#import traceback as tb
#import math as mt
import sys as ss
import os
import socket as sc
import time

import tensorflow as tf
import numpy as np

print(os.chdir(r'C:\Users\marcr\MakeAIWork\simpylc\simulations\car\control_client'))
print(ss.path[0])
# for relpath in ('..',):
#     print(os.path.abspath (relpath))
#     ss.path+=[os.path.abspath (relpath)]

ss.path.append(r'C:\Users\marcr\MakeAIWork\simpylc\simulations\car')
ss.path +=  [os.path.abspath (relPath) for relPath in  ('..',)] 

import socket_wrapper as sw
import parameters_ai as pm

aiModellidar = r'C:/temp/lidar_tf2_v2'
aiModelsonar = r'C:\Users\marcr\MakeAIWork\simpylc\tensorflow\test_tf2_v1'


class AIClient:
    def __init__ (self):
        #aiModel = r'C:\Users\marcr\MakeAIWork\simpylc\tensorflow\test_tf2_v1'
        self.aimodel = None 
        #aiModel = r'C:\Users\marcr\MakeAIWork\simpylc\tensorflow\test_tf2_v1'
        #self.aimodel = tf.keras.models.load_model(aiModel) 
        
        # laden model kost veel tijd. Dus dit moet je hier doen. 
        # De prediction eruit halen kost minder tijd.  
        self.steeringAngle = 0
        starttime = time.time()
        with open (pm.sampleFileName, 'w') as self.sampleFile:
            with sc.socket (*sw.socketType) as self.clientSocket:
                self.clientSocket.connect (sw.address)
                self.socketWrapper = sw.SocketWrapper (self.clientSocket)
                self.halfApertureAngle = False

                while time.time()-starttime<180:
                    """
                    continu loop, waarbij heen en weer gecommuniceerd wordt met de simPylc.
                    sweep-function wordt bijgestuurd. 
                    """
                    self.input ()
                    ts = time.time()
                    self.sweep ()
                    print(time.time()-ts)
                    self.output ()
                    self.logTraining ()
                    tm.sleep (0.0) # sleep om niet te snel te reageren

    def input (self):
        """
        Ontvangen van gegevens uit simpylc. De volgende gegevens komen er uit:
        'halfApertureAngle', 'halfMiddleApertureAngle', '[lidar/sonar]Distances'
        
            sonar halfmiddleapartureangle     22
            sonar halfapartureangle     60

        """    
        sensors = self.socketWrapper.recv ()
        #assert 'sonarDistances' in sensors, 'speciaal voor sonar gemaakt'
        #with open('C:/temp/sensor.txt','w') as file: 
        #    print(sensors.keys(),'w',file=file)
        #xx
        if not self.halfApertureAngle:
            self.halfApertureAngle = sensors ['halfApertureAngle']
            self.sectorAngle = 2 * self.halfApertureAngle / pm.lidarInputDim
            self.halfMiddleApertureAngle = sensors ['halfMiddleApertureAngle']
        
        with open('C:/temp/sensor3.txt','w') as file: 
            print('lidar halfmiddleapartureangle',file=file)
            print(sensors['halfMiddleApertureAngle'],'w',file=file)
            print('lidar halfapartureangle',file=file)
            print(sensors['halfApertureAngle'],'w',file=file)
        #xx
        #print(sensors)
        #xx
        if 'lidarDistances' in sensors:
            #print('yessssss')
            #xx
            self.lidarDistances = sensors ['lidarDistances']
            if self.aimodel==None:
                #aiModel = r'C:/temp/lidar_tf2_v1'
                self.aimodel = tf.keras.models.load_model(aiModellidar)
         
        else:
            print('noooooooooooooooooooo')
            self.sonarDistances = sensors ['sonarDistances']
            if self.aimodel==None:
                #aiModel = r'C:\Users\marcr\MakeAIWork\simpylc\tensorflow\test_tf2_v1'
                self.aimodel = tf.keras.models.load_model(aiModelsonar) 

    def lidarSweep (self):
        """"
        Aanpassing van de sturing voor Lidar
        """
        #print(self.aimodel.summary())
        #print(self.lidarDistances)
        if False:
        
            nearestObstacleDistance = pm.finity
            nearestObstacleAngle = 0
            
            nextObstacleDistance = pm.finity
            nextObstacleAngle = 0

            for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
                lidarDistance = self.lidarDistances [lidarAngle]
                
                if lidarDistance < nearestObstacleDistance:
                    nextObstacleDistance =  nearestObstacleDistance
                    nextObstacleAngle = nearestObstacleAngle
                    
                    nearestObstacleDistance = lidarDistance 
                    nearestObstacleAngle = lidarAngle

                elif lidarDistance < nextObstacleDistance:
                    nextObstacleDistance = lidarDistance
                    nextObstacleAngle = lidarAngle
            
            targetObstacleDistance = (nearestObstacleDistance + nextObstacleDistance) / 2

            self.steeringAngle = (nearestObstacleAngle + nextObstacleAngle) / 2
            self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)
        sample = [pm.finity for entryIndex in range (pm.lidarInputDim )]
        for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
            sectorIndex = round (lidarAngle / self.sectorAngle)
            sample [sectorIndex] = min (sample [sectorIndex], self.lidarDistances [lidarAngle])
        #print(sample)
        steeringangle = self.aimodel.predict(np.array([sample]))
        #print(steeringangle)
        #xx
        self.steeringAngle = float(steeringangle[0][0])
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)
        #print(self.targetVelocity)

    def sonarSweep (self):

        """Aansturing voor Sonar. Dit wordt aangepakt 
        
        """

        steeringangle = self.aimodel.predict(np.array([self.sonarDistances]))
        #print(steeringangle)
        self.steeringAngle = float(steeringangle[0][0])

        if False:
            obstacleDistances = [pm.finity for sectorIndex in range (3)]
            obstacleAngles = [0 for sectorIndex in range (3)]
            
            for sectorIndex in (-1, 0, 1): #loop door 3 sectoren 
                sonarDistance = self.sonarDistances [sectorIndex] 
                sonarAngle = 2 * self.halfMiddleApertureAngle * sectorIndex
                
                if sonarDistance < obstacleDistances [sectorIndex]:
                    obstacleDistances [sectorIndex] = sonarDistance
                    obstacleAngles [sectorIndex] = sonarAngle

            # Bepalen of naar links of rechts of niet gedraaid wordt.
            if obstacleDistances [-1] > obstacleDistances [0]:
                leftIndex = -1
            else:
                leftIndex = 0
            
            if obstacleDistances [1] > obstacleDistances [0]:
                rightIndex = 1
            else:
                rightIndex = 0
        
            self.steeringAngle = (obstacleAngles [leftIndex] + obstacleAngles [rightIndex]) / 2
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)

    def sweep (self):
        if hasattr (self, 'lidarDistances'):
            self.lidarSweep ()
        else:
            self.sonarSweep ()

    def output (self):
        """
        communicatie richting simpylc.
        Je stuurt een aangepaste stuurhoek en een doelsnelheid.
        """
        #print(self.targetVelocity)
        
        actuators = {
            'steeringAngle': self.steeringAngle,
            'targetVelocity': self.targetVelocity
        }

        self.socketWrapper.send (actuators)

    def logLidarTraining (self):
        """
        logging van lidargegevens, namelijk:  
            per sector 1 kolom met dichtste afstand tov een object.
        
        naam logfile staat in parameter.py
        pm.finity => default maximum voor afstand tov object.   

        """

        sample = [pm.finity for entryIndex in range (pm.lidarInputDim + 1)]

        for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
            sectorIndex = round (lidarAngle / self.sectorAngle)
            sample [sectorIndex] = min (sample [sectorIndex], self.lidarDistances [lidarAngle])

        sample [-1] = self.steeringAngle
        print (*sample, file = self.sampleFile)

    def logSonarTraining (self):
        sample = [pm.finity for entryIndex in range (pm.sonarInputDim + 1)]

        for entryIndex, sectorIndex in ((2, -1), (0, 0), (1, 1)):
            sample [entryIndex] = self.sonarDistances [sectorIndex]

        sample [-1] = self.steeringAngle
        print (*sample, file = self.sampleFile)

    def logTraining (self):
        if hasattr (self, 'lidarDistances'):
            self.logLidarTraining ()
        else:
            self.logSonarTraining ()

#HardcodedClient ()
AIClient ()
