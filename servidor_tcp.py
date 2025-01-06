import socket
import threading


# Defina o host e a porta

bind_ip = "0.0.0.0"
bind_port = 9999 # ou o endereço IP do servidor
                 # a porta que o servidor está escutando

# Cria o objeto socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[*] Escutando em {}:{}".format(bind_ip, bind_port))

# Conecta ao servidor

def handle_client(client_socket, addr):
    # Exibe o que cliente enviar
    request = client_socket.recv(1024)
    print("[*] Recebido de {}: {}".format(addr[0] , request.decode('utf-8')))

    # Envia um pacote de volta
    client_socket.send(b"MENSAGEM RECEBIDA")

    client_socket.close()


while True:
    client, addr = server.accept()
    #print("[*] Conexão recebida de {}:{}".format(addr[0], addr[1]))# se comentar esse linha fica mais bonito de se ver o chat

    # Coloca nossa thread de cliente em ação para tratar dados de entrada
    client_handler = threading.Thread(target=handle_client, args=(client, addr))
    client_handler.start()




