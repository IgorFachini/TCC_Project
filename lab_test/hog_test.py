
import dlib
import cv2
import imutils

detector = dlib.simple_object_detector("data/models/detector.svm")

"""
Detect from an image file
"""
image_path = 'data/samples/img/10.jpg'
img = cv2.imread(image_path)
h, w, n = img.shape

dets = detector(img)
for det in dets:
    direction = (w / 2) - det.center().x
    p1 = (det.left(), det.top())
    p2 = (det.right(), det.bottom())
    color = (0, 0, 255)  # Red
    cv2.rectangle(img, p1, p2, color)
    cv2.imshow('Eyeglasses', img)
    cv2.waitKey(0)


video_path = 'data/samples/20180616_144310_Trim.mp4'
vc = cv2.VideoCapture(video_path)

while True:
    hasFrame, frame = vc.read()

    # Stop the program if reached end of video
    if hasFrame:
        frame = imutils.resize(frame, width=600)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        dets = detector(frame)
        for det in dets:
            p1 = (det.left(), det.top())
            p2 = (det.right(), det.bottom())
            color = (0, 0, 255)  # Red
            cv2.rectangle(frame, p1, p2, color)

        h, w, n = img.shape
        direction = 0
        if dets:
                direction = (w / 2) - dets[0].center().x
        print(direction)
        cv2.imshow("Foto", frame)


    if cv2.waitKey(1) == 27:

        break
