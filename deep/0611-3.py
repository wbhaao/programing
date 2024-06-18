
import numpy as np 
import cv2
from matplotlib import pyplot as plt
#영상 읽기
img1_src = cv2.imread("deep/img_6_3.png", cv2.IMREAD_GRAYSCALE) 
img2_src = cv2.imread("deep/img_6_0.png", cv2.IMREAD_GRAYSCALE)

img1 = cv2.resize(img1_src, (320,240))
img2 = cv2.resize(img2_src, (320,240))
#직선 검출 
img1_edge = cv2.Canny(img1, 50, 150, apertureSize=3)
lines = cv2.HoughLines (img1_edge, 2, np.pi/180, 100)
linesP = cv2.HoughLinesP(img1_edge, 2, np.pi/180, 50, minLineLength=1, maxLineGap=100)

#원 검출
circles = cv2.HoughCircles(img2, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=20, minRadius=30, maxRadius=50)
#결과 출력
img1_color1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
if lines.any() != None:
    for line in lines:
        rho, theta = line [0]
        a = np.cos(theta); b=np.sin(theta)
        x0 = a*rho; y0 = b*rho
        x1 = int(x0 + 1000*(-b)); y1 = int(y0 + 1000*a)
        x2 = int(x0 - 1000*(-b)); y2 = int(y0 - 1000*a)
        cv2.line(img1_color1, (x1,y1), (x2,y2), (0,0,255), 2)


img1_color2 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR) 
if linesP.any() != None:
    for line in linesP:
        x1, y1, x2, y2 = line[0]
        cv2.line(img1_color2, (x1,y1), (x2,y2), (0,255,0), 2)
circles = np.uint16 (np.around (circles))
img2_color1 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
if circles.any() != None:
    for i in circles [0, :]:
        cv2.circle(img2_color1, (i[0], i[1]), i[2], (0, 0, 255), 2)
ress = []
ress.append(img1), ress.append(img2), ress.append(img1_edge)
ress.append(img1_color1),
ress.append(img2_color1)
ress.append(img1_color2)
titles = ["img1","img2", "canny edge", "HoughLines", "HoughLinesP", "HoughCircles", "HoughCircles"]
for i in range(6):
    plt.subplot(2,3,1+1)
    plt.imshow(ress[i], cmap='gray')
    plt.title([titles [i]])
    plt.xticks([]), plt.yticks([])
plt.show()