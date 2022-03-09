import cv2 as cv

img = cv.imread("joker.jpg" ,0)

negative = 255 - img
blur = cv.GaussianBlur(negative, (21,21), 0)

sketch = img / (255 - blur)
sketch = sketch * 255

cv.imwrite('Painting_joker.jpg' , sketch)