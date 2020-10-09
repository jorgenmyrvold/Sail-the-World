def drive_following_lane_curve(self, camera_value, speed = 50):
        
        #First we map the value from the lane curve
        curve_value = self._map_value_lane_curve(camera_value)
        #This value has to represent a distance left or right

        #We need a distance in front we want to reference
        target_distance = 10 #Find this later on

        #Now we can find the angle using the tangent of the target distance and the curve_value
        target_angle = curve_value / target_distance

        #Then we need to make the wheels reach the right point by driving in a slight angle
        return 0
        
    #Function that maps the value from the camera input to a distance in the 
    def _map_value_lane_curve(self, camera_value):

        max_camera_value = 50
        min_camera_value = -50

        
        return 0