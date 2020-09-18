import cv2 as cv
import numpy as np

def thresholding(img):
    imgHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lowerWhite = np.array([100, 100, 100])
    upperWhite = np.array([179, 255, 255])
    maskWhite = cv.inRange(imgHsv, lowerWhite, upperWhite)
    return maskWhite
    

if __name__ == "__main__":
    pass