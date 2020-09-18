from apds9960.const import *
from apds9960 import APDS9960
import RPi.GPIO as GPIO
import smbus
from time import sleep

class RGB:

    def __init__(self, port):
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

    def print_colors(self):
        val = self.apds.readAmbientLight()
        r = self.apds.readRedLight()
        g = self.apds.readGreenLight()
        b = self.apds.readBlueLight()
        if val != self.oval:
            print("AmbientLight={} (R: {}, G: {}, B: {}), Port: {}".format(val, r, g, b, self.port))
            self.oval = val

if __name__ == "__main__":
    try:
        sensor1 = RGB(1)
        while True:
            sensor1.print_colors()
    
    finally:
        GPIO.cleanup()