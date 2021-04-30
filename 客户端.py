import socket

phone = socket.socket()
phone.connect(('127.0.0.1',8080))
while 1:
    client_data = "好垃圾啊"
    phone.send(client_data.encode('utf-8'))
    from_server_data = phone.recv(1024)
    print(from_server_data.decode('utf-8'))

phone.close()
