import cv2 as cv
import numpy as np
import utils
from time import sleep

def getLaneCurve(img):
    imgThres = utils.thresholding(img)
    cv.imshow('Thresh img', imgThres)
    
    return None


if __name__ == "__main__":
    img = cv.imread('camera/demo_map_img.JPG')
    img = cv.resize(img, (480, 360))
    
    getLaneCurve(img)
    # cv.imshow('Image', img)
    cv.waitKey(0)
    
    cv.destroyAllWindows()

'''
# Code for testing lane detection with video.
# Currently not working
if __name__ == "__main__":
    cap = cv.VideoCapture('video.mp4')
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
