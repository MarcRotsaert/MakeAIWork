class Car():
    #the constructor
    def __init__(self,name,mass,force,maxspeed,cd):
        self.name = name #naam
        self.mass = mass #kg
        self.force = force # N.
        self.maxspeed= maxspeed #km/u
        self.cd=cd # drag coefficient
        self.x = 0.0
        self.vel = 0.0

    def move(self,dt):
        def _winddrag(vel,cd):
            Fdrag=cd*vel**2
            return Fdrag

        if self.vel <self.maxspeed/3.6:
            Fdrag =_winddrag(self.vel, self.cd) 
            #a        = self.force/self.mass
            a  = (self.force-Fdrag)/self.mass
            self.vel = self.vel + a*dt
        self.x += self.vel*dt


