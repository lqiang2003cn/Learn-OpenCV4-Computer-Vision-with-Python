import cv2
import numpy

ci = cv2.imread("MyPic.jpg")

byteArray = bytearray(ci)

print(byteArray)

bgrImage = numpy.array(byteArray).reshape((500, 411, 3))

cv2.imwrite("frombyte.jpg", bgrImage)