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
    right_forward = 27
    right_backward = 17
    left_encoder = 23
    right_encoder = 24

    #Wheel parameters
    wheel_diameter = 6.6
    wheel_space_between = 21 #cm

    #Setup the controller
    drive_control = DriveControl(left_motor, right_motor, 
                left_forward, left_backward,
                right_forward, right_backward,
                left_encoder, right_encoder, 
                wheel_diameter, wheel_space_between)

    #TESTS
    #test_drive_forward(drive_control)
    #test_turn_backwards(drive_control)
    #drive_control.turn_on_the_spot( 180, "CW")
    #test_drive_backward(drive_control)
    #drive_control.encoder_distance_test(30, 100)
    #drive_control.test_forward(30, 100)
    drive_control.test_forward(50,100)
    drive_control.turn_off_motors()
    print("Bye")

def test_drive_forward(drive_control):


    
    #test_distance = 100
    #test_speed = 70
    #drive_control.drive_forward_distance(test_speed, test_distance)
    drive_control.left_encoder.print_encoder_values()
    drive_control.right_encoder.print_encoder_values()

def test_drive_backward(drive_control):
    test_distance = 100
    test_speed = 50
    drive_control.drive_backward_distance(test_speed, test_distance)

def test_turn_backwards(drive_control):
    test_distance = 100
    test_speed = 50
    drive_control.motor_test(test_speed)
    return 0

def test_turn(drive_control):
    return 0
                          
main()