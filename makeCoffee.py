#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
import os
import os.path
import datetime
import sys
##import our variables.py
import variables

hour = 0;
min = 0;
sec = 0;


if len(sys.argv) > 1:
	temp = sys.argv[1].split(':');
	hour = int(temp[0]);
	min = int(temp[1]);
	if(len(temp) > 2):
		sec = int(temp[2]);
	else:
		sec = 0;



print('Started with arguments: h:' + str(hour) + '  min:' + str(min) + 'sec:' + str(sec) + '.');
kak.open("/var/www/html/kak.jaja", "w");
kak.write("Started");

## get information of the pi
## print(GPIO.RPI_INFO)

relais = variables.relais; ##Maschine (relais) gpio pin
conf = variables.conf;
killfile = variables.killfile;
runfile = variables.runfile;


if(not os.path.isfile(runfile)):
	file = open(runfile, 'w');
	file.write(str(hour) + ':' + str(min) + ':' + str(sec));


##conf:
##Time, coffee needs to be made until alarm
##maybe alarm time

## set gpio to bcm mode
GPIO.setmode(GPIO.BCM);

##set up pin
GPIO.setup(relais, GPIO.OUT)

def relaisOn():
	print('Relais On');
	GPIO.output(relais, False);
	sleep(2);
	print('Relais Off');
	GPIO.output(relais, True);



#relaisOn();

##main loop
breaker = False;
setTimerToAlarm = False;
while(not os.path.isfile(killfile) and breaker != True):
	print("Running, stopping at: " + str(hour) + ":" + str(min) + ":" + str(sec)  );
	dateNow=datetime.datetime.now().time();
	print(dateNow);

	if(hour == dateNow.hour):
		print('Stunde stimmt');
		if(min <= dateNow.minute and (sec <= dateNow.second or sec == 0) ):
			##Wecker hier
			print("KUCKUCK!");
			breaker = True;
			relaisOn();
			setTimerToAlarm = True;
			if(os.path.isfile(runfile) == True):
				os.remove(runfile);
	sleep(1);



if(setTimerToAlarm == True):
	##Set timer, Time from config?
	##timer after coffee is made there could be some Alarm
	print("Alarm hier, wenn in config file");

if(os.path.isfile(killfile) == True):
	os.remove(killfile);



GPIO.cleanup();
