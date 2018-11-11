# import socket programming library
import sys
import cv2
import dlib
import pickle
import socket
import struct  # new

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()


def recv_size(the_socket):
    # data length is packed into 4 bytes
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

# thread fuction


def threaded(c):
    data = b""
    detector = dlib.simple_object_detector("data/models/cone_hog.svm")

    while True:

        # data received from client
        # data = c.recv(1024)
        data = recv_size(c)
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break

        frame = pickle.loads(data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # do some fancy processing here....
        h, w, n = frame.shape
        dets = detector(frame)
        direction = 0
        if dets:
            direction = (w / 2) - dets[0].center().x

        for det in dets:
            p1 = (det.left(), det.top())
            p2 = (det.right(), det.bottom())
            color = (0, 0, 255)  # Red
            cv2.rectangle(frame, p1, p2, color)

        cv2.imshow('ImageWindow', frame)
        if cv2.waitKey(1) == 27:
            break

        response = 'image received. size={}x{}, direction={}'.format(
            frame.shape[1], frame.shape[0], direction)

        # send back reversed string to client
        c.send(response.encode())

    # connection closed
    c.close()


def Main():
    host = "192.168.1.104"

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()
