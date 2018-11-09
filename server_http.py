from flask import Flask, request, Response
import numpy as np
import cv2, dlib, jsonpickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/main', methods=['POST'])
def process_image():
    if request:
        r = request
        # convert string of image data to uint8
        nparr = np.frombuffer(r.data, np.uint8)
        # decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)


        # do some fancy processing here....
        detector = dlib.simple_object_detector("data/models/cone_hog.svm")
        h, w, n = img.shape
        dets = detector(img)
        direction = 0
        if dets:
                direction = (w / 2) - dets[0].center().x

        cv2.imshow("Foto", img)


        # build a response dict to send back to client
        response = {'message': 'image received. size={}x{}, direction={}'.format(img.shape[1], img.shape[0], direction)
                    }
        # encode response using jsonpickle
        response_pickled = jsonpickle.encode(response)

        return Response(response=response_pickled, status=200, mimetype="application/json")



# start flask app
app.run(host="0.0.0.0", port=5000)
