import cv2 as cv
import numpy as np
import camera.utils


def starting_east(cap, avg_len=10, display=False):
    '''
    Yellow starting area east
    Blue starting area west
    
    param:
        img: image to be evaluated
        display: Display images for debuging
    return:
        True if east, False if west
    '''      
    east_start_counter = 0
    west_start_counter = 0
      
    lower_blue = np.array([0, 0, 0])         # TODO: tune correct values for masks
    upper_blue = np.array([179, 255, 255])
    lower_yellow = np.array([0, 0, 0])
    upper_yellow = np.array([179, 255, 255])
    
    for i in range(avg_len):
        ret, img = cap.read()
        if not ret:
            print('Error reading camera')
        else:
            img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

            mask_blue = cv.inRange(img_hsv, lower_blue, upper_blue)
            mask_yellow = cv.inRange(img_hsv, lower_yellow, upper_yellow)
        
            if display:
                img_stacked = utils.stackImages(0.7, [img, mask_blue, mask_yellow])
                cv.imshow('img, blue mask, yellow mask', img_stacked)
    
            if sum(mask_blue) > sum(mask_yellow):
                east_start_counter += 1
            else:
                west_start_counter += 1

    return True if east_start_counter > west_start_counter else False

if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    
    while True:
        ret, img = cap.read()
        east_start = starting_east(img, display=True)
        print(east_start)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    cv.destroyAllWindows()
    cap.release()