import socket


def main():
    requisicao = b"GET /graduacao/sistemas-de-informacao/ HTTP/1.1\nHost: https://www.uni7.edu.br \n\n"

    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socketTCP.connect(("uni7.edu.br", 80))
    
    print("Conexão iniciada!")
    
    socketTCP.sendall(requisicao)

    resultado = socketTCP.recv(10000)

    while (len(resultado) > 0):
        print(resultado)
        resultado = socketTCP.recv(10000)

    socketTCP.close()

    print('Conexão encerrada!')


main()
