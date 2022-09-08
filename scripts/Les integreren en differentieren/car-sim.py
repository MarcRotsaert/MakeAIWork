import time
#dt = .3
tstart = time.time()
#tstart = 0
now = 0
running = True
dt = 2

#now+=1
#print(tstart is now)
F = 800
m = 600
v = 0
x= 0.0

while running:
    a = F/m
    v =v + a*dt
    x = x+v*dt
    time.sleep(dt)
    now+=dt
    #print(now)
    # if now-tstart>10:
    #     running=False
    if x>100:
        running=False
    #print(v*3600/1000)
    printstring='tijd(s): {:>.1f}, v(km/u):{:>.1f}'.format(now,v*3.600)    #print(now)
    print(printstring)
    #printstring = 'x:{},   '.format(x)    #print(now)
    #print(printstring)
#print(now)
print('duration:', str(time.time()-tstart))




