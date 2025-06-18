import cv2 as cv

img = cv.imread('Photos/senuka.jpg')

def rescaleFrame(img, scaleVal=1.5):
    width = int(img.shape[1] * scaleVal)
    height = int(img.shape[0] * scaleVal)
    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
    

img = rescaleFrame(img)

cv.imshow('Senuka', img)

cv.waitKey(0)