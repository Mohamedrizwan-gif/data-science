import cv2
import numpy as np
from stackimages import stackImages

img = cv2.imread('Resources/card.jpg')
imgResize = cv2.resize(img, (400, 300))
imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)

# hor = np.hstack([imgGray, imgResize])
# ver = np.vstack([imgResize, imgGray])
st = stackImages(0.5, ([imgResize, imgResize, imgGray]))

cv2.imshow('Horizontal img', st)
# cv2.imshow('Vertical img', ver)
cv2.waitKey(0)