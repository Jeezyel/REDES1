#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>

#define MAXIMOMSG 500

int main(int argc, char *argv[])
{
	char buffer[MAXIMOMSG+1]; //+1 para incluir o terminador nulo
	int tamanho, meusocket;

	struct sockaddr_in destinatario;

	meusocket = socket(AF_INET,SOCK_STREAM,0);

	destinatario.sin_family = AF_INET;

	destinatario.sin_addr.s_addr = inet_addr("127.0.0.1"); //IP do servidor

	destinatario.sin_port = htons(2343); //porta de conexao do servidor

	memset(&(destinatario.sin_zero),'\0',sizeof(destinatario.sin_zero)); //zerar o resto da estrutura

	connect(meusocket,(struct sockaddr *)&destinatario,sizeof(struct sockaddr));

	tamanho = recv(meusocket,buffer,MAXIMOMSG,0);

	buffer[tamanho] = '\0'; //Termina a mensagem

	printf("Mensagem recebida: %s\n",buffer);
	close(meusocket);
	exit(0);
}
