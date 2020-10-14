'''
Every function for driving in a specific manner will be given in this file. Using a combination of camera-, sensor-, and
motorfunctions we can make complex movement patterns that depend on conditions given by different inputs. 
'''
from servo_motor import *

def drive_forward(speed):
    motor_left = ServoMotor(LEFT_MOTOR_PIN)
    motor_right = ServoMotor(RIGHT_MOTOR_PIN)

#Dette navnet kan jobbes med
class DriveControl:

    def _init_(self, left_motor_pin, right_motor_pin):
        self.left_motor = ServoMotor(left_motor_pin, "Left")
        self.right_motor = ServoMotor(right_motor_pin, "Right")
    
    def drive_forwards(self, speed):
        self.left_motor.turn_forward(speed)
        self.right_motor.turn_forward(speed)

    def drive_backwards(self, speed):
        self.left_motor.turn_backward(speed)
        self.right_motor.turn_backward(speed)
    
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def turn_off_motors(self):
        self.left_motor.shut_down()
        self.right_motor.shut_down()

    def drive_forward_distance(self, distance):
        return 0
    
    def drive_backward_distance(self, distance):
        return 0

    def drive_forward_until_distance_from_wall(self, distance_from_wall):
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
