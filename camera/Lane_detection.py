import cv2 as cv
import numpy as np
import utils
from time import sleep

curve_list = []

def getLaneCurve(img, avg_len=10, display=False):
    '''
    Takes images and evaluates input to determine grade of curve. Returns an int
    describing how sharp the curve is.
    
    param:
        img: image to evaluate cuve from
        avg_len: number of the last frames to average to the final output
        display: Weather or not to display images for debuging. False on gameday
        
    return: 
        curve: int describing sharpness of curve. Negative is right curve, positive is left
    '''
    img = cv.resize(img, (480, 240))
    img_copy = img.copy()
    
    img_thres = utils.thresholding(img)   # Threshold image. Create usefull mask
    
    height, width, c = img.shape   # Warp image to see the image from right perspective
    points = utils.read_trackbars("Warp bars")
    warped_img = utils.warp_img(img_thres, points, width, height)
    warped_img_points = utils.draw_points(img_copy, points, color=(0,0,255), size=15)
    
    # Get raw data about the curve direction
    mid_point, img_hist = utils.get_histogram(warped_img, display=True, threshold_percentage=0.3, region=4)
    dir_point, img_hist = utils.get_histogram(warped_img, display=True, threshold_percentage=0.7, region=1)
    curve_raw = dir_point - mid_point
    # print(curve_raw)
    
    # Average curve to get more stabile results
    curve_list.append(curve_raw)
    if len(curve_list) > avg_len:
        curve_list.pop(0)
    curve = int(sum(curve_list)/len(curve_list))
    
    
    cv.imshow('Original img', img)
    cv.imshow('Thresh img', img_thres)
    cv.imshow('Warped img', warped_img)
    cv.imshow('Warped points', warped_img_points)
    cv.imshow('Histogram and basepoint', img_hist)
    
    return curve


if __name__ == "__main__":
    img = cv.imread('camera/resources/demo_map_img.JPG')
    img = cv.resize(img, (480, 360))
    
    initial_trackbar_vals = [104, 118, 56, 240]   # Right turn: [131, 40, 113, 154]. Straight line: [104, 118, 56, 240]
    utils.initialize_trackbars("Warp bars", initial_trackbar_vals)
    
    while True:
        curve_val = getLaneCurve(img, avg_len=10, display=True)
        print(curve_val)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv.destroyAllWindows()

'''
# Code for testing lane detection with video.
# Currently not working
if __name__ == "__main__":
    cap = cv.VideoCapture('camera/resources/video.mp4')
    frame_counter = 0
    while True:
        # frame_counter += 1                                      # If a videoclip is used, uncomment
        # if cap.get(cv.CAP_PROP_FRAME_COUNT) == frame_counter:   # this section of code.
        #     cap.set(cv.CAP_PROP_FRAME_COUNT) = 0                # When uncommented the video will
        #     frame_counter = 0                                   # (hopefully) loop continuously
        
        success, img = cap.read()
        img = cv.resize(img, (480,360))
        getLaneCurve(img)
        cv.imshow('Vid', img)
'''
