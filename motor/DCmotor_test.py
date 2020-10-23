from DCMotor import *
import RPi.GPIO as GPIO
from time import sleep
from encoder import * 

GPIO.setmode(GPIO.BCM)

def test():

    #DECIDE PINS
    encoder_left = Encoder(23)
    
    encoder_right = Encoder (24)
    left_pwm = 12
    left_forward = 22
    left_backward = 5
    right_forward = 4
    right_backward = 17
    right_pwm = 13

    GPIO.add_event_detect(GPIO_LEFT_ENCODER, GPIO.BOTH, 
            callback=encoder_callback_test, bouncetime=100)



    LeftMotor = DCMotor(left_pwm, left_forward, left_backward, 'Left')
    RightMotor = DCMotor(right_pwm, right_forward, right_backward, 'Right')

    #testDirections(LeftMotor)
    #testDirections(RightMotor)
    #testRange(LeftMotor)
    #testRange(RightMotor)
    testings(LeftMotor,RightMotor)


def testings(motorClass_L, motorClass_R):    
    
    motorClass_L.stop()
    motorClass_R.stop()
    sleep(5)

    motorClass_L.turn_forward(30)
    sleep(3)
    motorClass_L.stop()
    sleep(3)
    motorClass_R.turn_forward(50)
    sleep(2)
    motorClass_L.stop()
    
    motorClass_R.stop()
    sleep(3)
    motorClass_L.shut_down()
    motorClass_R.shut_down()


def testDirections(motorClass):
    
    motorClass.turn_forward(20)
    sleep(3)
    motorClass.stop()
    sleep(1)

    motorClass.turn_backward(20)
    sleep(3)
    motorClass.stop()
    sleep(1)

    motorClass.turn_forward(100)
    sleep(10)
    motorClass.stop()
    sleep(1)

    motorClass.turn_backward(100)
    sleep(10)
    motorClass.stop()
    sleep(1)

def testRange(motorClass):

    motorClass.turn_forward(10)
    sleep(3)
    motorClass.turn_forward(20)
    sleep(3)
    motorClass.turn_forward(30)
    sleep(3)
    motorClass.turn_forward(40)
    sleep(3)
    motorClass.turn_forward(50)
    sleep(3)
    motorClass.turn_forward(60)
    sleep(3)
    motorClass.turn_forward(70)
    sleep(3)
    motorClass.turn_forward(80)
    sleep(3)
    motorClass.turn_forward(90)
    sleep(3)
    motorClass.turn_forward(100)
    sleep(3)
    motorClass.stop()
    motorClass.shut_down()

test()