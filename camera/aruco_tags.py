import cv2 as cv
import numpy as np


aruco_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_100)
aruco_params = cv.aruco.DetectorParameters_create()

def aruco_detect_north_south(img):
    '''
    returns True if north, false if south
    '''
    marker_corners, _, _ = cv.aruco.detectMarkers(img, aruco_dict, parameters=aruco_params)
    if marker_corners:
        if marker_corners[0][0][0][1] < marker_corners[0][0][2][1] and marker_corners[0][0][1][1] < marker_corners[0][0][3][1]:    # y1 < y3 & y2 < y4 --> NORTH
            return 'NORTH'
        elif marker_corners[0][0][3][1] < marker_corners[0][0][1][1] and marker_corners[0][0][0][1] < marker_corners[0][0][2][1]:  # y4 < y2 & y1 < y3 --> EAST
            return 'SOUTH'
    else:
        return None


def aruco_print_corner(img):
    marker_corners, marker_IDs, rejected_candidates = cv.aruco.detectMarkers(img, aruco_dict, parameters=aruco_params)
    if marker_corners:
        print(marker_corners[0][0][0][1])
    else:
        print('No marker found')


def aruco_draw_detected_markers(img):
    marker_corners, marker_IDs, _ = cv.aruco.detectMarkers(img, aruco_dict, parameters=aruco_params)
    ret_img = cv.aruco.drawDetectedMarkers(img, marker_corners, marker_IDs)
    return ret_img


def aruco_detect_orientation(img):
    marker_corners, _, _ = cv.aruco.detectMarkers(img, aruco_dict, parameters=aruco_params)
    if marker_corners:
        if marker_corners[0][0][0][1] < marker_corners[0][0][2][1] and marker_corners[0][0][1][1] < marker_corners[0][0][3][1]:    # y1 < y3 & y2 < y4 --> NORTH
            return 'NORTH'
        elif marker_corners[0][0][3][1] < marker_corners[0][0][1][1] and marker_corners[0][0][0][1] < marker_corners[0][0][2][1]:  # y4 < y2 & y1 < y3 --> EAST
            return 'EAST'
        elif marker_corners[0][0][1][1] < marker_corners[0][0][3][1] and marker_corners[0][0][2][1] < marker_corners[0][0][0][1]:  # y2 < y4 & y3 < y1 --> WEST
            return 'WEST'
        elif marker_corners[0][0][2][1] < marker_corners[0][0][0][1] and marker_corners[0][0][3][1] < marker_corners[0][0][1][1]:  # y3 < y1 & y4 < y2 --> SOUTH
            return 'SOUTH'
        else:
            # print('No direction detected')
            return None
    else: 
        # print('No marker detected')
        return None


def park_north(cap, avg_len=5, max_atempts=100, display=False):
    '''
    Function to detect where to park. Checks until it has avg_len results of either north or south.
    If no direction is detected within the max_atempts first images the function returns True by default
    param: 
        cap: cv.VideoCapture object to read images
        avg_len: How many images to check before deciding. More images -> better presicion, but longer time
        max_atempts: Max images to check before giving up.
        diplay: currently no function.
    return:
        True if parking north, False if south
        If max_atempts is exceeded it returns True
    '''
    north_count = 0
    south_count = 0
    atempts = 0
    
    while north_count < avg_len and south_count < avg_len and atempts < max_atempts:
        atempts += 1
        
        _, img = cap.read()
        img = cv.resize(img, (480, 360))
        
        dir = aruco_detect_orientation(img)
        if dir == 'NORTH': north_count += 1
        elif dir == 'SOUTH': south_count += 1
    
    if north_count < south_count:
        print('Park SOUTH, atempts =', atempts)
        return False
    elif south_count < north_count:
        print('Park NORTH, atempts =', atempts)
        return True
    else:
        print('No direction detected. North =', north_count, 'South =', south_count, 'Atempts', atempts)
        return True


if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    
    for i in range(10):
        print(park_north(cap))
    
    # counter = 0
    
    # while True:
    #     counter += 1
    #     ret, img = cap.read()
    #     img = cv.resize(img, (480, 360))
        
    #     img_markers = aruco_draw_detected_markers(img)
    #     if counter%50 == 0: 
    #         aruco_print_corner(img)
    #         dir = aruco_detect_orientation(img)
    #         print(dir)
        
    #     cv.imshow('Markers', img_markers)
    #     if cv.waitKey(1) & 0xFF == ord('q'):
    #         break
        

        
    cap.release()
    cv.destroyAllWindows()