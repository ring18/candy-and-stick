class CandyStickClass():
    def __init__(self):
        self.check_result = False

    def check_communication(self):
        self.check_result = True

    def out_check_result(self):
        if self.check_result == False:
            print("Error")
        else:
            print("Correct")
            self.start_face_recognition()

    def start_face_recognition(self):
        print("faceRecognition Start")
        return 1


'''
ROBOTSTATUS = 1
boot = CandyStickClass()
#ロボットからのステータス送信
if ROBOTSTATUS == 1:
    boot.checkCommunication()
boot.out_check_result()
'''


