# Import socket module
import socket
import cv2, pickle, struct,imutils, time

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]

image_path = 'data/samples/img/1.jpg'
video_path = 'data/samples/4_Trim.mp4'


img = cv2.imread(image_path)
vc = cv2.VideoCapture(0)

def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'

    # Define the port on which you want to connect
    port = 12345

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host,port))

    # message you send to server
    message = "shaurya says geeksforgeeks"
    while True:
        hasFrame, frame = vc.read()

        # Stop the program if reached end of video
        if hasFrame:
            frame = imutils.resize(frame, width=600)
            result, frame = cv2.imencode('.jpg', frame)
            data = pickle.dumps(frame, 0)
            size = len(data)
            
            # sending = struct.pack(">L", size)
            # s.sendall(data)
            start = time.clock()
            s.sendall(struct.pack('>i', len(data))+data)

            # message sent to server
            # s.send(message.encode('ascii'))

            # messaga received from server
            data = s.recv(1024)

            # print the received message
            # here it would be a reverse of sent message
            print('Received from the server : time={}'.format(time.clock()-start),str(data.decode('ascii')))

        # ask the client whether he wants to continue
        # ans = input('\nDo you want to continue(y/n) :')
        # if ans == 'y':
        #     continue
        # else:
        #     break
        if cv2.waitKey(1) == 27:
            break
    # close the connection
    s.close()

if __name__ == '__main__':
    Main()