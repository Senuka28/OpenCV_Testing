import cv2 as cv

''' Reading Videos
img = cv.imread('Photos/Senuka.jpg') # returns image as matrix of pixels

cv.imshow('Cat', img) # displays image

cv.waitKey(0)
'''

# Reading vids
capture = cv.VideoCapture('Videos/perfect.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)