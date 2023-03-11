import cv2

img = cv2.imread('Resources/lenna.jpg')

cv2.imshow('Lenna', img)
cv2.waitKey(0)