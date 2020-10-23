import sys
import time
import signal
import cv2 as cv
import numpy as np
from camera.camera import *
from camera.aruco_tags import *
from tasks.raise_flag import raise_flag
from tasks.lighthouse import lighthouse
from tasks.wind_sausage import wind_sausage

# PIN ASSIGNMENTS

# LEFT_WHEEL_PIN = 12
# RIGHT_WHEEL_PIN = 13

# ULTRASONIC_RIGHT_AHEAD = Pin x
# ULTRASONIC_LEFT_AHEAD = Pin y
# ULTRASONIC_RIGHT_AFT = Pin z
# ULTRASONIC_LEFT_AFT = Pin w



def main():
    cap = cv.VideoCapture(0)   # Create a cameraobject to capture images
    
    # Determine if we have east or west start
    east_start = starting_east(cap, avg_len=10, display=False)   # TODO: Tune to detect correct colors
    
    # Follow inner line to south wall and Vindpølse
    drive_until_line()
    turn(90, east_start)  # Turn 90 deg to right or left depending on where we start
    follow_line_until_wall()
    
    # Vindpølse-taks
    wind_sausage(east_start)   # Do first task, follow wall to next, do second task
    
    # Follow outer line to north wall
    follow_line_until_wall()
    
    # Follow north wall to Værhane
    follow_wall_until_line(east_start, 0)   #follow_wall_until_line(start_pos, num_lines_to_cross)
    
    # Værhane-task: determine where to park
    park_north = park_north(cap, avg_len=5, max_atempts=100, display=False)  # Returns true or false
    
    # Follow norht wall to lighthouse
    turn(180, east_start)
    follow_wall_until_line(east_start, 1)  # Cross 1 line before stopping at the next
    
    # Lighthouse-task
    lighthouse_task(east_start)
    
    # Follow inner line to correct parking
    
    
    return 0

        
def raise_flag(e, msg):
    print('Raising flag!')
    exit()
    

if __name__ == "__main__":
    if len(sys.argv) < 2:   # Main competition program
        main()
        
    elif sys.argv[1] == 'comp':    # Test the complete main
        signal.signal(signal.SIGALRM, raise_flag)
        signal.alarm(96)   # Terminate main after 96 seconds to raise flag
        
        main()