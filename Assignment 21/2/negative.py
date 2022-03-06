import cv2 as cv

img1 = cv.imread('1/1.jpg', 0)
img2 = cv.imread('2/2.jpg', 0)

res1 = 255 - img1[::]
res2 = 255 - img2[::]

cv.imwrite('2/result1.jpg', res1)
cv.imwrite('2/result2.jpg', res2)