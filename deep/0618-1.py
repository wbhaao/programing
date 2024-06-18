
#관련 라이브러리 선언 
import numpy as np 
import cv2
from matplotlib import pyplot as plt
#영상 읽기
img1_src = cv2.imread("./deep/img_6_0.png", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1_src, (320,240))
#탬플릿 매칭 및 결과 출력/저장 
template = img1[5:70, 5:70] 
w, h = template.shape[::-1] 
methods = ['cv2.TM_CCOEFF',
'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
'cv2.TM_CCORR_NORMED',
'cv2.TM_SQDIFF',
'cv2.TM_SQDIFF_NORMED']


for meth in methods: 
    input=img1.copy()
    method = eval(meth)
    res = cv2.matchTemplate(img1, template, method) 
    min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h) 
    cv2.rectangle(input, top_left, bottom_right, 0, 2)
    
    plt.figure()
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(input, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([]) 
    plt.suptitle(meth)
plt.show()