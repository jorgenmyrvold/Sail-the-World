import cv2 as cv
import numpy as np
from camera.camera import *
from camera.aruco_tags import *



def main():
    cap = cv.VideoCapture(0)   # Create a cameraobject to capture images
    
    # Determine if we have east or west start
    east_start = starting_east(cap, avg_len=10, display=False)
    
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