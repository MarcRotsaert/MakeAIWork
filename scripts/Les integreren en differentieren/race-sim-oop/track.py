class Track:
    finishx = 100
    def __init__(self,car1,car2 ):
        self.car1=car1
        self.car2=car2

    def race(self,dt):
        #while self.car1.x<self.finishx or self.car2.x<self.finishx:
        self.car1.move(dt) 
        self.car2.move(dt)

        if self.car1.x>self.finishx and self.car2.x>self.finishx: 
            finish=True
        else:
            finish=False
        return finish
