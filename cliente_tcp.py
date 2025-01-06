import socket
import subprocess as sub


target_host = "172.16.90.181"
target_port = 9999
comando = ["python3 cliente_tcp.py"]



# Cria um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o cliente se conectar
try:
    client.connect((target_host, target_port))
    print(f"Conectado ao servidor {target_host}:{target_port}")
except ConnectionRefusedError:
    print("Conexão recusada. Verifique se o servidor está ativo.")
    exit()


variavelControle = True

while(variavelControle):

    # Entrada de mensagem do usuário
    mensagem = input("Digite a mensagem para enviar ao servidor: ")

    # Envia a mensagem digitada pelo cliente
    client.send(mensagem.encode('utf-8'))

    # Recebe a resposta do servidor
    response = client.recv(4096)

    # Exibe a resposta
    print("Resposta do servidor:", response.decode('utf-8'))

    print("Deseja enviar mais uma mensagem?\n 1: sim \n ctrl + C: não")

    opcao = input()  # Lê a opção do usuário
      
    sub.run(comando , shell=True , capture_output=False , text=True)
        
    

# Fecha a conexão
client.close()
