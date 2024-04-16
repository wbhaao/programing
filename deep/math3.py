
import numpy as np 
import cv2
from matplotlib import pyplot as plt

img1= cv2.imread('./deep/img1.jpg') 
img2 = cv2.imread('./deep/img2.jpg') 
img3 = cv2.imread('./deep/img3.jpg') 
img4 = cv2.imread('./deep/img4.jpg') 
img5 = cv2.imread('./deep/img5.jpg')
print(img5.shape)
#마스크 선언 및 초기화
mask = np.full(shape=img5. shape, fill_value=0, dtype=np. uint8) 
h, w, c=img5.shape
x = (int)(w/2) - 60; y = (int) (h/2) - 60
cv2.rectangle(mask, (x,y), (x+120, y+120), (255,255,255), -1)
#산술 및 논리 연산 수행
ress = []
ress.append(cv2.add(img1, img2))
ress.append(cv2.addWeighted (img1, 0.5, img2, 0.5, 0))
ress.append(cv2.subtract (img3, img4))
ress.append(cv2.absdiff(img3, img4))
ress.append(cv2.bitwise_not(img5))
ress.append(cv2.bitwise_and (img5, mask))


titles = []
titles.append('input1')
titles.append('input2')
titles.append('input3')
titles.append('input4')
titles.append('input5')
titles.append('mask')

titles.append('add')
titles.append('addWeighted')
titles.append('subtract')
titles.append('absdiff')
titles.append('bitwise_not') 
titles.append('bitwise_and')
images = [img1, img2, img3, img4, img5, mask, ress[0], ress[1], ress [2], ress [3], ress[4], ress [5]]
for i in range(12):
    plt.subplot(2,6,i+1), plt.imshow(images[i]) 
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()