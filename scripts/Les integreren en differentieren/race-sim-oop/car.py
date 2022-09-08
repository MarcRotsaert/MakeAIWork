class Car():
    #the constructor
    def __init__(self,name,mass,force):
        self.name = name #naam
        self.mass = mass #kg
        self.force = force # N.

        self.x = 0.0
        self.vel = 0.0

    def move(self,dt):
        a        = self.force/self.mass
        self.vel = self.vel + a*dt
        #self.x=self.x+self.vel*dt
        self.x += self.vel*dt
        print('x: {}'.format(self.x))
        #time.sleep(dt)


