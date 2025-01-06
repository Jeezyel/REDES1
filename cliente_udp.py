import socket

HOST = '192.168.15.254'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print('Para sair use CTRL+X\n')

msg = input()

while msg != '\x18':
    udp.sendto(msg.encode('utf-8'), dest)
    msg = input()

udp.close()
