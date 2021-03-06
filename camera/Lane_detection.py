import cv2 as cv
import numpy as np
# import camera.utils
from camera.utils import *
from time import sleep
import sys

# raspi camera dims: 640, 480
# mac camera dims: 1280, 640

curve_list = []

def getLaneCurve(img, avg_len=10, display=2):
    '''
    Takes images and evaluates input to determine grade of curve. Returns a float on the interval [-1, 1]
    describing how sharp the curve is.
    param:
        img: image to evaluate cuve from
        avg_len: number of the last frames to average to the final output
        display: Choose which images to display. 0: none, 1: result, 2: stack of all images
    return: 
        curve: float on the interval [-1, 1] describing curve. Negative is left curve, positive is right (I think...)
    '''
    #img = cv.resize(img, (640, 480))
    img_copy = img.copy()
    img_result = img.copy()
    
    img_thres = thresholding(img, 'HSV')   # Threshold image. Create usefull mask  # utils
    
    height, width, c = img.shape   # Warp image to see the image from right perspective
    points = read_trackbars("Warp bars", width=width, height=height)  # utils
    img_warped = warp_img(img, points, width, height)  # utils
    img_warped_masked = warp_img(img_thres, points, width, height)  # utils 
    img_warped_points = draw_points(img_copy, points, color=(0,0,255), size=15)  # utils
    
    # Get raw data about the curve direction
    mid_point, img_hist = get_histogram(img_warped_masked, display=True, threshold_percentage=0.3, region=4)  # Finds midpoint of line near to the car  # Utils 
    dir_point, img_hist = get_histogram(img_warped_masked, display=True, threshold_percentage=0.7, region=1)  # Finds dir based on the whole image  # Utils 
    curve_raw = dir_point - mid_point
    # curve_raw = dir_point
    
    # Average curve to get more stabile results
    curve_list.append(curve_raw)
    if len(curve_list) > avg_len:
        curve_list.pop(0)
    curve = int(sum(curve_list)/len(curve_list))
    
    # Display results.
    if display != 0:
        img_inv_warp = warp_img(img_warped_masked, points, width, height, inverse=True)  # Utils
        img_inv_warp_masked = img_inv_warp.copy()
        img_inv_warp_masked = cv.cvtColor(img_inv_warp, cv.COLOR_GRAY2BGR)
        img_inv_warp_masked[0:height // 3, 0:width] = 0, 0, 0
        img_lane_color = np.zeros_like(img)
        img_lane_color[:] = 0, 255, 0
        img_lane_color = cv.bitwise_and(img_inv_warp_masked, img_lane_color)
        img_result = cv.addWeighted(img_result, 1, img_lane_color, 1, 0)
        midY = int(height/2)
        cv.putText(img_result, str(curve), (width // 2 - 80, 85), cv.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
        # cv.putText(img, 'Original img', (0, 15), cv.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
        cv.putText(img_warped_points, 'warp points', (0, 15), cv.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
        cv.putText(img_warped, 'warped img', (0, 15), cv.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
        cv.putText(img_hist, 'Histogram', (0, 15), cv.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
        cv.putText(img_lane_color, 'Lane', (0, 15), cv.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)

        cv.line(img_result, (width // 2, midY), (width // 2 + (curve * 3), midY), (255, 0, 255), 5)
        cv.line(img_result, ((width // 2 + (curve * 3)), midY - 25), (width // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
        for x in range(-30, 30):
            w = width // 20
            cv.line(img_result, (w * x + int(curve // 50), midY - 10),
                     (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
        
    if display == 2:
        imgStacked = stackImages(0.7, ([img_warped_points, img_warped, img_inv_warp_masked],  # Utils 
                                             [img_hist, img_lane_color, img_result]))
        cv.imshow('ImageStack', imgStacked)
    elif display == 1:
        cv.imshow('Resutlt', img_result)
    
    # Normalization
    curve = curve/80
    if curve < -1: curve = -1
    if curve > 1: curve = 1
    
    return curve


if __name__ == "__main__":
    print('Live video')
    cap = cv.VideoCapture(0)
    
    initial_trackbar_vals = [150, 255, 100, 480]   # For warping of image
    initialize_trackbars("Warp bars", initial_trackbar_vals, width=640, height=480)  # Utils
    
    while True:
        ret, img = cap.read(0)
        # img = cv.resize(img, (640, 360))
        curve_val = getLaneCurve(img, avg_len=10, display=2)
        print(curve_val)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv.destroyAllWindows()
    cap.release()
        

