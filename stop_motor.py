from movements.drive import *

GPIO.setmode(GPIO.BCM)

drive_control = DriveControl()
drive_control.stop()