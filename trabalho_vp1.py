import socket
import sys
argumentos = sys.argv
requestUrl = argumentos[1]
http_method = argumentos[2]

def get():
    socketTCP = socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketTCP.connect((requestUrl.replace('http://', ''), 80))

    if http_method.upper() == 'POST':
        print("Conectado com sucesso!")

        payload = argumentos[3]
        print(argumentos)
    elif http_method.upper() == 'GET':
        print('Conectado com sucesso!')

        #requisicao = (http_method + ' ' + requestUrl +'/'+ ' / HTTP/1.1 / \r\nHost:'+requestUrl+'\rAccept:text/plain\r\n').encode()
        request=(http_method+" / HTTP/1.1\r\nHost: "+requestUrl+"\r\nAccept: text/plain\r\n\r\n").encode()
        #socketTCP.sendall(requisicao)
        #socketTCP.sendall(
        #b" / HTTP/1.1\r\nHost: uni7.edu.br\r\nAccept: text/plain\r\n\r\n")

        socketTCP.sendall(request)

        resposta_servidor = ''
        while True:
            dados=socketTCP.recv(1)
            resposta_servidor+=dados.decode('UTF-8')
            if dados ==b'':
                break
        print(resposta_servidor)
    socketTCP.close()
    print('Conexão encerrada')

    # def main():

    #     socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     socketTCP.connect(("www.uni7.edu.br", 80))

    #     requisicao = input(
    #         str("Digite qual metodo <GET, POST, DELETE> voce deseja utilizar: ")).upper()
    #     if requisicao == 'GET':

    #         print('Conexão iniciada!')

    #         print('Resposta HTTP:')

    #         socketTCP.sendall(
    #             b"GET / HTTP/1.1\r\nHost: uni7.edu.br\r\nAccept: text/plain\r\n\r\n")

    #         print(str(socketTCP.recv(1024).decode('UTF-8')))
    #         print('Conexão encerrada!')

    #     elif requisicao == 'POST':
    #         print('Conexão iniciada!')

    #         print('Reposta HTTP:')

    #         socketTCP.sendall(
    #             b"POST / HTTP/1.1\r\nHost: uni7.edu.br\r\nAccept: text/plain\n\r um playload qualquer\n\r")

    #         print(str(socketTCP.recv(1024).decode('UTF-8')))
    #         print('Conexão encerrada!')

    #     elif requisicao == 'DELETE':
    #         print('Conexão iniciada!')

    #         print('Reposta HTTP:')

    #         socketTCP.sendall(
    #             b"DELETE / HTTP/1.1\r\nHost: uni7.edu.br\r\nAccept: text/plain\n\r um playload qualquer\n")

    #         print(str(socketTCP.recv(1024).decode('UTF-8')))
    #         print('Conexão encerrada!')

get()
