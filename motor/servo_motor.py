"""
In this file we will find all the necessary functions and classes to drive the servo motor. 
"""

import RPi.GPIO as GPIO
from time import sleep

class servo_motor:

    '''
    These motors have an operating pulse frequency of 50Hz and a duty cycle of 20ms.
    The specications for forward, backward and standstill motion are: 
        
        Full forward: 10% duty cycle
        Stop: 7.5% duty cycle
        Full backwards: 5% duty cycle

    '''

    def __init__(self, pin_out, orientation_of_motor)
        self.pin_out = pin_out
        
        self.stop_percentage = 7.5

        if(orientation_of_motor == "Left"):
            self.orientation = "Left"
        else if(orientation_of_motor == "Right"):
            self.orientation = "Right"
        else:
            raise Exception("The orientation of the motor must be 'Left' or 'Right'!")

        self.pwm_instance = GPIO.PWM(pin_out, 50) #Sets a PWM instance with a frequency of 50 => 20ms.
        self.pwm_instance.start(self.stop_percentage) #Sets the start DUTY CYCLE to a ON-DUTY-PERCENT. 7.5% for stop.  

        
    def drive_forward(self, speed_percent)
        self.pwm_instance.ChangeDutyCycle(self.__speed_to_duty_percentage(speed_percent, "Forwards"))

    def drive_backwards(self, speed_percent)
        self.pwm_instance.ChangeDutyCycle(self.__speed_to_duty_percentage(speed_percent, "Backwards"))

    def stop(self)
        self.pwm_instance.ChangeDutyCycle(self.stop_percentage)
        return 1

    def getOrientation(self)
        return self.orientation

    def shut_down(self)
        self.pwm_instance.stop()

    #This function maps the speed percentage from input (0 - 100) to required in duty cycle (5 - 7.5 - 10)
    def __speed_to_duty_percentage(self, percentage, direction)
        if direction == "Forwards":
            return 7.5 + (1/40) * percentage
        else if direction == "Backwards":
            return 7.5 - (1/40) * percentage
        else:
            raise Exception("This function requires a specified driving direction")

