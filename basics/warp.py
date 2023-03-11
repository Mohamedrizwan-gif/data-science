import cv2
import numpy as np

img = cv2.imread('Resources/card.jpg')

width, height = 300, 400

pts1 = np.float32([[797, 111], [1188, 328], [485, 745], [895, 945]])
pts2 = np.float32([[0,0], [width,0], [0, height], [width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
wrapImg = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Card', img)
cv2.imshow('Card Wrap', wrapImg)
cv2.waitKey(0)