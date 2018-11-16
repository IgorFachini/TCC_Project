# Import OpenCV
import cv2
import imutils  # recognition function easy

# Imagem
IMAGE_FILE = 'data/samples/img/1.jpg' 
# Video
VIDEO_FILE = 'data/samples/4_Trim.mp4'
# Arquivo cascade
DETECTOR_FILE = 'data/models/cascade.xml'
# carregar o arquivo cascade
detector = cv2.CascadeClassifier(DETECTOR_FILE)
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
        rectangles = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10,
        minSize=(70, 70))

        # circular cada objeto encontrado na imagem com retangulo
        for (i, (x, y, w, h)) in enumerate(rectangles):
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(image, ITEM + " #{}".format(i + 1), (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    
    # Mostrar resultado
    cv2.imshow(ITEM + "s", image)
    if cv2.waitKey(1) == 27:
        break
