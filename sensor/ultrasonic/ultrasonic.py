from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=1)
while True:
    print('Distance: ', sensor.distance)
    sleep(1)