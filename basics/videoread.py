import cv2

cap = cv2.VideoCapture('Resources/carPark.mp4')

while True:
    success, img = cap.read()
    print(success)
    cv2.imshow('CarPark', img)
    cv2.waitKey(1)