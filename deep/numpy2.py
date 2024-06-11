# 관련 라이브러리 선언
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 영상 읽기
img1 = cv2.imread("./deep/result.jpg", cv2.IMREAD_GRAYSCALE)

# 이동 변환
h, w = img1.shape # 수정된 부분
trans_x = 10; trans_y = 25 # 오타 수정: tlans_x, tlans_y -> trans_x, trans_y
point1_src = np.float32([[15,20], [50,70], [130,140]])
point1_dst = np.float32(point1_src + [trans_x, trans_y])
affine_mat1 = cv2.getAffineTransform(point1_src, point1_dst)
user_mat1 = np.float32([[1,0,trans_x], [0,1,trans_y]])
res1 = cv2.warpAffine(img1, affine_mat1, (w,h))
res2 = cv2.warpAffine(img1, user_mat1, (w,h))

# 크기변환
scale_x = 0.8; scale_y = 0.6
user_mat2 = np.float32([[scale_x,0,0], [0,scale_y,0]])
res3 = cv2.warpAffine(img1, user_mat2, (w,h))
res4 = cv2.resize(img1, (0,0), fx=scale_x, fy=scale_y)
background = np.full((h,w), fill_value=0, dtype=np.uint8) # 수정된 부분: shape 매개변수 수정
background[:int(h*scale_y), :int(w*scale_x)] = res4 # 수정된 부분: 슬라이싱 방법 수정
res4 = background

# 이동 및 크기 변환
user_mat3 = np.float32([[0.4, 0, 100], [0, 0.6, 501]])
res5 = cv2.warpAffine(img1, user_mat3, (w,h))

# 결과 영상 출력
ress = [img1, res1, res2, res3, res4, res5] # 수정된 부분: append 방식 대신 직접 할당
titles = ['input', 'res1', 'res2', 'res3', 'res4', 'res5']
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(ress[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
