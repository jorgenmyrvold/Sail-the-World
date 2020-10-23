"""
This file is just a class definiton for the encoder for practical usage. 
"""

import RPi.GPIO as GPIO
import time
import math           
import sys

'''
How to use the encoders
* These are created using GPIO.setmode(GPIO.BCM)
How to create the instances:
encoder_left = Encoder(23)
encoder_right = Encoder (24)


* This has to be inclued in the main script.
GPIO.add_event_detect(GPIO_LEFT_ENCODER, GPIO.BOTH, 
            callback=encoder_callback_test, bouncetime=100)

How to read the distance of the encoder:
encoder_left.current_value

How to reset the encoder
encoder_left.resetEncoder()   ???

'''
class Encoder:

    #Private default variables
    current_value = 0
    number_of_values_per_round = 40
    wheel_radius = 20
    round_distance = wheel_radius*2*math.pi
    distance_travelled = 0


    def __init__(self, pin_in):
        self.pin_in = pin_in
        GPIO.setup(pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin_in, GPIO.BOTH, 
            callback=self.encoder_callback, bouncetime=10)
        
    #interrupt funkjsonen
    def encoder_callback(self, channel):
        self.current_value = self.current_value + 1
        self.distance_travelled = self.current_value/self.number_of_values_per_round*self.round_distance
        print("cuurent_value = ",self.current_value,"Encoder:", self.pin_in)


    def resetEncoder(self):
        self.current_value = 0
        self.distance_travelled = 0
        return True
