
import dlib, cv2

detector = dlib.simple_object_detector("custom.svm")

"""
Detect from an image file
"""
image_path = 'DSC01134resized.jpg'
img = cv2.imread(image_path)
h, w, n = img.shape

dets = detector(img)
for det in dets:
    direction = (w / 2) - det.center().x
    p1 = (det.left(), det.top())
    p2 = (det.right(), det.bottom())
    color = (0, 0, 255) # Red
    cv2.rectangle(img, p1, p2, color)
    cv2.imshow('Eyeglasses', img)
    cv2.waitKey(0)