from gpiozero import DistanceSensor
from time import sleep
import numpy as np

class Ultrasonic:

    def __init__(self, e, t):
        #Translates from GPIO.BOARD to GPIO.BCM
        board_to_bcm = np.array([-1, -1, -1, 2, -1, 3, -1, 4, 14, -1, 15, 17, 18, 27, -1, 22, 23, -1, 24, 10, -1, 9, 25, 11, 8, -1, 7, 0, 1, 5, -1, 6, 12, 13, -1, 19, 16, 26, 20, -1, 21])
        
        #Creating a DistanceSensor object
        self.sensor = DistanceSensor(board_to_bcm[e], board_to_bcm[t])
    
    def get_distance(self):
        #returns distance in cm
        return self.sensor.distance

if __name__ == "__main__":
    #sensor = DistanceSensor(echo=18, trigger=1)
    ultrasonic_1 = Ultrasonic(36, 28) #Triggger: GPIO1, Echo: GPIO16
    while True:
        print('Distance: ', ultrasonic_1.get_distance)
        sleep(1)