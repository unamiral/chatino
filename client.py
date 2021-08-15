import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8888))
x = 1
while True:
    data = input(f"[{x}]:")
    print(s.recv(1024).decode())
    s.send(data.encode())

    x += 1
s.close()