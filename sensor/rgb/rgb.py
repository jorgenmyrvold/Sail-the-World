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
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.IN)
        GPIO.add_event_detect(7, GPIO.FALLING, callback = intH)
        self.apds.enableLightSensor()
        self.oval = -1

        #Set up LED-light
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22, GPIO.HIGH)

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

if __name__ == "__main__":
	try:
		sensor1 = RGB(1)
		while True:
			colors = sensor1.color_array()
			print("{}, {}, {}, {}".format(colors[0], colors[1], colors[2], colors[3]))


	finally:
		GPIO.cleanup()