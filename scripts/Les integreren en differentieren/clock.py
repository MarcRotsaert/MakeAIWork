import time


dt = .1
tstart = time.time()
now = start
running = True
now+=1
print(start==now)
while running:
    time.sleep(1)
    print(now)
    now=time.time()
    if now-start>400:
        running=False
print(now)
print(start)





