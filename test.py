import cv2
import numpy as np

cap = cv2.imread("S__14.jpg")
gray=cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)        #แปลงภาพสีให้เป็นเกรย์สเกล
cv2.imshow("Show",gray)
cv2.waitKey(0)

cv2.imwrite("grayy.jpg",gray)
cv2.destroyAllWindows()