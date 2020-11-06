import cv2 as cv
import numpy as np


def print_camera_dims(cap):
    _, img = cap.read()
    print(img.shape)

def show_vid(cap):
    while True:
        _, img = cap.read()
        img = cv.resize(img, (640, 360))
        cv.imshow('img', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    
    print_camera_dims(cap)
    
    show_vid(cap)