'''
Every function for driving in a specific manner will be given in this file. Using a combination of camera-, sensor-, and
motorfunctions we can make complex movement patterns that depend on conditions given by different inputs. 
'''
# Speed er i % fra 0 - 100
from servo_motor import ServoMotor
from encoder import Encoder
import math

def drive_forward(speed):
    motor_left = ServoMotor(LEFT_MOTOR_PIN)
    motor_right = ServoMotor(RIGHT_MOTOR_PIN)

#Dette navnet kan jobbes med
class DriveControl:

    def _init_(self, left_motor_pin, right_motor_pin, left_encoder_pin, right_encoder_pin):
        self.left_motor = ServoMotor(left_motor_pin, "Left")
        self.right_motor = ServoMotor(right_motor_pin, "Right")

        self.left_encoder = Encoder(left_encoder_pin, "Left")
        self.right_encoder = Encoder(right_encoder_pin, "Right")
    
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

    def drive_following_lane_curve(self, lane_curve, default_speed = 50):
        
        #First we map the value from the lane curve
        curve_value = map_value_lane_curve(lane_curve)
        #This value has to represent a distance left or right

        #We need a distance in front we want to reference
        target_distance = 10 #Find this later on

        #Now we can find the angle using the tangent of the target distance and the curve_value
        target_angle = curve_value / target_distance

        #Then we need to make the wheels reach the right point by driving in a slight angle
        


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
