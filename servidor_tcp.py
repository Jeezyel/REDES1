import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[*] Escutando em {}:{}".format(bind_ip, bind_port))


# Thread para tratamento de clientes
def handle_client(client_socket):
    # Exibe o que cliente enviar
    request = client_socket.recv(1024)
    print("[*] Recebido: {}".format(request.decode('utf-8')))

    # Envia um pacote de volta
    client_socket.send(b"ACK!")

    client_socket.close()


while True:
    client, addr = server.accept()
    print("[*] Conexão recebida de {}:{}".format(addr[0], addr[1]))

    # Coloca nossa thread de cliente em ação para tratar dados de entrada
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

