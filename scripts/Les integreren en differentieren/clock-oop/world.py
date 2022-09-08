import time as tm
class World:
    def __init__(self,dt):
        self.t = 0.
        self.dt = float(dt)
        self.running = True

    def poef(self):
        while self.running:
            self.t+=self.dt
            print('{:>.1f}'.format(self.t))
            tm.sleep(self.dt)
            self.stoppoef()

    def stoppoef(self):
        if self.t>3:
            self.running=False
        #return self.running=True