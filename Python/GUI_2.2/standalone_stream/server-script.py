import io
import socket
import struct
import cv2
import numpy as np

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

# Inserted accept function into the loop so it may always listen for any
# data transmitted while not crashing if client closes transmission
# https://stackoverflow.com/questions/18767147/server-crashes-when-the-client-is-closing

# Server side is based on
# https://stackoverflow.com/questions/46624449/load-bytesio-image-with-opencv
# https://stackoverflow.com/questions/48611517/raspberry-pi-3-python-and-opencv-face-recognition-from-network-camera-stream
try:
    while True:
        connection = server_socket.accept()[0].makefile('rb')
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        while True:
            image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
            if not image_len:
                break
            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))
            image_stream.seek(0)
            file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            cv2.imshow("Image", img)
            cv2.waitKey(1)

finally:
    connection.close()
    server_socket.close()

