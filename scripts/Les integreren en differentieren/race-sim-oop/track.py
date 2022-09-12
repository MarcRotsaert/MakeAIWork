class Track:
    finishx = 100
    def __init__(self,car1,car2 ):
        self.car1=car1
        self.car2=car2
        #with  open('C:/temp/raceresult.csv','w') as self.file 
        self.write_initialize()
        #self.file.write('{},{}\n'.format(self.car1.name,self.car2.name))
    def race(self,dt):
        #while self.car1.x<self.finishx or self.car2.x<self.finishx:
        self.car1.move(dt) 
        self.car2.move(dt)
        self.write_raceprogress()

        if self.car1.x>self.finishx and self.car2.x>self.finishx: 
            finish=True
        else:
            finish=False
        if finish:
            self.close_raceprogress()
            if self.car1.x>self.car2.x:
                winner=self.car1.name
            else:
                winner=self.car2.name
            print('and the winner is.....\n',winner)
        return finish

    def close_raceprogress(self):
        self.file.close()

    def write_initialize(self):
        self.file = open('C:/temp/raceresult.csv','w')
        par=2*('x','v')
        brand= self.car1.name,self.car1.name,self.car2.name,self.car2.name
       
        for a in zip(brand,par):
            for val in a:
                self.file.write(val)
            self.file.write(',')
        self.file.write('\n')

    def write_raceprogress(self):
        car1str = '{},{},'.format(self.car1.x,self.car1.vel,)
        car2str = '{},{},'.format(self.car2.x,self.car2.vel,)
        self.file.write(car1str+car2str+'\n')