"""
In this file we will find all the necessary functions and classes to drive the servo motor. 
"""

import RPi.GPIO as GPIO
from time import sleep

ledpin = 12				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 
while True:
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        sleep(0.01)
    sleep(0.5)
    
    for duty in range(100,-1,-1):
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)

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

        self.pwm_instance = GPIO.PWM(pin_out, 50) #Sets a PWM instance with a frequency of 50.
        self.pwm_instance.start(self.stop_percentage) #Sets the start DUTY CYCLE to a ON-DUTY-PERCENT. 7.5% for stop.  

        
    def drive_forward(self, speed_percent)


    def drive_backwards(self, speed_percent)

    def stop(self)
        self.pwm_instance.ChangeDutyCycle(self.stop_percentage)
        return 1

    def getOrientation(self)
        return self.orientation

    def shut_down(self)
        self.pwm_instance.stop()

    def __speed_to_duty_percentage(self, percentage)

        
