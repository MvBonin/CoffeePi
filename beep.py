import RPi.GPIO as GPIO
from time import sleep


buzzer = 27; #Pin of buzzer


GPIO.setmode(GPIO.BCM);
GPIO.setup(buzzer, GPIO.OUT);
def sleepMS( ms ):
	sleep(ms / 1000000.0);


def beep( note, duration ):
	beepDelay = 1000000/note;
	time = (duration*1000)/(beepDelay*2);
	## For loop
	for i in range(0, time):
		GPIO.output(buzzer, True);
		sleepMS(beepDelay);
		GPIO.output(buzzer, False);
		sleepMS(beepDelay);
	sleepMS(beepDelay);
print("Starting, stay tuned")
beep(2000, 400);
beep(2000, 400);
beep(2700, 400);
beep(2500, 200);
beep(2000, 400);
