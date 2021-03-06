import socket


def main():
    requisicao = b'GET /graduacao/ HTTP/1.1\nHost: http://www.uni7.edu.br \n\n'

    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socketTCP.connect((b"uni7.edu.br", 80))


    socketTCP.sendall(requisicao)

    resultado = socketTCP.recv(1024)

    while (len(resultado) > 0):
        print("Conexão iniciada!")
        print(resultado)
        resultado = socketTCP.recv(1024)

    socketTCP.close()

    print('Conexão encerrada!')


main()
