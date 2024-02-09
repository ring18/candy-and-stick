import time
import cv2 as cv
import matplotlib.pyplot as plt
import picamera2 as picamera
import keyboard

#fn = "image.jpg"

i = 0
while True:
	with picamera.Picamera2() as camera:
		fn = f'my_pic{i}.jpg'
		camera.resolution = (512, 384)
		camera.start_preview()
		time.sleep(1)
		camera.start()
		print("kokoitta")
		camera.capture_file(fn)
	
		# 撮影した写真を読み込む
		img = cv.imread(fn)

		# 顔検出の処理効率化のために、写真の情報量を落とす（モノクロにする）
		grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

		# 顔検出のための学習元データを読み込む
		face_cascade = cv.CascadeClassifier('/home/forpbl/workspace/haarcascade_frontalface_default.xml')
		# 目検出のための学習元データを読み込む
		eye_cascade = cv.CascadeClassifier('/home/forpbl/workspace/haarcascade_eye.xml')
		# 顔検出を行う
		facerect = face_cascade.detectMultiScale(grayimg, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
		# 目検出を行う
		eyerect = eye_cascade.detectMultiScale(grayimg)
	
		#print(facerect)
		print(eyerect)

		# 顔を検出した場合
		if len(facerect) > 0:
			# 検出した場所すべてに赤色で枠を描画する
			for rect in facerect:
				cv.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=3)

		# 目を検出した場合
		if len(eyerect) > 0:
		# 検出した場所すべてに緑色で枠を描画する
			for rect in eyerect:
				cv.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 255, 0), thickness=3)

		# 結果の画像を表示する
		cv.imshow('camera', img)
		#cv.cvShowImage('camera', img)
		# 結果を書き出す
		cv.imwrite(fn, img)
		camera.close()
		# plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
		# 何かキーが押されるまで待機する
		# cv.waitKey(0)
		# 表示したウィンドウを閉じる
		# cv.destroyAllWindows()
		i += 1
		'''
		if keyboard.is_presssed('escape'):
			messagebox.showinfo('Processing finished!')
			sys.exit()
		'''
		

