import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 2 Ie Bee]
img = cv.imread('result.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# Olzls} +aHst7]

ret, thresh1= cv.threshold(img, 20,255, cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,20,255,cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 20,255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img,20,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,20,255,cv.THRESH_TOZERO_INV)

# 284 AS 718s)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

# SAO A] Tl Ses]

images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt. subplot (2,3, i+1),plt.imshow( images[i], 'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
