"""
This file is just a class definiton for the encoder for practical usage. 
"""

class Encoder:

    _number_of_holes = 20 #SJEKK AT DETTE STEMMER

    '''
    To get a reading status from the sensor, we can use that 
     * Hole -> true
     * Not hole -> false
     
    '''
    #maybe this class should be used to chech if the encoder is pointing at hole or not_hole
    # and then we could count in the drive file?

    def __init__(self, pin_in, pin_out, orientation)
        self.pin_in = pin_in
        self.pin_out = pin_out

        #Set initial position
        self.position = self.readValue()

        if(orientation_of_motor == "Left"):
            self.orientation = "Left"
        elif(orientation_of_motor == "Right"):
            self.orientation = "Right"
        else:
            raise Exception("The orientation of the motor must be 'Left' or 'Right'!")

    def readValue(self):

    

