import socket

target_host = "192.168.0.110"
target_port = 9999

# Cria um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o cliente se conectar
client.connect((target_host, target_port))

# Envia alguns dados
client.send(b"VASCO DA GAMA")

# Recebe alguns dados
response = client.recv(4096)

print(response.decode('utf-8'))