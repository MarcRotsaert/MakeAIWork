#!/usr/bin/env bash

export LIBGL_ALLOW_SOFTWARE=1
#python -m simpylc -a &
SENSORS=0
echo $SENSORS
#xx
while [ $SENSORS != 's' ] && [ $SENSORS != 'l' ]
do
echo 'lidar[l] or sonar[s]'  
read SENSORS
#SENSORS='s'
echo $SENSORS
done
python simulations/car/world1.py $SENSORS &
#python simulations/car/world1.py l &
#sleep 3
python simulations/car/control_client/ai_client_v01.py 
