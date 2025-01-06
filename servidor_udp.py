import socket

HOST = '192.168.15.239'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(1024)
    print(cliente, msg.decode('utf-8'))

udp.close()
