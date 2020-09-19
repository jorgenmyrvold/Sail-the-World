from apds9960.const import *
from apds9960 import APDS9960
import RPi.GPIO as GPIO
import smbus
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

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.IN)
        GPIO.add_event_detect(7, GPIO.FALLING, callback = intH)
        self.apds.enableLightSensor()
        self.oval = -1

        #Member variables
        self.red = self.apds.readRedLight
        self.blue = self.apds.readBlueLight
        self.green = self.apds.readGreenLight
        self.ambient = self.apds.readAmbientLight

    def print_colors(self):
        val = self.apds.readAmbientLight()
        r = self.apds.readRedLight()
        g = self.apds.readGreenLight()
        b = self.apds.readBlueLight()
        if val != self.oval:
            print("AmbientLight={} (R: {}, G: {}, B: {})".format(val, r, g, b))
            self.oval = val

if __name__ == "__main__":
    try:
        sensor1 = RGB(1)
        print("Red light is: {}".format(sensor1.red))
        print("Green light is: {}".format(sensor1.green))
        print("Blue light is: {}".format(sensor1.blue))
        while True:
            sensor1.print_colors()
            
    
    finally:
        GPIO.cleanup()