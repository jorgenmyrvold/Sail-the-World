import cv2 as cv
import numpy as np
import os
import sys

STD_DIMENSIONS =  {
    "360p": (480, 360),
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv.VideoWriter_fourcc(*'H264'),
    'mp4': cv.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    '''
    Extracts video format from filename and sets it to the corresponding VIDEO_TYPE.
    Default goes to avi
    '''
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


def get_dims(cap, res='360p'):
    if res in STD_DIMENSIONS:    # Check to see if passed res argument is valid, and
        width, height = STD_DIMENSIONS[res]   # the STD_DIMENTIONS dict.
    else:
        width, height = STD_DIMENSIONS['360p']
    
    change_res(cap, height, width)
    return width, height


def main(filename):
    cap = cv.VideoCapture(0)
    dims = get_dims(cap, res='360p')
    video_type_cv = get_video_type(filename)
    
    out = cv.VideoWriter(filename, video_type_cv, 24.0, dims)
    
    while True:
        success, img = cap.read()
        out.write(img)
        if not success:
            print('Error reading image')
            
        cv.imshow('Image', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    out.release()
    cv.destroyAllWindows()        
    return 0

if __name__ == "__main__":
    main(sys.argv[1])   # Run file by: python3 camera.py [filename]
    