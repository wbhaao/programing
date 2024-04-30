import cv2
import numpy as np

# 웹캠으로부터 영상 캡처 시작
cap = cv2.VideoCapture(0)

# 배경 이미지 저장 변수 초기화
background = None

while True:
    # 영상 프레임을 읽기
    ret, frame = cap.read()
    if not ret:
        break
    
    # 프레임을 회색조로 변환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 키보드 입력 처리
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('a'):
        # 'a'를 눌렀을 때 현재 프레임을 배경으로 설정
        background = gray_frame
    elif key == ord('b') and background is not None:
        # 'b'를 눌렀을 때 배경과 현재 프레임의 차이 계산
        frame_delta = cv2.absdiff(background, gray_frame)
        
        # 차이 이미지를 이진화
        _, thresh = cv2.threshold(frame_delta, 60, 255, cv2.THRESH_BINARY)
        
        cv2.imshow("Threshold", thresh)
    elif key == ord('q'):
        # 'q'를 눌러 프로그램 종료
        break
    
    # 원본 프레임 표시
    cv2.imshow("Frame", frame)
    
# 자원 해제 및 모든 창 닫기
cap.release()
cv2.destroyAllWindows()
