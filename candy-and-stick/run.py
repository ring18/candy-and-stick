from candyStickController import CandyStickClass
from aiManager import ManagementAI
import time

ROBOTSTATUS = 1 #ロボットとの通信状況
TIMESPAN = 5 #推論を行う間隔

boot = CandyStickClass()

if ROBOTSTATUS == 1:
    boot.checkCommunication()
boot.out_check_result()

if boot.start_face_recognition() == 1:
    ai = ManagementAI()
    ai.Start()
    time.sleep(TIMESPAN) #これはカメラ初期化の時間
    ai.Run()  # 1秒ごとに処理を繰り返す




