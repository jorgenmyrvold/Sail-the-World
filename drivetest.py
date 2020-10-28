from movements.drive import *

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def main():

    #Pins
    left_motor = 12
    right_motor = 13
    left_forward = 22
    left_backward = 5
    right_forward = 4
    right_backward = 17
    left_encoder = 23
    right_encoder = 24

    #Wheel parameters
    wheel_diameter = 6.4
    wheel_space_between = 21 #cm

    #Setup the controller
    drive_control = DriveControl(left_motor, right_motor, 
                left_forward, left_backward,
                right_forward, right_backward,
                left_encoder, right_encoder, 
                wheel_diameter, wheel_space_between)

    #TESTS
    test_drive_forward(drive_control)
    print("Bye")


def test_drive_forward(drive_control):

    test_distance = 500
    test_speed = 50
    drive_control.drive_forward_distance(test_speed, test_distance)

def test_turn(drive_control):
    return 0
                                
main()