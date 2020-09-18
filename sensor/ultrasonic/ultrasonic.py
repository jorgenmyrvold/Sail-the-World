from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=4)
while True:
    print('Distance: ', sensor.distance)
    sleep(1)