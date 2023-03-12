import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:
            cv2.drawContours(imgContours, cnt, -1, (255,0,255), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCor == 4:
                objType = 'Rectangle'
                aspRatio = float(w)/h
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objType = 'Square'
            elif objCor == 3:
                objType = 'Triangle'
            elif objCor == 5:
                objType = 'Pentagon'
            elif objCor == 6:
                objType = 'Hexagon'
            elif objCor == 10:
                objType = 'Star'
            else:
                objType = 'Circle'
                aspRatio = float(w)/h
                if aspRatio > 1.25 and aspRatio < 1.50:
                    objType = 'Oval'
            cv2.rectangle(imgContours, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(imgContours, objType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,255), 2)

img = cv2.imread('Resources/shapes.jpg')
imgContours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
imgCanny = cv2.Canny(imgBlur, 100, 100)
getContours(imgCanny)

cv2.imshow('Canny', imgContours)
cv2.waitKey(0)