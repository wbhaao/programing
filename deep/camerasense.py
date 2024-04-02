import numpy as np
import cv2 as cv
import glob

nCols = 9
nRows = 6

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((nCols*nRows, 3), np.float32)
objp[:, :2] = np.mgrid[0:nCols, 0:nRows].T.reshape(-1, 2)

objpoints = []
imgpoints = []
images = glob.glob('deep\*.jpg')
gray = None
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (nCols,nRows), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (nCols,nRows), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(0) # 수정된 부분
cv.destroyAllWindows()

# Calibration #
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Undistortion #

img = cv.imread(images[0])

h, w = img.shape[:2]

newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

# cv.undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite('result.jpg', dst)
