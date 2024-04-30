
import numpy as np 
import cv2
from matplotlib import pyplot as plt
#영상 읽기
img1= cv2.imread("./deep/img8.jpg", cv2.IMREAD_GRAYSCALE)
#필터 정의 및 블러링 수행
ksize1 = 3; ksize2 = 5; ksize3 = 7; ksize4 = 9
kernel = np.full(shape=[ksize4, ksize4], fill_value=1, dtype=np.float32) / (ksize4*ksize4) 
res1 = cv2.blur(img1, (ksize1, ksize1))
res2 = cv2.blur(img1, (ksize2, ksize2))
res3 = cv2.boxFilter(img1, -1, (ksize3, ksize3)) 
res4= cv2.filter2D (img1, -1, kernel)
res5 = cv2.boxFilter(img1, -1, (1,21))
ress = []
ress.append(img1), ress.append(res1), ress.append(res2) 
ress.append(res3), ress.append(res4), ress.append(res5)
titles = ['input', 'res1', 'res2', 'res3', 'res4', 'res5']
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(ress[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()