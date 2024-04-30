
import cv2
import numpy as np
from matplotlib import pyplot as plt
#영상 읽기
img1 = cv2.imread("./deep/img5.jpg", cv2.IMREAD_GRAYSCALE)
if img1 is None:
    print('no file found') 
    exit()

#영상 명암비 조절 변수 선언 및 초기화
multi_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8) 
log_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8) 
invol_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8) 
sel_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8) 

multi_v = 2; gamma1 = 0.1; gamma2= 0.6
thres1  = 5; thres2 = 100

max_v_log = 255 / np.log(1 + 255)
max_v_invol = 255 / np.power(255, gamma1) 
max_v_sel = 100 / np. power (thres2, gamma2)


for i in range(256):
    val = i * multi_v
    if val > 255: val = 255 
    multi_lut[i] = val
    log_lut[i] = np.round(max_v_log * np.log(1+i)) 
    invol_lut[i] = np.round(max_v_invol * np.power(i, gamma1))
    
    if i < thres1 : sel_lut[i] = i
    elif i > thres2 : sel_lut[i] = i
    else: sel_lut[i] = np.round(max_v_sel * np.power(i, gamma2))
#명암비 조절 (LUT 적용)
ress = []
ress.append(img1)
ress.append(cv2.LUT(img1, multi_lut)) 
ress.append(cv2.LUT (img1, log_lut))
ress.append(cv2.LUT(img1, invol_lut)) 
ress.append(cv2.LUT (img1, sel_lut))
#결과 영상 출력
titles = ['입력영상', '상수곱', '로그 변환', '거듭제곱 변환', '구간 변환']
plt.rc('font',family='Pretendard')
for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(ress[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()