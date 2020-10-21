from DCMotor import *
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

def test():

    #DECIDE PINS
    left_pwm = 13
    left_forward = 4
    left_backward = 17
    right_forward = 27
    right_backward = 19 
    right_pwm = 12

    LeftMotor = DCMotor(left_pwm, left_forward, left_backward, 'Left')
    RightMotor = DCMotor(right_pwm, right_forward, right_backward, 'Right')

    testDirections(LeftMotor)
    testDirections(RightMotor)
    testRange(LeftMotor)
    testRange(RightMotor)

def testDirections(motorClass):
    
    motorClass.turn_forward(50)
    sleep(3)
    motorClass.stop()
    sleep(1)

    motorClass.turn_backward(50)
    sleep(3)
    motorClass.stop()
    sleep(1)

    motorClass.turn_forward(100)
    sleep(3)
    motorClass.stop()
    sleep(1)

    motorClass.turn_backward(100)
    sleep(3)
    motorClass.stop()
    sleep(1)

    motorClass.shut_down() 

def testRange(motorClass):

    motorClass.turn_forward(10)
    sleep(1)
    motorClass.turn_forward(20)
    sleep(1)
    motorClass.turn_forward(30)
    sleep(1)
    motorClass.turn_forward(40)
    sleep(1)
    motorClass.turn_forward(50)
    sleep(1)
    motorClass.turn_forward(60)
    sleep(1)
    motorClass.turn_forward(70)
    sleep(1)
    motorClass.turn_forward(80)
    sleep(1)
    motorClass.turn_forward(90)
    sleep(1)
    motorClass.turn_forward(100)
    sleep(1)
    motorClass.stop()
    motorClass.shut_down()

test()