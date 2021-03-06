import socket

def main():
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketTCP.connect(('www.uni7.edu.br',80))
    get='GET www.uni7.edu.br HTTP/1.0\r\n\r\n'.encode()
    
    socketTCP.send(get)
    print("Conexão estabelecida com sucesso!")
    
    linha = ""
    while True:
        data = socketTCP.recv(1)
        linha += data.decode("UTF-8")
        if data == b"\n":
            print(linha) 
            break

    socketTCP.close()

main()
