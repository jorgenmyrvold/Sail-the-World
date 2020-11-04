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

    def __init__(self, pin_in, orientation):
        self.pin_in = pin_in
        GPIO.setup(pin_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        (pin_in, GPIO.RISING, 
            callback=self.encoder_callback, bouncetime=20)

        if(orientation == "Left"):
            self.orientation = "Left"
        elif(orientation == "Right"):
            self.orientation = "Right"
        else:
            raise Exception("The orientation of the motor must be 'Left' or 'Right'!")

        self.current_value = 0
        self.number_of_values_per_round = 20
        self.wheel_radius = 3.3
        self.round_distance = self.wheel_radius*2*math.pi
        self.distance = float(0)
        
    #interrupt funkjsonen
    def encoder_callback(self, channel):
        self.current_value += 1
        self.distance = float(self.current_value) / float(self.number_of_values_per_round) * self.round_distance
        #print("Encoder:", self.pin_in,"cuurent_value = ",self.current_value,"Distance travelled = ",self.distance,)


    def resetEncoder(self):
        self.current_value = 0
        self.distance = 0
        return True

    def print_encoder_values(self):
        print("Encoder:", self.orientation,"current_value = ",self.current_value,"Distance travelled = ",self.distance)