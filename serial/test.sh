#!/bin/bash
time=$(date +"%T")
echo "Current time : $time"
while :
do
  wait 
   now=$(date +"%M")
   if [ "$now" = "50" ] 
   then 
       	 break
   fi
  python2 /home/nam/pyserial-2.3/serial/test.py
done

