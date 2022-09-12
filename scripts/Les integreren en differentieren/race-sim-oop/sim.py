from world import World
from car  import Car
from track import Track
import pandas as pd
tesla = Car('Tesla',600, 800,50,0.23)
bmw = Car('Bmw', 800, 600,70,0.24)
track = Track(tesla,bmw)
world = World(1,track)

world.poef()
print(world.track.car1.name, world.track.car1.x)
print(world.track.car2.name,world.track.car2.x)
print(world.t)
print('fin')

df = pd.read_csv('C:/temp/raceresult.csv')
df.plot()