import RPi.GPIO as GPIO
from time import sleep


def raise_flag():
    
    flag_motor_pin = 7
    GPIO.setup(flag_motor_pin, GPIO.OUT)
    
    GPIO.output(flag_motor_pin, GPIO.HIGH)
    sleep(3)
    GPIO.output(flag_motor_pin,GPIO.LOW)
    
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    sleep(2)
    raise_flag()
