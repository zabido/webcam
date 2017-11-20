import urllib
import cv2
import numpy as np

url="http://192.168.0.122:4747/cam/1/frame.jpg"

while True:
	imgRes=urllib.urlopen(url)
	imgNp=np.array(bytearray(imgRes.read()),dtype=np.uint8)
	img=cv2.imdecode(imgNp,-1)
	cv2.imshow("IP Webcam",img)
	cv2.waitKey(10)