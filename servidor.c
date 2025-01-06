#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>

#define PORTANUMERO 2343

int main(int argc, char *argv[])
{
	char buffer[]="Esta eh uma mensagem do servidor!\n";
	int sockettamanho; //recebe o tamanho da estrutura sockaddr_in
	int meusocket; //Descritor do socket de escuta
	int socketconexao; //Descritor do socket da conexao

	struct sockaddr_in endereco_cliente; //informacoes do cliente
	struct sockaddr_in endereco_servidor; //informacoes do servidor

	sockettamanho = sizeof(struct sockaddr_in);

	meusocket = socket(AF_INET,SOCK_STREAM,0);

	endereco_servidor.sin_family = AF_INET;

	endereco_servidor.sin_addr.s_addr = INADDR_ANY; //define qualquer IP da interface de rede

	endereco_servidor.sin_port = htons(PORTANUMERO); //define a porta de escuta da conexao

	memset(&(endereco_servidor.sin_zero),'\0',sizeof(endereco_servidor.sin_zero)); //zera o resto da estrutura

	bind(meusocket,(struct sockaddr *)&endereco_servidor,sizeof(struct sockaddr)); //liga o enderecamento do servidor ao socket

	listen(meusocket,1); //Habilita a escuta de conexoes

	printf("Servidor escutando na porta TCP %d\n",PORTANUMERO);

	while(1)
	{
		socketconexao = accept(meusocket,(struct sockaddr *)&endereco_cliente,&sockettamanho); //espera por uma conexao
		printf("Uma conexao do endereco %s foi estabelecida - enviando boas vindas!\n",inet_ntoa(endereco_cliente.sin_addr));
		send(socketconexao,buffer,strlen(buffer),0);
		close(socketconexao);
	}

	close(meusocket);
	exit(0);
}
