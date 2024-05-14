
import numpy as np 
import cv2
from matplotlib import pyplot as plt
#영상 읽기
img1 = cv2.imread("./deep/img9.jpg", cv2.IMREAD_GRAYSCALE)
#샤프닝 수행
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
res1 = cv2.filter2D (img1, -1, kernel)
#언샤프 기법 수행
ksize1 = 3; ksize2 = 15
img1_blur1 = cv2.blur(img1, (ksize1, ksize1))
img1_blur2 = cv2.blur(img1, (ksize2,ksize2))
res2 = cv2.subtract(img1.astype(np. uint16) * 2, img1_blur1.astype(np.uint16)) 
res3 = cv2.subtract(img1.astype(np. uint16) * 2, img1_blur2.astype(np.uint16)) 
res2 = res2.astype (np. uint8); res3 = res3.astype (np.uint8)
dif_img1 = cv2.absdiff(img1, img1_blur1) 
dif_img2 = cv2.absdiff(img1, img1_blur2)
# Display!
ress = []
ress.append(img1), ress.append(res1), ress.append(res2), ress.append(res3),
ress.append(dif_img1), ress.append(dif_img2)
titles = ['input', '3*3 filter', 'unsharp (3*3 blur)', 'unsharp (15*15 blur)', 'absDiff(3*3 blur)', 'absDiff (15*15 blur)']
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(ress[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()