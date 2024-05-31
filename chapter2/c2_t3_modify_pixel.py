import cv2

img = cv2.imread('MyPic.png')
img[0, 0] = [255, 255, 255]
cv2.imwrite('modified_0_0.png', img)

img = cv2.imread('MyPic.png')
img.itemset((0, 1, 0), 255)  # Sets the value of a pixel's blue channel
print(img.item(0, 1, 0))
cv2.imwrite('modified_0_1.png', img)

img = cv2.imread('MyPic.png')
img[:, :, 1] = 0
cv2.imwrite('modified_all_G_to_0.png', img)

img = cv2.imread('MyPic.png')
my_roi = img[0:200, 0:200]
img[200:400, 200:400] = my_roi
cv2.imwrite('modified_roi.png', img)

img = cv2.imread('MyPic.png')
print(img.shape)
print(img.size)  # H*W*C
print(img.dtype)  # bit per channel: different from bit per pixel
