
import numpy as np 
import cv2
from matplotlib import pyplot as plt
#영상 읽기
img1 = cv2.imread("./../images/img13.jpg",
#모폴로지 연산 수행
cv2.IMREAD_GRAYSCALE)
methods = [cv2.MORPH_OPEN,cv2.MORPH_CLOSE,cv2.MORPH_GRADIENT,cv2.MORPH_TOPHAT,cv2.MORPH_BLACKHAT,cv2.MORPH_HITMISS]


ress = []
for method in methods:
    res = cv2.morphologyEx (img1, method, cv2.UMat(), iterations=1)
    ress.append(res)
for i in range(6):
    cv2.imshow("Test", ress[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()