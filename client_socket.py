import cv2, pickle, struct,imutils, time, socket

image_path = 'data/samples/img/5.jpg'
video_path = 'data/samples/5.mp4'

img = cv2.imread(image_path)
vc = cv2.VideoCapture(video_path)

# local host IP '127.0.0.1'
host = '127.0.0.1'
# Define the port on which you want to connect
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connect to server on local computer
s.connect((host,port))

while True:
    hasFrame, frame = vc.read()

    # Stop the program if reached end of video
    if hasFrame:
        frame = imutils.resize(frame, width=600)
        result, frame = cv2.imencode('.jpg', frame)
        data = pickle.dumps(frame, 0)
        
        # mandar mensagem para o servidor
        start = time.clock()
        s.sendall(struct.pack('>i', len(data))+data)
        
        # messaga received from server
        data = s.recv(1024)

        # print the received message
        # here it would be a reverse of sent message
        print('Dados recebidos:{} /tempo de resposta={}'.format((time.clock()-start), str(data.decode('ascii'))))

    if cv2.waitKey(1) == 27:
        break
# close the connection
s.close()
