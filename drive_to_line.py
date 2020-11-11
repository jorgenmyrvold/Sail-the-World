from sensor.rgb.rgb import *
from movements.drive import *
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def drive_to_black_line_detected(rgb_sensor, motors, speed=15):
    motors.drive_forwards(speed)
    while(detect_line(rgb_sensor) != True):
        print('Line not detected')
        sleep(0.5)
    print('Detected black line!')
    motors.drive_backwards(5)
    sleep(0.5)
    motors.stop()
    return True

if __name__ == "__main__":

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
    wheel_diameter = 6.4
    wheel_space_between = 21 #cm

    #Setup the controller
    drive_control = DriveControl(left_motor, right_motor, 
                left_forward, left_backward,
                right_forward, right_backward,
                left_encoder, right_encoder, 
                wheel_diameter, wheel_space_between)
    rgb_sensor = RGB(1)
    speed = 15

    drive_to_black_line_detected(rgb_sensor, drive_control, speed)