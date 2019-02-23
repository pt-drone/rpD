import socket

IP = '192.168.100.111'
PORT = 50000
BUFFER_SIZE = 2048
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    data = input('Please input > ')
    s.send(data.encode())
    print(s.recv(BUFFER_SIZE).decode())
    s.close()