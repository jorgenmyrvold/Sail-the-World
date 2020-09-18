'''
This file is for tuning the HSV variables for a video. 
Under main, choose video source in the camera constructor
'''

import cv2 as cv
import numpy as np
from camera import Camera


def empty(a):
    pass

def create_HSV_trackbar_window():
    '''
    Creates a window with 6 trackbars for tuning of HSV
    '''
    cv.namedWindow("HSV")
    cv.resizeWindow("HSV", 640, 240)
    cv.createTrackbar("HUE_min", "HSV", 0, 179, empty)
    cv.createTrackbar("HUE_max", "HSV", 179, 179, empty)
    cv.createTrackbar("SAT_min", "HSV", 0, 255, empty)
    cv.createTrackbar("SAT_max", "HSV", 255, 255, empty)
    cv.createTrackbar("VAL_min", "HSV", 0, 255, empty)
    cv.createTrackbar("VAL_max", "HSV", 255, 255, empty)

def read_HSV_trackbar_values():
    '''
    Reads all 6 trackbar values and returns them as numpy arrays for upper and
    lower limit for a mast
    
    Returns:
        upper: np.array of upper values of hsv
        lower: np.array of lower values of hsv
    '''
    h_min = cv.getTrackbarPos("HUE_min", "HSV")
    h_max = cv.getTrackbarPos("HUE_max", "HSV")
    s_min = cv.getTrackbarPos("SAT_min", "HSV")
    s_max = cv.getTrackbarPos("SAT_max", "HSV")
    v_min = cv.getTrackbarPos("VAL_min", "HSV")
    v_max = cv.getTrackbarPos("VAL_max", "HSV")
    
    upper = np.array([h_max, s_max, v_max])
    lower = np.array([h_min, s_min, v_min])
    
    return upper, lower


if __name__ == "__main__":

    cap = cv.VideoCapture('video.avi')
    create_HSV_trackbar_window()

    while True:
        ret, frame = cap.read()
        frame = cv.resize(frame, (480, 360))
        
        upper, lower = read_HSV_trackbar_values()
        mask = cv.inRange(frame, lower, upper)
        masked_frame = cv.bitwise_and(frame, frame, mask=mask)
        
        mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)            # Converts img to right dimentions to show in stack
        h_stack_img = np.hstack([frame, mask, masked_frame])  # Stacks the array in a single window        
        img_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        
        cv.imshow("Images", h_stack_img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
