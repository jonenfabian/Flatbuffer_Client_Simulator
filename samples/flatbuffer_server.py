import socket

HOST = ''
PORT = 8089
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(int(1024*4))
    print(data)
