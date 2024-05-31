import cv2

clicked = False


def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv2.VideoCapture("MyOutputVid.mp4")

# created a cv window named MyWindow
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

print('Showing camera feed. Click window or press any key to stop.')
success, frame = cameraCapture.read()
# only update cv2 window when cv2.waitKey is called
# only exit when pressed 27 (Esc Key)
while cv2.waitKey(100) != 27 and not clicked:
    if frame is not None:
        cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
