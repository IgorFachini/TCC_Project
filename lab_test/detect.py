
import dlib
import cv2
import imutils

# tipo do detector
typeDetector = 'hog'

# Imagem
IMAGE_FILE = 'data/samples/img/5.jpg' 
# Video
VIDEO_FILE = 'data/samples/4_Trim.mp4'
# Arquivo cascade
detector = ''
# carregar o arquivo detector
if typeDetector == 'hog':
    detector = dlib.simple_object_detector('data/models/cone_hog.svm')
else:
    detector = cv2.CascadeClassifier('data/models/cascade.xml')
# Nome do item
ITEM = 'cone'
color = (0, 0, 255)  # Red

# Carregar leitor
cam = cv2.VideoCapture(IMAGE_FILE)
image = False

while True:
    # ler imagem
    ret, imageRead = cam.read()
    if ret != False:
        # redimensionar imagem
        image = imutils.resize(imageRead, width=600)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # procurar o objeto 
        # circular cada objeto encontrado na imagem com retangulo
        if typeDetector == 'hog':
            dets = detector(image)

            for (i, det) in enumerate(dets):
                p1 = (det.left(), det.top())
                p2 = (det.right(), det.bottom())
                cv2.rectangle(image, p1, p2, color)
                cv2.putText(image, ITEM + " #{}".format(i + 1), (det.center().x, det.center().y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
        else:
            # procurar o objeto 
            rectangles = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,
            minSize=(55, 55))

            # circular cada objeto encontrado na imagem com retangulo
            for (i, (x, y, w, h)) in enumerate(rectangles):
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(image, ITEM + " #{}".format(i + 1), (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    
    # Mostrar resultado
    cv2.imshow(ITEM + "s", image)
    if cv2.waitKey(1) == 27:
        break
