import sys
import cv2
import dlib
import pickle
import socket
import struct
import threading
from _thread import *
print_lock = threading.Lock()

# tratar a mensagem recebida


def recv_size(the_socket):
    total_len = 0
    total_data = []
    size = 2 ** (struct.Struct('i').size * 8 - 1) - 1
    size_data = sock_data = b''
    recv_size = 8192
    while total_len < size:
        sock_data = the_socket.recv(recv_size)
        if not total_data:
            if len(sock_data) > 4:
                size_data += sock_data
                size = struct.unpack('>i', size_data[:4])[0]
                recv_size = size
                if recv_size > 524288:
                    recv_size = 524288
                total_data.append(size_data[4:])
            else:
                size_data += sock_data
        else:
            total_data.append(sock_data)
        total_len = sum([len(i) for i in total_data])
    return b"".join(total_data)

# thread


def threaded(c):
    data = b""
    detector = dlib.simple_object_detector("data/models/cone_hog.svm")
    while True:
        # dados recebidos do cliente
        data = recv_size(c)
        if not data:
            print_lock.release()
            break
        frame = pickle.loads(data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.COLOR_BGR2GRAY)

        h, w, n = frame.shape
        dets = detector(frame)
        direction = 0
        if dets:
            direction = dets[0].center().x - (w / 2)

        for det in dets:
            p1 = (det.left(), det.top())
            p2 = (det.right(), det.bottom())
            color = (0, 0, 255)  # Red
            cv2.rectangle(frame, p1, p2, color)
        cv2.imshow('ImageWindow', frame)
        if cv2.waitKey(1) == 27:
            break
        response = 'direcao={}'.format(
            direction)
        # mandar a mensagem para o cliente
        c.send(response.encode())
    # fechar conexao
    c.close()


def distance_to_camera(knownWidth, focalLength, perWidth):
        # compute and return the distance from the maker to the camera
    return (knownWidth * focalLength) / perWidth


# initialize the known distance from the camera to the object, which
# in this case is 24 inches
KNOWN_DISTANCE = 24.0

# initialize the known object width, which in this case, the piece of
# paper is 12 inches wide
KNOWN_WIDTH = 11.0

host = "127.0.0.1"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("socket binded to post", port)
# socket em espera
s.listen(5)
print("socket is listening")
while True:
    # estabilizar conexao
    c, addr = s.accept()
    print_lock.acquire()
    print('Connected to :', addr[0], ':', addr[1])
    # colocar conexao em uma thread
    start_new_thread(threaded, (c,))
s.close()
