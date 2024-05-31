import cv2

videoCapture = cv2.VideoCapture('../chapter8/pedestrians.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (
    int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
)
# videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
videoWriter = cv2.VideoWriter('MyOutputVid.mp4', cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), fps, size)

# read the first frame
success, frame = videoCapture.read()
while success:  # Loop until there are no more frames.
    videoWriter.write(frame)
    # read next frame
    success, frame = videoCapture.read()
