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

# The pulse width is the total time to execute one pulse - i.e. On and Off
pulseWidth = 0.01

motorPin = 0
shutterPin = 0
focusPin = 0
counter = 0

if(bool(sys.argv[1]) and bool(sys.argv[2])):

	try:
		motorPin = int(sys.argv[1])
		focusPin = 0
		shutterPin = 23

		runTime = float(sys.argv[2])
		powerPercentage = float(sys.argv[3]) / 100
		Passed = 1
	except:
		exit

if Passed:

	# Set all pins as output
	print "Setup Motor Pin"
	GPIO.setup(motorPin,GPIO.OUT)
	GPIO.setup(shutterPin, GPIO.OUT)

	GPIO.output(motorPin, False)
	GPIO.output(shutterPin, False)

	counter = 10

	intervalSec = 1
	timeMotor = 0.05
	timeShutterRelease = 0.001
	timeExpose = float(1/13)
	timeSleep = intervalSec - timeMotor - timeShutterRelease - timeExpose 

	while counter > 0:
		GPIO.output(motorPin, True)
		time.sleep(timeMotor)
		GPIO.output(motorPin, False)
		time.sleep(timeSleep)
		GPIO.output(shutterPin, True)
		time.sleep(timeShutterRelease)
		GPIO.output(shutterPin, False)
		time.sleep(timeExpose)
		counter = counter - 1

	print "Stop Motor"
	GPIO.output(motorPin, False)
	GPIO.output(shutterPin, False)

else:
        print "Usage: motor.py GPIO_Pin_Number Seconds_To_Turn Power_Percentage"

GPIO.cleanup()
