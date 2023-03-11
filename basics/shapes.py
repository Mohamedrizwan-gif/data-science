import cv2
import numpy as np

img = np.ones((512, 512, 3), np.uint8)
print(img.shape)

img[:] = 255,0,255
cv2.rectangle(img, (100, 100), (300, 400), (255,0,0), 3)
cv2.line(img, (100, 100), (300, 400), (255,0,0), 2)
cv2.circle(img, (150, 150), 40, (255,190,255), cv2.FILLED)
cv2.putText(img, "Hello", (20, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 140, 0), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)
