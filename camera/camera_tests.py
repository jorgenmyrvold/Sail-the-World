import cv2 as cv
import numpy as np


def print_camera_dims(cap):
    _, img = cap.read()
    print(img.shape)


if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    
    print_camera_dims(cap)