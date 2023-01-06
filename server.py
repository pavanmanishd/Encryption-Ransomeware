import socket

server_ip_address = '192.168.101.120'
server_port = 5678

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((server_ip_address,server_port))
    print("Server Listening ...")
    s.listen(1)
    conn,addr = s.accept()
    print(f'Connection established from : {addr}')
    with conn:
        while True:
            data = conn.recv(1024)
            break
    print(data)