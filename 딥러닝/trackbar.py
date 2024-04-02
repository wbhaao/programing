import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("RGB track bar")

# 트랙바 생성
cv2.createTrackbar('red color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('green color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('blue color', 'RGB track bar', 0, 255, nothing)

# 트랙바 초기 위치 설정
cv2.setTrackbarPos('red color', 'RGB track bar', 125)
cv2.setTrackbarPos('green color', 'RGB track bar', 125)
cv2.setTrackbarPos('blue color', 'RGB track bar', 125)

img = np.zeros((512, 512, 3), np.uint8)

while True:
    # 트랙바의 현재 위치를 가져옴
    redVal = cv2.getTrackbarPos('red color', 'RGB track bar')
    greenVal = cv2.getTrackbarPos('green color', 'RGB track bar')
    blueVal = cv2.getTrackbarPos('blue color', 'RGB track bar')
    
    # 이미지에 색상 적용
    cv2.rectangle(img, (0,0), (512, 512), (blueVal, greenVal, redVal), -1)
    
    # 이미지와 트랙바 창을 보여줌
    cv2.imshow('RGB track bar', img)
    
    # 'ESC' 키를 누르면 반복문을 종료하고 창을 닫음
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
