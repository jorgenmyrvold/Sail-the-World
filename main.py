import sys
import time
import signal
import cv2 as cv
import numpy as np
import RPi.GPIO as GPIO
from camera.camera import *
from camera.aruco_tags import *
from tasks.raise_flag import raise_flag
from tasks.lighthouse import lighthouse_task
from tasks.wind_sausage import wind_sausage
from tasks.startcord import startcord
from sensor.rgb.rgb import *
from movements.drive import DriveControl
from follow_line import *
from drive_to_line import *
from gpiozero import DistanceSensor

# PIN ASSIGNMENTS

# LEFT_WHEEL_PIN = 12
# RIGHT_WHEEL_PIN = 13

# ULTRASONIC_RIGHT_AHEAD = Pin x
# ULTRASONIC_LEFT_AHEAD = Pin y
# ULTRASONIC_RIGHT_AFT = Pin z
# ULTRASONIC_LEFT_AFT = Pin w

GPIO.setmode(GPIO.BCM)

def main():
    cap = cv.VideoCapture(0)   # Create a cameraobject to capture images
    rgb_sensor = RGB(1)
    drive_controll = DriveControl()
    ultrasonic_front = DistanceSensor(echo=16, trigger=1)
    
    # Determine if we have east or west start
    start_west = check_west(rgb_sensor)
    print("Starting west: ", start_west)
    
    # Follow inner line to south wall and Vindpølse
    drive_to_black_line_detected(rgb_sensor, drive_controll)
    
    if start_west: drive_controll.turn_on_the_spot(180, 'CW')
    else: drive_controll.turn_on_the_spot(180, 'CC')
    
    follow_line_until_wall(cap, drive_controll, ultrasonic_front)
    
    # Vindpølse-taks
    # wind_sausage(east_start)   # Do first task, follow wall to next, do second task
    
    # Follow outer line to north wall
    # follow_wall_until_line()
    # follow_line_until_wall(cap, drive_controll)   #follow_wall_until_line(start_pos, num_lines_to_cross)
        
    # Follow north wall to Værhane
    # Værhane-task: determine where to park
    # park_north = park_north(cap, avg_len=5, max_atempts=100, display=False)  # Returns true or false
    
    # drive_controll.turn_on_the_spot(140, )
    # follow_wall_until_line(east_start, 1)  # Cross 1 line before stopping at the next
    
    # Lighthouse-task
    # lighthouse_task(east_start)
    
    # Follow inner line to correct parking
    
    sleep(100)
    return 0

        
def raise_flag_final(e, msg):
    raise_flag()
    exit()

def foo():
    for i in range(99999):
        print('foo')
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:   # Main competition program
        main()
        
    elif sys.argv[1] == 'comp':    # Test the complete main
        startcord()
        signal.signal(signal.SIGALRM, raise_flag_final)
        signal.alarm(96)   # Terminate main after 96 seconds to raise flag
        
        main()
