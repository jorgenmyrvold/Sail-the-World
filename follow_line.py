import cv2 as cv
from camera.Lane_detection import getLaneCurve
from movements.drive import drive_following_lane_curve
from camera.utils import initialize_trackbars




if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    
    initial_trackbar_vals = [150, 255, 100, 480]   # For warping of image
    initialize_trackbars("Warp bars", initial_trackbar_vals, width=640, height=480)
    
    while True:
        ret, img = cap.read(0)
        curve_val = getLaneCurve(img, avg_len=10, display=2)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv.destroyAllWindows()
    cap.release()