import numpy as np
import cv2 as cv

letter = np.zeros(480000).reshape(800,600)
letter[::] = 255

letter[310:335, 245:345] = 0
letter[435:460, 245:345] = 0

letter[335:435, 220:245] = 0
letter[335:435, 345:370] = 0

letter[460:560, 220:245] = 0
letter[460:560, 345:370] = 0

cv.imwrite('7\letter(A).jpg', letter)