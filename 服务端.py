import socket

phone = socket.socket()
phone.bind(('127.0.0.1',8080))
phone.listen(5)

print("有消息送达...")
while 1:
    try:
        conn, addr = phone.accept()  # 当没有消息时，处于阻塞状态
        client_data = conn.recv(1024)
        print(client_data.decode('utf-8'))
        conn.send(client_data+b'sb')
        conn.close()
    except ConnectionAbortedError:
        break
