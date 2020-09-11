import cv2 as cv
import numpy as np

def thresholding(img):
    imgHsv = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    lowerWhite = np.array([0, 0, 0])
    upperWhite = np.array([179, 255, 255])
    maskWhite = cv.inRange(imgHsv, lowerWhite, upperWhite)
    return img
    

if __name__ == "__main__":
    pass