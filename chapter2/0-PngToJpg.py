import cv2


gi = cv2.imread("MyPicGray.png")
ci = cv2.imread("MyPic.jpg")
# image is in BGR format, not RGB
image = cv2.imread('MyPic.png')
cv2.imwrite('MyPic.jpg', image)
