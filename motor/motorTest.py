from servo_motor import ServoMotor
import GPIO
import time

def test():

    GPIO.setmode(GPIO.BCM)
    #initialize motor
    motor = ServoMotor(13, "Right")
    motor.turn_forward(50)
    time.sleep(7)
    motor.stop()

test()