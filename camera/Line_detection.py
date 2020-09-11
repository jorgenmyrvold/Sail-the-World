import cv2 as cv2
import numpy as np
import utils

def getLaneCurve(img):
    imgThres = utils.thresholding(img)
    cv.imshow('Thresh img', imgThres)
    
    return None

if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    frame_counter = 0
    while True:
        # frame_counter += 1                                      # If a videoclip is used, uncomment
        # if cap.get(cv.CAP_PROP_FRAME_COUNT) == frame_counter:   # this section of code.
        #     cap.set(cv.CAP_PROP_FRAME_COUNT) = 0                # When uncommented the video will
        #     frame_counter = 0                                   # (hopefully) loop continuously
        
        success, img = cap.read()
        img = cv2.resize(img, (480,240))
        getLaneCurve(img)
        cv2.imshow('Vid', img)