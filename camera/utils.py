import cv2 as cv
import numpy as np

def thresholding(img):
    '''
    Thresholds image and returns a white mask of the area that is white
    '''
    imgHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lowerWhite = np.array([0, 0, 197])
    upperWhite = np.array([179, 22, 255])
    maskWhite = cv.inRange(imgHsv, lowerWhite, upperWhite)
    return maskWhite
    
def warp_img(img, points, width, height):
    '''
    Warps image to get correct perspective of the track. 
    Try to keep the area small and close to the bottom where the robot
    actually is
    '''
    pts1 = np.float32(points)     # Points from capture
    pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    warped_img = cv.warpPerspective(img, matrix, (width, height))
    return warped_img

def nothing(a):
    '''
    Dummy function
    '''
    pass

def initialize_trackbars(win_name, initial_trackbar_vals, width=480, height=240):
    '''
    Creates a window for trackbars with parameters for warping the image.
    '''
    cv.namedWindow(win_name)
    cv.resizeWindow(win_name, 360, 240)
    cv.createTrackbar("Width top", win_name, initial_trackbar_vals[0], width//2, nothing)
    cv.createTrackbar("Height top", win_name, initial_trackbar_vals[1], height, nothing)
    cv.createTrackbar("Width bottom", win_name, initial_trackbar_vals[2], width//2, nothing)
    cv.createTrackbar("Height bottom", win_name, initial_trackbar_vals[3], height, nothing)    

def read_trackbars(win_name, width=480, height=240):
    '''
    Read trackbar values for the warping. Returns an np.array with 4 points to use
    for warping later.
    '''
    width_top = cv.getTrackbarPos('Width top', win_name)
    height_top = cv.getTrackbarPos('Height top', win_name)
    width_bottom = cv.getTrackbarPos('Width bottom', win_name)
    height_bottom = cv.getTrackbarPos('Height bottom', win_name)
    points = np.float32([(width_top, height_top), (width - width_top, height_top), 
                         (width_bottom, height_bottom), (width - width_bottom, height_bottom)])
    return points

def draw_points(img, points, color=(0,0,255), size=15):
    '''
    Draws points on an image. Draw on image, does not take a copy.
    param:
        img: imgage to draw points on
        points: list of points on format [(a,b),(c,d)...]
        color: color of points
        size: int for size
    return:
        img: same image with points drawn on
    '''
    for x in range(len(points)):
        cv.circle(img, (int(points[x][0]), int(points[x][1])), size, color, cv.FILLED)
    return img

def get_histogram(img, threshold_percentage=0.3, display=False, region=1):
    '''
    
    '''
    if region == 1:
        hist_values = np.sum(img, axis=0)
    else:
        hist_values = np.sum(img[img.shape[0]//region:, :], axis=0)
    
    # hist_values = np.sum(img, axis=0)
    max_value = np.max(hist_values)
    min_value = max_value * threshold_percentage
    
    index_array = np.where(hist_values >= min_value)
    base_point = int(np.average(index_array))
    
    if display:
        img_hist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for x, intensity in enumerate(hist_values):
            cv.line(img_hist, (x, img.shape[0]), (x, img.shape[0] - int(intensity//255//region)), (0,255,0), 1)
            cv.circle(img_hist, (base_point, img.shape[0]), 20, (255, 0, 0), cv.FILLED)
        return base_point, img_hist
    return base_point

# def stack_images(scale, img_array):
#     rows = len(img_array)
#     cols = len(img_array[0])
#     is_multiple_rows= isinstance(img_array[0], list)
#     width = img_array[0][0].shape[1]
#     height = img_array[0][0].shape[0]
    
#     if is_multiple_rows:
#         for x in range(0, rows):
#             for y in range(0, cols):
#                 if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
#                     img_array[x][y] = cv.resize(img_array[x][y], (0,0), None, scale, scale)
#                 else:
#                     img_aray[x][y] = cv.resize(img_array[x][y], (img_array[0][0].shape[1], img))

if __name__ == "__main__":
    pass