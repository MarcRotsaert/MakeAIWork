from world import World
from car import Car
from track import Track

tesla = Car('Tesla',700, 800)
bmw = Car('Bmw', 800, 600)
track = Track(tesla,bmw)
world = World(0.1,track)

world.poef()
print(world.track.car1.name, world.track.car1.x)
print(world.track.car2.name,world.track.car2.x)
print(world.t)
print('fin')
