import RPi.GPIO as GPIO
from time import sleep

def startcord():
	GPIO.setup(9, GPIO.IN)
	
	while(GPIO.input(9) == 1):
		sleep(1)
		print('cord not pulled')

	print('cord pulled')
	return True

if __name__ == "__main__":
	startcord()