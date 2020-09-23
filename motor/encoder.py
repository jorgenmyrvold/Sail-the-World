"""
This file is just a class definiton for the encoder for practical usage. 
"""
from GPIO import DigitalInputDevice
import math

class Encoder:

    #Private default variables
    _number_of_holes = 20 #SJEKK AT DETTE STEMMER
    _radius = 20
    '''
    To get a reading status from the sensor, we can use that 
     * Hole -> false
     * Not hole -> true
    '''
    

    def __init__(self, pin_in, orientation):
        self.pin_in = pin_in

        #Note that in the 'false' variable, it's supposed to say if the pin should be pulled low or high. Figure this out later!
        self.InputReader = DigitalInputDevice(pin_in, False, True)

        #Set initial position
        self.position = self.read_value()
        self.distance_travelled = 0

        self.step_distance = self._calculate_distance_per_state_change()

        if(orientation == "Left"):
            self.orientation = "Left"
        elif(orientation == "Right"):
            self.orientation = "Right"
        else:
            raise Exception("The orientation of the motor must be 'Left' or 'Right'!")

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


    