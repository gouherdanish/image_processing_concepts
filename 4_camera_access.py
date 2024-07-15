import cv2
import sys

# Which camera to access: 0 - primary system camera, 1 - added camera 
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

# Video capture object 
source = cv2.VideoCapture(s)

# Window Frame Name
win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# Capture video frames until Esc key is pressed
while cv2.waitKey(1) != 27: # Escape Char
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)

# Release Camera Resources
source.release()
cv2.destroyWindow(win_name)