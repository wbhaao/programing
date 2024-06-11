
#관련 라이브러리 선언 
import numpy as np 
import cv2
from matplotlib import pyplot as plt
#트랙바 호출함수 
def nothing(x):
    pass
def check_odd(num): 
    if num % 2 == 0:
        num += 1
    return num
def set_run(pos): 
    global img1
    method = cv2.getTrackbarPos('method', "morphology") 
    itr = cv2.getTrackbarPos('iter', "morphology") 
    ksize = cv2.getTrackbarPos('ksize', "morphology") 
    run = cv2.getTrackbarPos('run', "morphology")
    if run == 1:
        ksize = check_odd (ksize)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize)) 
        if method == 0:
            res = cv2.erode (img1, kernel, iterations=itr)
        else:
            res = cv2.dilate(img1, kernel, iterations=itr) 
        cv2.imshow("morphology", res)


#영상 읽기
img1 = cv2.imread("deep/img9.jpg", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('morphology')
cv2.createTrackbar('method', 'morphology', 0, 1, nothing) 
cv2.createTrackbar('ksize', 'morphology', 3, 10, nothing) 
cv2.createTrackbar("iter", 'morphology', 1, 10, nothing) 
cv2.createTrackbar("run", 'morphology', 0, 1, set_run) 
cv2.setTrackbarPos("method", "morphology", 0)
cv2.setTrackbarPos("ksize", "morphology", 3)
cv2.setTrackbarPos("iter", "morphology", 1)
cv2.setTrackbarPos("run", "morphology", 0)
cv2.imshow("morphology", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()