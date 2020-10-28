'''
Every function for driving in a specific manner will be given in this file. Using a combination of camera-, sensor-, and
motorfunctions we can make complex movement patterns that depend on conditions given by different inputs. 
'''
# Speed er i % fra 0 - 100
from motor.DCMotor import *
from motor.encoder import *
import math
from time import sleep


#Dette navnet kan jobbes med
class DriveControl:

    def __init__(self, left_motor_pin, right_motor_pin, 
        left_forward_pin, left_backward_pin,
        right_forward_pin, right_backward_pin,
        left_encoder_pin, right_encoder_pin, 
        wheel_diameter, 
        wheel_space_between):

        self.left_motor = DCMotor(left_motor_pin, left_forward_pin, left_backward_pin, "Left")
        self.right_motor = DCMotor(right_motor_pin, right_forward_pin, right_backward_pin, "Right")

        self.left_encoder = Encoder(left_encoder_pin)
        self.right_encoder = Encoder(right_encoder_pin)

        self.wheel_diameter = wheel_diameter
        self.wheel_space_between = wheel_space_between

        self.lane_curve_sensitivity = 0.1 #The change in cameravalue required to change the turning values
        self.lane_curve_margin = 0.1 #The margin in which the lane curve following goes form straight forward to turn
        self.last_camera_value = 0

    def drive_forward_distance(self, speed, distance):
        #her the encoder should be implementet in order to check if both motors have the same speed
        # same power doesent nesesarry mean equal speed
        # Extra note: maybe the "variable" speed should be changed to "power"?
        self.left_encoder.resetEncoder()
        self.right_encoder.resetEncoder()

        current_speed = speed
        while(self.left_encoder.distance < distance and self.right_encoder.distance < distance):
            sleep(0.2)
            #Correct errors
            if abs(self.left_encoder.current_value - self.right_encoder.current_value) > 10:
                if self.left_encoder.current_value > self.right_encoder.current_value:
                    current_speed = current_speed-(0.2)*current_speed
                    self.left_motor.turn_forward(current_speed) #Watch out for the speed reduction value
                    print("Slowed down left motor")
                    print("left distance: ",self.left_encoder.distance," Right distance: ",self.right_encoder.distance)
                else:
                    current_speed = current_speed-(0.2)*current_speed
                    self.right_motor.turn_forward(current_speed) #Watch out for the speed reduction value
                    print("Slowed down right motor")
                    print("left distance: ",self.left_encoder.distance," Right distance: ",self.right_encoder.distance)
            else:
                current_speed = speed
                self.left_motor.turn_forward(speed)
                self.right_motor.turn_forward(speed)

        self.stop()

        return self.left_encoder.distance, self.right_encoder.distance       


    def drive_backwards(self, speed):
        self.left_motor.turn_backward(speed)
        self.right_motor.turn_backward(speed)
    
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def turn_off_motors(self):
        self.left_motor.shut_down()
        self.right_motor.shut_down()

    # def drive_forward_distance(self, speed, distance):
    #     self.resetEncoderDistance()

    #     self.left_motor.turn_forward(speed)
    #     self.right_motor.turn_forward(speed)

    #     while (self.left_encoder < distance and self.right_encoder < distance):
    #         self.left_encoder.read_value()
    #         self.right_encoder.read_value()
        
    #     self.left_motor.stop()
    #     self.right_motor.stop()

    #     return 0
    
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

    #Must be used in a WHILE-LOOP
    def drive_following_lane_curve(self, camera_value, main_speed = 50):
        #Negative values imply turn left and positive imply turn right in this case
        if abs(camera_value) > abs(self.last_camera_value) + abs(self.lane_curve_sensitivity): 
            if (camera_value < 0 - self.lane_curve_margin):
                self.left_motor.turn_forward(main_speed*(1-camera_value))
                self.right_motor.turn_forward(main_speed*camera_value)
            elif (camera_value > 0 + self.lane_curve_margin):
                self.right_motor.turn_forward(main_speed*(1-camera_value))
                self.left_motor.turn_forward(main_speed*camera_value)
            else:
                self.right_motor.turn_forward(main_speed)
                self.left_motor.turn_forward(main_speed)
        else:
            if self.right_motor.speed == 0 and self.left_motor.speed == 0:
                self.right_motor.turn_forward(main_speed)
                self.left_motor.turn_forward(main_speed)

        self.last_camera_value = camera_value
        return 0

    def turn_degrees(self, degrees):
        self.left_motor.stop()
        self.right_motor.stop()

        #Turn such that the encoders make a turndistance equal to what you should expect
        
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
