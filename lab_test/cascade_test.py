# Import OpenCV
import cv2
import imutils  # recognition function easy


# Image file
IMAGE_FILE = 'achar/DSC00760resized.jpg'  # Change this to be your image

# Cascade file
CASCADE_FILE = 'xml/cascade10.xml'

# Cascade item name
CASCADE_ITEM = 'cone'

# Load image file
image = cv2.imread(IMAGE_FILE)
image = imutils.resize(image, width=600)
# cam = cv2.VideoCapture(IMAGE_FILE)

while True:
    # Convert the image to gray
    # ret, image = cam.read()
    # if ret == False:
    #     break

    image = imutils.resize(image, width=600)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rectangles = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5,
    minSize=(70, 70))

    for (i, (x, y, w, h)) in enumerate(rectangles):
        # Surround cascade with rectangle
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, CASCADE_ITEM + " #{}".format(i + 1), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    # Display the cascade to the user
    cv2.imshow(CASCADE_ITEM + "s", image)
    if cv2.waitKey(1) == 27:
        break
