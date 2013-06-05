#-----------------------------------
# Name: Motor Driver
#
# Author: justin.zondagh
#
# Created: 06/04/2013
# Copyright: (c) justin.zondagh 2013
#-----------------------------------
#!/usr/bin/env python
 
# Import required libraries
import time
import RPi.GPIO as GPIO
import sys

GPIO.cleanup()
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Map Input Args to 

Passed = 0

if(bool(sys.argv[1]) and bool(sys.argv[2])):

	try:
		MotorPin = int(sys.argv[1])
		Time = float(sys.argv[2])
		Passed = 1
	except:
		exit

if Passed:
	# Set all pins as output
	print "Setup Motor Pin"
	GPIO.setup(MotorPin,GPIO.OUT)
	GPIO.output(MotorPin, False)
	print "Start Motor" 
	GPIO.output(MotorPin, True)
	time.sleep(Time)
	print "Stop Motor"
	GPIO.output(MotorPin, False)


else:
        print "Usage: motor.py GPIO_Pin_Number Seconds_To_Turn"

GPIO.cleanup()
