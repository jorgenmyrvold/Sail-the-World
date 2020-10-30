import RPi.GPIO as GPIO
from time import sleep


def raise_flag():
    flag_motor_pin = 7
    GPIO.setup(flag_motor_pin, GPIO.OUT)
    servo = GPIO.PWM(flag_motor_pin, 50)   # Pin and 50 = 50Hz

    servo.start(12)
    print('Raise flag!')
    sleep(1)
    
    servo.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    raise_flag()
