import cv2
import numpy

img = numpy.zeros((3, 3), dtype=numpy.uint8)
img[0, 0] = 1
img[0, 1] = 2
print(img)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img)

img = numpy.zeros((5, 3), dtype=numpy.uint8)
print(img.shape)


byteArray = bytearray(image)