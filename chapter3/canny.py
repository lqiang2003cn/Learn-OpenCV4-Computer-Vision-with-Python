import cv2
import numpy as np

img = cv2.imread("statue_small.jpg", 0)
# Width and Height
cv2.imwrite("canny.jpg", cv2.Canny(img, img.shape[1], img.shape[0]))
cv2.imshow("canny", cv2.imread("canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()
