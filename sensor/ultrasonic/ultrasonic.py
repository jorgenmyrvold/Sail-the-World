from gpiozero import DistanceSensor
from time import sleep

if __name__ == "__main__":
    sensor = DistanceSensor(echo=12, trigger=7)
    while True:
        print('Distance: ', sensor.distance * 100)
        sleep(1)