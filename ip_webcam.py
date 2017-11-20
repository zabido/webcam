import urllib
import cv2
import numpy as np

# This url is to work on ZabiMon nw
url="http://192.168.0.221:4747/cam/1/frame.jpg"

# Url to work on EWA/Int nw
#url="http://10.149.157.216:4747/cam/1/frame.jpg"

# url="http://zabido25.pagekite.me/cam/1/frame.jpg"

imgRes=urllib.urlopen(url)
imgNp=np.array(bytearray(imgRes.read()),dtype=np.uint8)
img=cv2.imdecode(imgNp,-1)
cv2.imshow("IP Webcam",img)
cv2.waitKey(0)