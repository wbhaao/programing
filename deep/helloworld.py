import cv2
import numpy as np

# 트랙바가 조정될 때마다 호출될 콜백 함수
def onChange(trackbarValue):
    pass

# 웹캠 설정
cap = cv2.VideoCapture(0)

# 트랙바 생성을 위한 초기 윈도우
cv2.namedWindow("Webcam with Filter")
# 트랙바 생성, 'Filter Size'는 트랙바의 이름, 1은 최소값, 20은 최대값, onChange는 콜백 함수
cv2.createTrackbar("Filter Size", "Webcam with Filter", 1, 20, onChange)

while True:
    # 웹캠으로부터 영상을 읽어옴
    ret, frame = cap.read()
    if not ret:
        break

    # 트랙바의 현재 위치(값)을 읽음
    filterSize = cv2.getTrackbarPos("Filter Size", "Webcam with Filter")

    # 필터 크기가 0이 되지 않도록 조정 (최소 1)
    if filterSize == 0:
        filterSize = 1

    # 필터 적용 (가우시안 블러 사용, 샤프닝 필터 적용 시 다른 함수 사용)
    # 필터 크기는 홀수여야 하므로 (filterSize * 2 + 1)로 설정
    frame_filtered = cv2.GaussianBlur(frame, (filterSize * 2 + 1, filterSize * 2 + 1), 0)
    
    # 필터링된 영상을 화면에 표시
    cv2.imshow("Webcam with Filter", frame_filtered)

    # 'q'를 누르면 반복문 탈출
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
