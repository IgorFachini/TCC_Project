import requests,imutils, json, cv2

addr = 'http://localhost:5000'
test_url = addr + '/main'

image_path = 'data/samples/img/1.jpg'

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
print(response.elapsed.total_seconds())


video_path = 'data/samples/4_Trim.mp4'
vc = cv2.VideoCapture(video_path)

while True:
    hasFrame, frame = vc.read()

    # Stop the program if reached end of video
    if hasFrame:
        frame = imutils.resize(frame, width=600)
        # encode image as jpeg
        _, img_encoded = cv2.imencode('.jpg', frame)
        # send http request with image and receive response
        response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)

        # decode response
        print(json.loads(response.text))
        print(response.elapsed.total_seconds())



