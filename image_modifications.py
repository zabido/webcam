import urllib
import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

url="https://nl207.extcam.com/preview/live?access_token=100-U_censored_e05a6&ts=1514972095.58&server=100-C2P0fU4vbGX45sCq9O0vw6&q=0&camera=0&u=100001395990&token=8d5d6c4a77c4c438df4b8009b7229d88"

# url="http://192.168.0.221:4747/cam/1/frame.jpg"

# list all possible flags in cv2
# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print flags

# load image from url and convert it from binary to readable image format
imgRes=urllib.urlopen(url)
imgNp=np.array(bytearray(imgRes.read()),dtype=np.uint8)
img=cv2.imdecode(imgNp,-1)

# convert image to gray scale
imgGray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#show image in a window
# cv2.imshow("IP Webcam",imgGray)

ret,thresh1 = cv2.threshold(imgGray,12,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(imgGray,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(imgGray,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(imgGray,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(imgGray,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [imgGray, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# cv2.waitKey(0)