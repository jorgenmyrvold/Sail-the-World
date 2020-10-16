'''
This file is for tuning the HSV variables for a video. 
Under main, choose video source in the camera constructor
'''

import cv2 as cv
import numpy as np
import sys


def empty(a):
    pass

def create_HSV_trackbar_window():
    '''
    Creates a window with 6 trackbars for tuning of HSV
    '''
    cv.namedWindow("HSV Trackbar")
    cv.resizeWindow("HSV Trackbar", 640, 240)
    cv.createTrackbar("HUE_min", "HSV Trackbar", 0, 179, empty)
    cv.createTrackbar("HUE_max", "HSV Trackbar", 179, 179, empty)
    cv.createTrackbar("SAT_min", "HSV Trackbar", 0, 255, empty)
    cv.createTrackbar("SAT_max", "HSV Trackbar", 255, 255, empty)
    cv.createTrackbar("VAL_min", "HSV Trackbar", 0, 255, empty)
    cv.createTrackbar("VAL_max", "HSV Trackbar", 255, 255, empty)

def read_HSV_trackbar_values():
    '''
    Reads all 6 trackbar values and returns them as numpy arrays for upper and
    lower limit for a mast
    
    Returns:
        upper: np.array of upper values of hsv
        lower: np.array of lower values of hsv
    '''
    h_min = cv.getTrackbarPos("HUE_min", "HSV Trackbar")
    h_max = cv.getTrackbarPos("HUE_max", "HSV Trackbar")
    s_min = cv.getTrackbarPos("SAT_min", "HSV Trackbar")
    s_max = cv.getTrackbarPos("SAT_max", "HSV Trackbar")
    v_min = cv.getTrackbarPos("VAL_min", "HSV Trackbar")
    v_max = cv.getTrackbarPos("VAL_max", "HSV Trackbar")
    
    upper = np.array([h_max, s_max, v_max])
    lower = np.array([h_min, s_min, v_min])
    
    return upper, lower

def create_HLS_trackbar_window():
    '''
    Creates a window with 6 trackbars for tuning of HLS
    '''
    cv.namedWindow("HLS Trackbar")
    cv.resizeWindow("HLS Trackbar", 640, 240)
    cv.createTrackbar("HUE_min", "HLS Trackbar", 0, 179, empty)
    cv.createTrackbar("HUE_max", "HLS Trackbar", 179, 179, empty)
    cv.createTrackbar("LIG_min", "HLS Trackbar", 0, 255, empty)
    cv.createTrackbar("LIG_max", "HLS Trackbar", 255, 255, empty)
    cv.createTrackbar("SAT_min", "HLS Trackbar", 0, 255, empty)
    cv.createTrackbar("SAT_max", "HLS Trackbar", 255, 255, empty)
    
def read_HLS_trackbar_values():
    '''
    Reads all 6 trackbar values and returns them as numpy arrays for upper and
    lower limit for a mast
    
    Returns:
        upper: np.array of upper values of hls
        lower: np.array of lower values of hls
    '''
    h_min = cv.getTrackbarPos("HUE_min", "HLS Trackbar")
    h_max = cv.getTrackbarPos("HUE_max", "HLS Trackbar")
    v_min = cv.getTrackbarPos("LIG_min", "HLS Trackbar")
    v_max = cv.getTrackbarPos("LIG_max", "HLS Trackbar")
    s_min = cv.getTrackbarPos("SAT_min", "HLS Trackbar")
    s_max = cv.getTrackbarPos("SAT_max", "HLS Trackbar")
    
    upper = np.array([h_max, s_max, v_max])
    lower = np.array([h_min, s_min, v_min])
    
    return upper, lower


# For tuning on image.
if __name__ == "__main__":
    if len(sys.argv) < 2:
        cap = cv.VideoCapture(0)
        create_HLS_trackbar_window()
        create_HSV_trackbar_window()
        
        while True:
            _, img = cap.read()
            img_hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
            img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
            
            upper_hsv, lower_hsv = read_HSV_trackbar_values()
            upper_hls, lower_hls = read_HLS_trackbar_values()
            mask_hsv = cv.inRange(img_hsv, lower_hsv, upper_hsv)
            mask_hls = cv.inRange(img_hls, lower_hls, upper_hls)
            res_hsv = cv.bitwise_and(img, img, mask=mask_hsv)
            res_hls = cv.bitwise_and(img, img, mask=mask_hls)
            
            mask_hsv = cv.cvtColor(mask_hsv, cv.COLOR_GRAY2BGR)   # Converts img to right dimentions to show in stack
            mask_hls = cv.cvtColor(mask_hls, cv.COLOR_GRAY2BGR)   # Converts img to right dimentions to show in stack
            h_stack_hsv = np.hstack([img_hls, mask_hsv, res_hsv])     # Stacks the array in a single window
            h_stack_hls = np.hstack([img_hsv, mask_hls, res_hls])     # Stacks the array in a single window
            
            cv.imshow("HSV", h_stack_hsv)
            cv.imshow("HLS", h_stack_hls) 
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            
        cv.destroyAllWindows()
        cap.release()
        
        
    elif sys.argv[1] == 'img':
        img = cv.imread('camera/resources/demo_map_img.JPG')
        img = cv.resize(img, (480,240))
        img_hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
        img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        create_HLS_trackbar_window()
        create_HSV_trackbar_window()
        
        while True:
            upper_hsv, lower_hsv = read_HSV_trackbar_values()
            upper_hls, lower_hls = read_HLS_trackbar_values()
            mask_hsv = cv.inRange(img_hsv, lower_hsv, upper_hsv)
            mask_hls = cv.inRange(img_hls, lower_hls, upper_hls)
            res_hsv = cv.bitwise_and(img, img, mask=mask_hsv)
            res_hls = cv.bitwise_and(img, img, mask=mask_hls)
            
            mask_hsv = cv.cvtColor(mask_hsv, cv.COLOR_GRAY2BGR)   # Converts img to right dimentions to show in stack
            mask_hls = cv.cvtColor(mask_hls, cv.COLOR_GRAY2BGR)   # Converts img to right dimentions to show in stack
            h_stack_hsv = np.hstack([img_hls, mask_hsv, res_hsv])     # Stacks the array in a single window
            h_stack_hls = np.hstack([img_hsv, mask_hls, res_hls])     # Stacks the array in a single window
            
            cv.imshow("HSV", h_stack_hsv)
            cv.imshow("HLS", h_stack_hls) 
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            
        cv.destroyAllWindows()
    
    elif sys.argv[1] == 'vid':
        # For tuning on live video. Should be possible with video clip 
        # as well, but not at the moment
        cap = cv.VideoCapture(0)
        create_HSV_trackbar_window()

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read from camera")
                break

            upper, lower = read_HSV_trackbar_values()
            mask = cv.inRange(frame, lower, upper)
            masked_frame = cv.bitwise_and(frame, frame, mask=mask)
            
            mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)            # Converts img to right dimentions to show in stack
            h_stack_img = np.hstack([frame, mask, masked_frame])   # Stacks the array in a single window        
            
            cv.imshow("Images", h_stack_img)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        
        cv.destroyAllWindows()
