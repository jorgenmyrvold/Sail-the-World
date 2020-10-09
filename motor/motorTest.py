from servo_motor import ServoMotor
import time

def test():

    #initialize motor
    motor = ServoMotor(13, "Right")
    motor.turn_forward(50)
    time.sleep(7)
    motor.stop()

test()