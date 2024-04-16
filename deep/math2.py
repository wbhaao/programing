
import cv2 as cv
from time import sleep
from matplotlib import pyplot as plt
img1 = cv.imread('./deep/img3.jpg') 
img2 = cv.imread('./deep/img4.jpg')
# cv.subtract( src1, src2[, dst[, mask[, 
img3 = cv.subtract(img1, img2)
# cv.absdiff( src1, src2[, dst] ) ->
img4 = cv.absdiff(img1, img2)
titles = ['src', 'map', 'sub', 'absDiff']
imgs = [img1, img2, img3, img4]
for i in range(4):
    plt.subplot(2,2,i+1) 
    plt.imshow(imgs[i]) 
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
sleep(100)