import sys
import time
import cv2 as cv
import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from camera.Lane_detection import getLaneCurve
from movements.drive import DriveControl
from camera.utils import initialize_trackbars
from time import sleep


# def follow_line_until_wall(cap, ultrasonic_front, drive_control, distance_from_wall=5):
def follow_line_until_wall(cap, drive_control):
    # close_to_wall_count = 0
    # while close_to_wall_count < 3:
    #     if ultrasonic_front < distance_from_wall: close_to_wall_count += 1
    #     if ultrasonic_front > distance_from_wall: close_to_wall_count = 0
    
    timeout = time.time() + 20   # timeout after 20 sec
    while time.time() < timeout:
        ret, img = cap.read(0)
        if not ret:
            print("Error reading camera!")
        curve_val = getLaneCurve(img, avg_len=10, display=0)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        drive_control.drive_following_lane_curve(curve_val, timeout-time.time())
        #sleep(0.2)
    


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    if len(sys.argv) < 2:
        
        cap = cv.VideoCapture(0)
        drive_control = DriveControl()
        # ultrasonic_front = DistanceSensor(echo=12, trigger=7)
        
        initial_trackbar_vals = [150, 255, 100, 480]   # For warping of image
        initialize_trackbars("Warp bars", initial_trackbar_vals, width=640, height=480)
        
        follow_line_until_wall(cap, drive_control)
        
        drive_control.stop()
        cv.destroyAllWindows()
        cap.release()
    
    elif sys.argv[1] == 'test':
        drive_control = DriveControl()
        drive_control.left_motor.turn_forward(30)
        sleep(2)
        drive_control.left_motor.turn_backward(30)
        sleep(2)
        drive_control.left_motor.stop()
        sleep(2)
        drive_control.right_motor.turn_forward(30)
        sleep(2)
        drive_control.right_motor.turn_backward(30)
        sleep(2)
        drive_control.right_motor.stop()
        sleep(2)