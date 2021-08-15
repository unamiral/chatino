import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 8888))
s.listen(1)
x = 1
conn, client = s.accept()
print(client, "connected")
while True:
    data = input(f"[{x}]:")
    conn.send(data.encode())
    print(conn.recv(1024).decode())
    x += 1

