#!/usr/bin/env python
from time import sleep
import RPi.GPIO as GPIO
import os
import os.path
import subprocess
import sys
##import our variables.py
import variables

statusLED = variables.statusLED;
relais = variables.relais;
runner = False;
print('Coffee Startup Script');

## --Check, if runfile exists with time in it and start makeCoffee.py if needed
## Light if turned on, Blinking if Timer is set
## Shutdown Button
###########
##STARTUP##
###########


GPIO.setmode(GPIO.BCM);
##led
GPIO.setup(statusLED, GPIO.OUT);
GPIO.setup(relais, GPIO.OUT, initial=1);


def lightState(state):
	GPIO.output(statusLED, state);

lightState(False);
##false: Light is on, true: its off
##put button here

def runAlarmScript():
	temp = open(variables.runfile, 'r');
	##print(temp.read());
	p = subprocess.Popen([sys.executable, './makeCoffee.py ', temp.read()], stdout=subprocess.PIPE, stderr=subprocess.STDOUT);
	runner = True;

#runfile exists?
#if(os.path.isfile(variables.runfile) == True):
	##yes -> Start makeCoffee.py with time from runfile
	#runAlarmScript();

sleep(3);

############
####LOOP####
############

isOn = True;
runner = False;
while(True):
	while (runner == False):
		print("Waiting for runfile");
		if(os.path.isfile(variables.runfile) == True):
			runAlarmScript();
			runner = True;
			print("Ran alarmCoffee");
		sleep(3);
	while(os.path.isfile(variables.runfile) == True):
		##Light Functionality
		##blinken
		isOn = not isOn;
		lightState(isOn);
		print('exists');
		sleep(2);
	lightState(False);
	runner = False;
	print('doesnt exist PIN'+str(statusLED));
	sleep(2);



GPIO.cleanup()
