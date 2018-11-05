"""
This file demos method to detect and visualize an object from:
- An image file
- A live capture stream
"""

import dlib, cv2

detector = dlib.simple_object_detector("custom.svm")

"""
Detect from an image file
"""
image_path = 'DSC01134resized.jpg'
img = cv2.imread(image_path)

dets = detector(img)
for det in dets:
    p1 = (det.left(), det.top())
    p2 = (det.right(), det.bottom())
    color = (0, 0, 255) # Red
    cv2.rectangle(img, p1, p2, color)
    cv2.imshow('Eyeglasses', img)
    cv2.waitKey(0)

# ========================================= #

"""
Detect from a live stream
"""
camera_number = 0
camera = cv2.VideoCapture()
camera.open(camera_number)
if camera.isOpened() is not True:
    print("Could not access camera")
    exit()
else:
    print("Camera ready")

width, height = 320, 240
fps = 60

camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, fps)

while True:
    capture_success, camera_frame = camera.read()

    if capture_success:
        dets = detector(camera_frame)
        if len(dets) == 0:
            a = 1
        else:
            for det in dets:
                p1 = (det.left(), det.top())
                p2 = (det.right(), det.bottom())
                color = (0, 0, 255) # Red
                cv2.rectangle(camera_frame, p1, p2, color)
        cv2.imshow('Eyeglasses', camera_frame)
        key = cv2.waitKey(1000 // fps)
    if key == 27: # Escape key
        break