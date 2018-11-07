import requests
import json
import cv2

addr = 'http://localhost:5000'
test_url = addr + '/main'

image_path = 'img/1.jpg'
img = cv2.imread(image_path)

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
print(json.loads(response.text))
