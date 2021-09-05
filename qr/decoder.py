import cv2 as cv

im = cv.imread('etc/testimg.jpeg')
det = cv.QRCodeDetector(im)

retval, points, straight_qrcode = det.detectAndDecode(im)
