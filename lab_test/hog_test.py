
import dlib
import cv2
import imutils

# detector = dlib.simple_object_detector("data/models/detector.svm")

# """
# Detect from an image file
# """
# # Load image file
# cam = cv2.VideoCapture(VIDEO_FILE)
# image = False

# h, w, n = img.shape

# dets = detector(img)
# for det in dets:
#     direction = (w / 2) - det.center().x
#     p1 = (det.left(), det.top())
#     p2 = (det.right(), det.bottom())
#     color = (0, 0, 255)  # Red
#     cv2.rectangle(img, p1, p2, color)
#     cv2.imshow('Eyeglasses', img)
#     cv2.waitKey(0)


# video_path = 'data/samples/20180616_144310_Trim.mp4'
# vc = cv2.VideoCapture(video_path)

# while True:
#     hasFrame, frame = vc.read()

#     # Stop the program if reached end of video
#     if hasFrame:
#         frame = imutils.resize(frame, width=600)
#         # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         dets = detector(frame)
#         for det in dets:
#             p1 = (det.left(), det.top())
#             p2 = (det.right(), det.bottom())
#             color = (0, 0, 255)  # Red
#             cv2.rectangle(frame, p1, p2, color)

#         h, w, n = img.shape
#         direction = 0
#         if dets:
#                 direction = (w / 2) - dets[0].center().x
#         print(direction)
#         cv2.imshow("Foto", frame)


#     if cv2.waitKey(1) == 27:
#         break


# Imagem
IMAGE_FILE = 'data/samples/img/1.jpg' 
# Video
VIDEO_FILE = 'data/samples/4_Trim.mp4'
# Arquivo cascade
DETECTOR_FILE = 'data/models/detector.svm'
# carregar o arquivo cascade
detector = dlib.simple_object_detector(DETECTOR_FILE)
# Nome do item
ITEM = 'cone'
# Carregar leitor
cam = cv2.VideoCapture(VIDEO_FILE)
image = False

while True:
    # ler imagem
    ret, imageRead = cam.read()
    if ret != False:
        # redimensionar imagem
        image = imutils.resize(imageRead, width=600)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # procurar o objeto 
        dets = detector(image)

        # circular cada objeto encontrado na imagem com retangulo
        for (i, det) in enumerate(dets):
            p1 = (det.left(), det.top())
            p2 = (det.right(), det.bottom())
            color = (0, 0, 255)  # Red
            cv2.rectangle(image, p1, p2, color)
            cv2.putText(image, ITEM + " #{}".format(i + 1), (det.center().x, det.center().y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    
    # Mostrar resultado
    cv2.imshow(ITEM + "s", image)
    if cv2.waitKey(1) == 27:
        break
