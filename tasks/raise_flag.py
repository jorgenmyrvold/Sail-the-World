import RPi.GPIO as GPIO
from time import sleep


def raise_flag():
    
    flag_motor_pin = 7
    GPIO.setup(flag_motor_pin, GPIO.OUT)
    
    GPIO.output(flag_motor_pin, GPIO.HIGH)
    sleep(3)
    GPIO.output(flag_motor_pin,GPIO.LOW)


def raise_flag_servo():
    flag_motor_pin = 7
    GPIO.setup(flag_motor_pin, GPIO.OUT)
    servo = GPIO.PWM(flag_motor_pin, 50)   # Pin and 50 = 50Hz
    servo.start(0)
    
    servo.ChangeDutyCycle(0)   # Set to 0 pos
    sleep(2)
    servo.ChangeDutyCycle(100)  # raise flag
    
    servo.stop()
    GPIO.cleanup()

    

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    # raise_flag()
    raise_flag_servo()
