import cv2, time

#1. Create an object. Zero for external camera
video=cv2.VideoCapture(0)

#3. Create a frame object
check, frame = video.read()

print(check)
print(frame)

#4. Show the frame
cv2.imshow("IP Webcam",frame)

#5. Press any key to exit
cv2.waitKey(0)

#2. Shut down the camera.
video.release()