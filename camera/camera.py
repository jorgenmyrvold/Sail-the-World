import cv2 as cv

class Camera(object):
        
    def __init__(self, video_src):
        '''
        Constructer for camera object. 
        Param: video_src: 0 for internal camera, filename for other file
        '''
        self.camera = cv.VideoCapture(video_src)
        if not self.camera.isOpened():
            print("Not able to open camera")
            exit()


    def capture(self, compressed=True):
        '''
        Version of cv .read(), but compresses image by default and prints error
        if camera is not read correctly.
        '''
        success, img = self.camera.read()
        if not success:
            print("Error reading camera")
            
        if compressed:
            img = cv.resize(img, (480, 360))  # TODO: Check for correct dimentions
            return img
        else:
            return img

    
    def __del__(self):
        self.camera.release()
        self.camera = cv.destroyAllWindows()

if __name__ == "__main__":
    pass