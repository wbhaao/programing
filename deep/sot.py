import cv2
import numpy as np

img = cv2.imread('./deep/img27.jpg')

pts_src = []

def mouse_callback(event, x, y, a, m):
    global pts_src
    if event == cv2.EVENT_LBUTTONDOWN:
        pts_src.append((x, y))
        print(f"Point {len(pts_src)}: ({x}, {y})")
        
        if len(pts_src) == 4:
            cv2.destroyWindow('image')

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)
cv2.imshow('image', img)
cv2.waitKey(0)

pts_dst = np.array([[0, img.shape[0]], [0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]]], dtype=np.float32)
M = cv2.getPerspectiveTransform(np.array(pts_src, dtype=np.float32), pts_dst)

warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))

cv2.imshow('Warped Image', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()