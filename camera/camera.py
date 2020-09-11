import cv2 as cv

class Camera(object):
        
    def __init__(self, video_src):
        self.camera = cv.VideoCapture(video_src)
        if not self.camera.isOpened():
            print("Not able to open camera")
            exit()


    def capture(self, compressed=True):   # Default uses compressed img to save computational power
        success, img = self.camera.read()
        if not success:
            print("Error reading camera")
            
        if compressed:
            img = cv.resize(img, (640, 360))  # TODO: Check for correct dimentions
            return img
        else:
            return img

    
    def __del__(self):
        self.camera.release()
        self.camera = cv.destroyAllWindows()


if __name__ == "__main__":
    cam = Camera(0)
    while True:
        img = cam.capture()
        cv.imshow("Image", img)   
        cv.waitKey(1)        
        