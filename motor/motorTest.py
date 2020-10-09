from servo_motor import ServoMotor
import RPi.GPIO as GPIO
import time

def test():

    GPIO.setmode(GPIO.BCM)
    #initialize motor
    motor = ServoMotor(13, "Right")
    motor.turn_forward(50)
    time.sleep(3)
    motor.turn_forward(90)
    time.sleep(3)
    motor.stop()
    time.sleep(2)
    motor.turn_backward(20)
    time.sleep(3)
    motor.stop()

test()