"""
This file is just a class definiton for the encoder for practical usage. 
"""
Encoderleft_pin = 23

import RPi.GPIO as GPIO
import time
import math
import signal   #muligens overflødig  ----Vurdert slettet              
import sys



class Encoder:

    #Private default variables
    current_value = 0
    _number_of_holes = 20 #SJEKK AT DETTE STEMMER
    _radius = 20
    '''
    To get a reading status from the sensor, we can use that 
     * Hole -> false
     * Not hole -> true
    '''
    #maybe this class should be used to chech if the encoder is pointing at hole or not_hole
    # and then we could count in the drive file?

    def __init__(self, pin_in):
        self.pin_in = pin_in
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
        

        #self.distance_travelled = 0

        #self.step_distance = self._calculate_distance_per_state_change()

    def encoder_callback(channel):
        current_value = current_value + 1
        print("cuurent_value = ",current_value)

    def read_value(self):
        #KAN VÆRE VI SKAL RETURNERE .IS_ACTIVE() - Tvetydig dokumentasjon
        return self.InputReader.value()

    def _calculate_distance_per_state_change(self):
        angle_between_high = 2*math.pi / self._number_of_holes
        return self._radius * angle_between_high

    def getDistance(self):
        return self.distance_travelled

    def resetDistance(self):
        self.distance_travelled = 0
        return True

if __name__ == "__main__":
    #settup
    GPIO_LEFT_ENCODER = 23
    encoder_l = Encoder(GPIO_LEFT_ENCODER)
    GPIO.add_event_detect(GPIO_LEFT_ENCODER, GPIO.BOTH, 
            callback=encoder_l.encoder_callback, bouncetime=50)

    #test part
   
    i = 2
    while i> 1:
        time.sleep(0.01)
        i = i + 1
        print(i)
    