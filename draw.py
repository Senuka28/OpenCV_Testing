import numpy as np
import cv2 as cv

blank = np.zeros((500, 500), dtype='uint8')
cv.imshow('Blank', blank)



cv.waitKey(0)