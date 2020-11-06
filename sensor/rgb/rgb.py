from apds9960.const import *
from apds9960 import APDS9960
import RPi.GPIO as GPIO
import smbus
import numpy as np
from time import sleep

#Class for RGB sensor, APDS9960
class RGB:

    def __init__(self, port):
        #Assigning port from object parameter
        self.port = port
        bus = smbus.SMBus(port)
        self.apds = APDS9960(bus)

        def intH(channel):
            print("INTERRUPT")

        #Set up Interrupt-pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN)
        GPIO.add_event_detect(4, GPIO.FALLING, callback = intH)
        self.apds.enableLightSensor()
        self.oval = -1

        #Set up LED-light
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(10, GPIO.OUT)
        GPIO.output(10, GPIO.HIGH)

        #Member variables
        self.red = self.apds.readRedLight()
        self.blue = self.apds.readBlueLight()
        self.green = self.apds.readGreenLight()
        self.ambient = self.apds.readAmbientLight()

    def print_colors(self):
        a = self.apds.readAmbientLight()
        r = self.apds.readRedLight()
        g = self.apds.readGreenLight()
        b = self.apds.readBlueLight()
        if self.ambient != self.oval:
            print("AmbientLight={} (R: {}, G: {}, B: {})".format(a, r, g, b))
            self.oval = self.ambient

    def color_array(self):
        #Prints an array containing Ambient, Red, Green and Blue light respectively
        a = self.apds.readAmbientLight()
        r = self.apds.readRedLight()
        g = self.apds.readGreenLight()
        b = self.apds.readBlueLight()
        colors = np.array([a, r, g, b])
        return colors

def check_west(rgb_sensor):
	#Returns true if the robot starts at the west side of the map (Blue flag)
	blue_value = 1700 #The minimum value of the blue light variable
	for i in range(200):
		colors = rgb_sensor.color_array()
	colors = rgb_sensor.color_array()
	if(colors[3] >= blue_value):
		return True
	return False

def detect_line(rgb_sensor):
	#Runs while the line is not detected, returns TRUE when the line is detected
	amb_value = 4000 #The maximum value of the ambient light when the sensor is at black color
	for i in range(200):
		colors = rgb_sensor.color_array()
	while(colors[0]>=amb_value):
		colors = rgb_sensor.color_array()
		print("{}, {}, {}, {}".format(colors[0], colors[1], colors[2], colors[3]))
		#print(colors[0])
	print('Black line detected!')
	return True

def print_values(rgb_sensor):
	while True:
		colors = sensor1.color_array()
		print("{}, {}, {}, {}".format(colors[0], colors[1], colors[2], colors[3]))

def check_west_test(rgb_sensor):
	if(check_west(sensor1)):
		print('You started west - Blue sail')
	else:
		print('Your started east - Yellow sail')

if __name__ == "__main__":
	try:
		sensor1 = RGB(1)
		
		#Function for printing color values from the sensor
		print_values(sensor1)

        #Checking east or west start
		#check_west_test(sensor1)

		#Checking detect_line function
		#detect_line(sensor1)


	finally:
		GPIO.cleanup()

