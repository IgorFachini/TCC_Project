import cv2, pickle, struct,imutils, time, socket

image_path = 'data/samples/img/5.jpg'
video_path = 'data/samples/5.mp4'
vc = cv2.VideoCapture(video_path)
# local host IP '127.0.0.1'
host = '127.0.0.1'
# Defina a porta na qual você deseja se conectar
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connectar no servidor
s.connect((host,port))

while True:
    hasFrame, frame = vc.read()
    # para o programa caso nao haja mais frames
    if hasFrame:
        frame = imutils.resize(frame, width=600)
        result, frame = cv2.imencode('.jpg', frame)
        data = pickle.dumps(frame, 0)
        # mandar mensagem para o servidor
        start = time.clock()
        s.sendall(struct.pack('>i', len(data))+data)
        # mensagem recebida do servidor
        data = s.recv(1024)
        # monstrar a mensagem recebida
        print('Dados recebidos:{} /tempo de resposta={}'.format(str(data.decode('ascii')), (time.clock()-start) * 10))
    if cv2.waitKey(1) == 27:
        break
# fecha conexao
s.close()
