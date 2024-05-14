
import numpy as np 
import cv2
from matplotlib import pyplot as plt
#영상 읽기
img1= cv2.imread("./deep/img8.jpg", cv2.IMREAD_GRAYSCALE)
#필터 정의 및 블러링 수행
ksize1 = 3; ksize2 = 5; ksize3 = 7; ksize4 = 9
res1 = cv2.GaussianBlur(img1, (ksize1, ksize1), 0)
res2 = cv2.GaussianBlur(img1, (ksize2, ksize2), 0)
res3 = cv2.GaussianBlur(img1, (1,21), 0)
ress = []
ress.append(img1), ress.append(res1)
ress.append(res2), ress.append(res3)
titles = ['input', '7x1', '9x9', '1x21']
for i in range(4):
    plt.subplot(2,3,i+1)
    plt.imshow(ress[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()