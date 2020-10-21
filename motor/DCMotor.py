import RPi.GPIO as GPIO
from time import sleep

class DCMotor:

    '''
    These motors have an operating pulse frequency of 50Hz and a duty cycle of 20ms.
    The specications for forward, backward and standstill motion are: 
        
        Full forward: 85% duty cycle
        Stop: 0% duty cycle

    Setting pin1 and pin2 high or low dictates wether the motor moves forward or backwards.
        
        pin1 = high && pin2 = low -> forward
        pin1 = low && pin2 = high -> backward
    '''

    # When you change the speed of a motor. Should the power be increased slowly? Too get a smoth acceleration?
    # Maybe this should be done in drive file. idk --  Ludvik
    def __init__(self, pwm_pin, pin_out_1, pin_out_2, orientation_of_motor, stop_percentage = 0):
        
        self.pwm_pin = pwm_pin
        self.pin1 = pin_out_1
        self.pin2 = pin_out_2

        self.full_forward = 85 #THIS SETS THE MAXIMUM PWM LIMIT. For the 6V motor, 85 should be fine. 
        self.stop_percentage = stop_percentage

        if(orientation_of_motor == "Left"):
            self.orientation = "Left"
        elif(orientation_of_motor == "Right"):
            self.orientation = "Right"
        else:
            raise Exception("The orientation of the motor must be 'Left' or 'Right'!")

        #Set the pwm high and initial speed 0
        GPIO.setup(pwm_pin, GPIO.OUT)
        self.pwm_instance = GPIO.PWM(pwm_pin, 50) #Sets a PWM instance with a frequency of 50 => 20ms.
        self.pwm_instance.start(self.stop_percentage) #Sets the start DUTY CYCLE to a ON-DUTY-PERCENT. 7.5% for stop. 

        #Set directional pins.
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        self.set_direction_forward() #Initial direction forwards
        
        #SPEED TRACKER - A variable that constantly tracks the current speed of the motor
        self.speed = 0

    def turn_forward(self, speed_percent):
        self.set_direction_forward()
        duty_cycle = self.__speed_to_duty_percentage(speed_percent)
        self.pwm_instance.ChangeDutyCycle(duty_cycle)
        print(self.orientation + "motor set to forward. Duty cycle: " + str(duty_cycle))
        self.speed = speed_percent #Update speed tracker

    def turn_backward(self, speed_percent):
        self.set_direction_backward()
        duty_cycle = self.__speed_to_duty_percentage(speed_percent)
        self.pwm_instance.ChangeDutyCycle(duty_cycle)
        print(self.orientation + "motor set to forward. Duty cycle: " + str(duty_cycle))
        self.speed = speed_percent #Update speed tracker

    def set_direction_forward(self):
            #Switches the output of the two h-bridge controller pins
            GPIO.output(self.pin1, GPIO.HIGH)
            GPIO.output(self.pin2, GPIO.LOW)
        
    def set_direction_backward(self):
            #Switches the output of the two h-bridge controller pins
            GPIO.output(self.pin1, GPIO.LOW)
            GPIO.output(self.pin2, GPIO.HIGH)

    #Stops the wheel, but not the program. The duty cycle is still active!
    def stop(self):
        self.pwm_instance.ChangeDutyCycle(self.stop_percentage)
        self.speed = 0 #Update speed tracker
        print(self.orientation + "motor stopped.")

    def getOrientation(self):
        return self.orientation

    #Stops the program entire
    def shut_down(self):
        self.speed = 0
        self.pwm_instance.stop()
        print(self.orientation + "motor shut down. Bye.")

    def __speed_to_duty_percentage(self, percentage):
        #Find the factor you have to multiply a percentage with to map perfectly from 100% to full_forward_percent
        print(percentage)
        factor = float(self.full_forward)/100.0
        duty_percentage = (self.stop_percentage) + factor * percentage
        print(duty_percentage)
        return duty_percentage