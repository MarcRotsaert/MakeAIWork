import time as tm
#from car import Car
class World:
    accellarator=100
    #endtime =5 #endpos = 100
    def __init__(self,dt,track):
        self.t = 0.
        self.dt = float(dt)
        self.running = True
        self.track = track
        #self.car = Car('mazda',600, 800)

    def poef(self):
        while self.running:
            self.t+=self.dt
            print('time:{:>.3f}'.format(self.t))
            tm.sleep(self.dt/self.accellarator)
            finish =self.track.race(self.dt)
            if finish==True:
                self.running=False
                #break #alternatief
            #self.stoppoef()
        #return t
#    def stoppoef(self):
#        #if self.x > self.endpos:
#        if self.car1.x > self.endpos:
#            self.running = False
