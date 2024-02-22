import time
import cv2 as cv
import matplotlib.pyplot as plt
import picamera2 as picamera
import keyboard
	

class ManagementAI:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.results = []

    def Start(self):
        self.camera.resolution = (512, 384)
        self.camera.start_preview()

    def GetImage(self):
        fn = 'my_pic.jpg'
        self.camera.capture(fn)
        return fn
    
    def InputImagetoAI(self, fn):
        img = cv.imread(fn)
        grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        eye_cascade = cv.CascadeClassifier('/home/forpbl/workspace/haarcascade_eye.xml')
        eyerect = eye_cascade.detectMultiScale(grayimg)
        if len(eyerect) != 2:
            print("0")
            return 0
        else:
            print("1")
            return 1
    
    def Run(self, time_span):
        while True:
            key = cv.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            image_path = self.GetImage()
            result = self.InputImagetoAI(image_path)
            self.results.append(result)
            time.sleep(time_span)

ai = ManagementAI()
ai.Start()
time.sleep(1) #これはカメラ初期化の時間
ai.Run(1)  # 1秒ごとに処理を繰り返す

    
