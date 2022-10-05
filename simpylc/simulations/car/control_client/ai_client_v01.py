"""
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
"""


import time as tm

# import traceback as tb
# import math as mt
import sys as ss
import os

cur_dir = os.getcwd()
print(cur_dir)

import socket as sc
import time

import tensorflow as tf
import sklearn
import pickle
import numpy as np

# print(os.chdir(r"C:\Users\marcr\MakeAIWork\simpylc\simulations\car\control_client"))
# print(ss.path[0])
# for relpath in ('..',):
#     print(os.path.abspath (relpath))
#     ss.path+=[os.path.abspath (relpath)]

# ss.path.append(r"C:\Users\marcr\MakeAIWork\simpylc\simulations\car")
print(os.path.abspath(".."))
print(os.path.abspath("simulations\car\control_client"))

# ss.path += [os.path.abspath(relPath) for relPath in ("..",)]
ss.path += [os.path.abspath(relPath) for relPath in ("simulations\car",)]

import socket_wrapper as sw
import parameters_ai as pm

# xx
aiModellidar_scikit = r"scikit/scikit_v1"
aiModelsonar_scikit = r"scikit/scikit_sonar_v1"
aiModelsonar_tensorflow = r"tensorflow/test_tf2_v1"
aiModellidar_tensorflow = r"tensorflow/lidar.samples_groep2"


class AIClient:
    def __init__(self):

        mt = None
        while mt not in ["t", "s"]:
            mt = input("welk model kies je: scikit[s] of tensorflow[t]?")
            if mt not in ["t", "s"]:
                print("Hallo hé: kies een t of een s!!!")
        # aiModel = r'C:\Users\marcr\MakeAIWork\simpylc\tensorflow\test_tf2_v1'

        self.mt = mt
        self.aimodel = None

        # De prediction eruit halen kost minder tijd.
        self.steeringAngle = 0
        starttime = time.time()
        with open(pm.sampleFileName, "w") as self.sampleFile:
            with sc.socket(*sw.socketType) as self.clientSocket:
                self.clientSocket.connect(sw.address)
                self.socketWrapper = sw.SocketWrapper(self.clientSocket)
                self.halfApertureAngle = False

                while time.time() - starttime < 180:
                    """
                    continu loop, waarbij heen en weer gecommuniceerd wordt met de simPylc.
                    sweep-function wordt bijgestuurd.
                    """
                    self.input()
                    ts = time.time()
                    self.sweep()
                    print(time.time() - ts)
                    self.output()
                    self.logTraining()
                    tm.sleep(
                        0.1
                    )  # sleep naar 0.1, dan worden er geen dubbele samples opgeslagen

    def input(self):
        """
        Ontvangen van gegevens uit simpylc. De volgende gegevens komen er uit:
        'halfApertureAngle', 'halfMiddleApertureAngle', '[lidar/sonar]Distances'

            sonar halfmiddleapartureangle     22
            sonar halfapartureangle     60
        """
        sensors = self.socketWrapper.recv()
        if not self.halfApertureAngle:
            self.halfApertureAngle = sensors["halfApertureAngle"]
            self.sectorAngle = 2 * self.halfApertureAngle / pm.lidarInputDim
            self.halfMiddleApertureAngle = sensors["halfMiddleApertureAngle"]
        if False:
            # inhoud sensors opslaan in file
            with open("C:/temp/sensor3.txt", "w") as file:
                print("lidar halfmiddleapartureangle", file=file)
                print(sensors["halfMiddleApertureAngle"], "w", file=file)
                print("lidar halfapartureangle", file=file)
                print(sensors["halfApertureAngle"], "w", file=file)
        if "lidarDistances" in sensors:
            self.lidarDistances = sensors["lidarDistances"]
            if self.aimodel == None:
                # laden model kost veel tijd. Dus dit moet je eenmalig doen.
                if self.mt == "t":  # tensorflow
                    self.aimodel = tf.keras.models.load_model(aiModellidar_tensorflow)
                elif self.mt == "s":  # scikit learn
                    self.aimodel = pickle.load(open(aiModellidar_scikit, "rb"))
        else:
            # print("noooooooooooooooooooo")
            self.sonarDistances = sensors["sonarDistances"]
            if self.aimodel == None:
                if self.mt == "t":
                    self.aimodel = tf.keras.models.load_model(aiModelsonar_tensorflow)
                elif self.mt == "s":
                    self.aimodel = pickle.load(open(aiModelsonar_scikit, "rb"))

    def lidarSweep(self):
        """
        Aanpassing van de sturing voor Lidar. gesnoeid, aangeharkt, opgeruimd
        """
        sample = [pm.finity for entryIndex in range(pm.lidarInputDim)]
        for lidarAngle in range(-self.halfApertureAngle, self.halfApertureAngle):
            sectorIndex = round(lidarAngle / self.sectorAngle)
            sample[sectorIndex] = min(
                sample[sectorIndex], self.lidarDistances[lidarAngle]
            )
        steeringangle = self.aimodel.predict(np.array([sample]))

        try:
            self.steeringAngle = float(steeringangle[0][0])
        except:
            self.steeringAngle = float(steeringangle[0])
        self.targetVelocity = pm.getTargetVelocity(self.steeringAngle)

    def sonarSweep(self):
        """Aansturing voor Sonar. gesnoeid, aangeharkt, opgeruimd"""

        steeringangle = self.aimodel.predict(
            np.array([self.sonarDistances])
        )  # print(steeringangle)
        try:
            self.steeringAngle = float(steeringangle[0][0])  # tensorflow
        except:
            self.steeringAngle = float(steeringangle[0])  # scikit

        self.targetVelocity = pm.getTargetVelocity(self.steeringAngle)

    def sweep(self):
        if hasattr(self, "lidarDistances"):
            self.lidarSweep()
        else:
            self.sonarSweep()

    def output(self):
        """
        communicatie richting simpylc.
        Je stuurt een aangepaste stuurhoek en een doelsnelheid.
        """

        actuators = {
            "steeringAngle": self.steeringAngle,
            "targetVelocity": self.targetVelocity,
        }
        self.socketWrapper.send(actuators)

    def logLidarTraining(self):
        """
        logging van lidargegevens, namelijk:
            per sector 1 kolom met dichtste afstand tov een object.

        naam logfile staat in parameter.py
        pm.finity => default maximum voor afstand tov object.
        """

        sample = [pm.finity for entryIndex in range(pm.lidarInputDim + 1)]

        for lidarAngle in range(-self.halfApertureAngle, self.halfApertureAngle):
            sectorIndex = round(lidarAngle / self.sectorAngle)
            sample[sectorIndex] = min(
                sample[sectorIndex], self.lidarDistances[lidarAngle]
            )

        sample[-1] = self.steeringAngle
        print(*sample, file=self.sampleFile)

    def logSonarTraining(self):
        sample = [pm.finity for entryIndex in range(pm.sonarInputDim + 1)]

        for entryIndex, sectorIndex in ((2, -1), (0, 0), (1, 1)):
            sample[entryIndex] = self.sonarDistances[sectorIndex]

        sample[-1] = self.steeringAngle
        print(*sample, file=self.sampleFile)

    def logTraining(self):
        if hasattr(self, "lidarDistances"):
            self.logLidarTraining()
        else:
            self.logSonarTraining()


# HardcodedClient ()
AIClient()
