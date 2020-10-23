
class DifferentialSteering:

    #Class instructions:
    #1: Initialize for right behavioral parameters
    #2: Use set_**_velocity to calculate the turn radius
    #3: Use a new function to map how much you should turn
    #  
    def __init__(self, space_between_wheels, wheel_diameter):   
        self.wheel_space = space_between_wheels
        self.wheel_diameter = wheel_diameter

        #Set initial velocity values
        self.LV = 0
        self.RV = 0
        self.CV = (self.RV+self.LV)/2
        self.radius = 0
        
        self.sensitivity = 1

    def set_left_velocity(self, speed):
        self.LV = speed
        self._update_values()
    
    def set_right_velocity(self, speed): 
        self.RV = speed
        self._update_values()

    #In case it's cleaner to do both at the same time
    def set_velocities(self, left_velocity, right_velocity):
        self.set_left_velocity(left_velocity)
        self.set_right_velocity(right_velocity)

    #This is used to always keep the values updated, and is always run internally. 
    def _update_values(self):
        self.CV = (self.RV+self.LV)/2
        self.radius = (self.wheel_space*(self.LV+self.RV))/(2*(self.LV - self.RV))
        self._update_sensitivity(self)

    #The sensitivity has to be updated based on the velocity. 
    #High velocity -> High sensitivity
    #Low velocity -> Low sensitivity
    def _update_sensitivity(self):
        return 0


    #Get functions:
    def get_radius(self):
        return self.radius
    def get_left_velocity(self):
        return self.LV
    def get_right_velocity(self):
        return self.RV
    def get_central_velocity(self):
        return self.CV