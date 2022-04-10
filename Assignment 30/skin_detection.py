import cv2
import numpy as np

webcam = cv2.VideoCapture(0)

min = np.array([0, 55, 80], dtype = "uint8")
max = np.array([25, 255, 255], dtype = "uint8")

while True:
    ret, frame = webcam.read()
    if not ret:
        break    

    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    Mask = cv2.inRange(frame_HSV, min, max)
    Mask = cv2.GaussianBlur(Mask, (5, 5), 0)
    frame = cv2.bitwise_and(frame, frame, mask = Mask)

    cv2.imshow("output", frame)

    if cv2.waitKey(1) == 27: #esc
        break
