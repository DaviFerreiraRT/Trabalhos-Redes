import socket


def main():
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    url = 'uni7.edu.br', 80
    getRequest = b'GET /https://www.uni7.edu.br HTTP/1.0\r\n\r\n'
    socketTCP.connect((url))

    socketTCP.send(getRequest)

    linha = ""
    print("Conexao estabelecida com sucesso!")
    while True:
        data = socketTCP.recv(1)
        linha += data.decode("UTF-8")
        if data == b"\n":
            print(linha)
            break

    socketTCP.close()


main()
