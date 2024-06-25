import cv2
import numpy as np

#--- pre-setting
click = False
click2 = False
x1, y1 = -1, -1
x2, y2 = -1, -1

def mousePass(event, x, y, flags, param):
    pass

def mouseCallback(event, x, y, flags, param):
    global x1, y1, x2, y2, click, click2, frameCp
    if event == cv2.EVENT_LBUTTONDOWN:
        click = True
        x1, y1 = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if click:
            frameCp = frame.copy()
            cv2.rectangle(frameCp, (x1, y1), (x, y), (255, 0, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        if click:
            click = False
            x2, y2 = x, y
            click2 = True

# camera setting
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# --- main code #1
if not cam.isOpened():
    print('webcam error')
    exit()

cv2.namedWindow("test")
cv2.setMouseCallback("test", mouseCallback)

status, frame = cam.read()
template = frame.copy()

while not click2:
    if click:
        cv2.imshow("test", frameCp)
    else:
        cv2.imshow("test", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.setMouseCallback("test", mousePass)
cv2.namedWindow("template")

# 좌표 값 확인 및 경계 처리
if x1 < 0: x1 = 0
if y1 < 0: y1 = 0
if x2 > frame.shape[1]: x2 = frame.shape[1]
if y2 > frame.shape[0]: y2 = frame.shape[0]

if x1 < x2 and y1 < y2:
    template2 = template[y1:y2, x1:x2]
    cv2.imshow("template", template2)
    cv2.waitKey(10)
else:
    print("잘못된 좌표 값입니다.")
    cam.release()
    cv2.destroyAllWindows()
    exit()

# --- main code #2
w = x2 - x1
h = y2 - y1
method = cv2.TM_CCOEFF_NORMED

while cam.isOpened():
    status, frame = cam.read()
    if not status:
        break
    rows, cols = frame.shape[:2]
    res = cv2.matchTemplate(frame, template2, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    M = np.float32([[1, 0, -max_loc[0] + int(-w / 2 + cols / 2)], [0, 1, -max_loc[1] + int(-h / 2 + rows / 2)]])
    dst = cv2.warpAffine(frame, M, (cols, rows))
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
    if status:
        cv2.imshow("test", dst)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
