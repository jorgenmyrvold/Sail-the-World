import cv2 as cv
import numpy as np
from camera.camera import *
from camera.aruco_tags import *
from sensor.rgb.rgb import *

# PIN ASSIGNMENTS

# LEFT_WHEEL_PIN = 
# RIGHT_WHEEL_PIN = 
# ULTRASONIC_RIGHT_AHEAD = Pin x
# ULTRASONIC_LEFT_AHEAD = Pin y
# ULTRASONIC_RIGHT_AFT = Pin z
# ULTRASONIC_LEFT_AFT = Pin w


def main():
    cap = cv.VideoCapture(0)   # Create a cameraobject to capture images

    rgb_sensor = RGB(1)
    
    # Determine if we have east or west start
    east_start = starting_east(cap, avg_len=10, display=False)

    is_west = check_west(rgb_sensor)

    #Drive until first line is discovered
    
    ''''
    Start driving function
    ''''

    detect_line(rgb_sensor)

    ''''
    Stop driving function and turn 90 degrees depending on east/west start
    ''''
    
    # Follow inner line to south wall and Vindpølse
    
    # Vindpølse-taks
    
    # Follow south wall to outer line
    
    # Follow outer line to north wall
    
    # Follow north wall to Værhane    
    
    # Værhane-task: determine where to park
    park_north = park_north(cap, avg_len=5, max_atempts=100, display=False)  # Returns true or false
    
    # Follow norht wall to lighthouse
    
    # Lighthouse-task
    
    # Follow inner line to correct parking
    
    return 0


if __name__ == "__main__":
    main()