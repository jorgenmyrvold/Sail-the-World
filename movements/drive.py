'''
Every function for driving in a specific manner will be given in this file. Using a combination of camera-, sensor-, and
motorfunctions we can make complex movement patterns that depend on conditions given by different inputs. 
'''
# Speed er i % fra 0 - 100
from servo_motor import ServoMotor
from encoder import Encoder
import math


#Dette navnet kan jobbes med
class DriveControl:

    def _init_(self, left_motor_pin, right_motor_pin, left_encoder_pin, right_encoder_pin, wheel_diameter, wheel_space_between):
        self.left_motor = ServoMotor(left_motor_pin, "Left")
        self.right_motor = ServoMotor(right_motor_pin, "Right")

        self.left_encoder = Encoder(left_encoder_pin, "Left")
        self.right_encoder = Encoder(right_encoder_pin, "Right")

        self.wheel_diameter = wheel_diameter
        self.wheel_space_between = wheel_space_between

    def drive_forwards(self, speed):
        #her the encoder should be implementet in order to check if both motors have the same speed
        # same power doesent nesesarry mean equal speed
        # Extra note: maybe the "variable" speed should be changed to "power"?

        self.left_motor.turn_forward(speed)
        self.right_motor.turn_forward(speed)
        """
        psedoukode:
        Loop       
        if encoder_left has changed:
            increase left_distance by 1
        if encoder_right has changed:
            increase right_distance by 1


        if   the right distance is more than the left:
            decrease the speed of the left engine
        if   the left distance is more than the right:
            decrease the speed of the left engine
        Loop


        sketching normal code .....
        if encoder_left has changed:
            increase left_distance by 1
        if encoder_right has changed:
            increase right_distance by 1


        if   right_distance > left_distance+2----This is a random value:
            self.right_motor.turn_forward(speed-speed/10)
        if   left_distance > right_distance+2----This is a random value:
            self.left_motor.turn_forward(speed-speed/10)   

        """
    def drive_backwards(self, speed):
        self.left_motor.turn_backward(speed)
        self.right_motor.turn_backward(speed)
    
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def turn_off_motors(self):
        self.left_motor.shut_down()
        self.right_motor.shut_down()

    def drive_forward_distance(self, speed, distance):
        self.resetEncoderDistance()

        self.left_motor.turn_forward(speed)
        self.right_motor.turn_forward(speed)

        while (self.left_encoder < distance and self.right_encoder < distance):
            self.left_encoder.read_value()
            self.right_encoder.read_value()
        
        self.left_motor.stop()
        self.right_motor.stop()

        return 0
    
    def drive_backward_distance(self, speed, distance):
        self.resetEncoderDistance()
        
        self.left_motor.turn_backward(speed)
        self.right_motor.turn_backward(speed)

        while (self.left_encoder < distance and self.right_encoder < distance):
            self.left_encoder.read_value()
            self.right_encoder.read_value()
        
        self.left_motor.stop()
        self.right_motor.stop()

        return 0

    def drive_forward_until_distance_from_wall(self, distance_from_wall):
        return 0

    def drive_following_lane_curve(self, camera_value, speed = 50):

        '''
        I dette tilfellet her baserer vi oss på det som kalles DIFFERENTIAL STEERING.
        Teknikken baserer seg på å kalkulere en svingradius basert på hastigheten til hvert hjul.
        Grunnen til at dette bør brukes, er fordi vi gjerne vil at roboten skal justere vinkelen den kjører i
        basert på den hastigheten den allerede har - fremfor å la et hjul gå helt til null hver gang den skal snu.
        '''
        #self.wheel_diameter
        #self.wheel_space_between

        

        return 0
        
    #Function that maps the value from the camera input to a distance in the 
    def _map_value_lane_curve(self, camera_value):

        max_camera_value = 50
        min_camera_value = -50


        return 0

    #Reset the distance travelled variable of the encoders
    def resetEncoderDistance(self):
        self.left_encoder.distance_travelled = 0
        self.right_encoder.distance_travelled = 0
        return 0
'''
#Eksempel
def drive_forward_until_distance_from_wall(speed, distance_from_wall):
    
    #Initialize motor
    motor_left = ServoMotor(pin_out, "Left")
    motor = ServoMotor
    #Initialize distance sensor
    while distance_from_wall < distanceReading
        
'''
