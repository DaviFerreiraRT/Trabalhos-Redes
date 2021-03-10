import socket
import sys
# args = sys.argv
# request = args[1]
# http_request = args[2]


# def get():
#     socketTCP = socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     socketTCP.connect((request.replace('http://', ''), 80))
#     print('conectado')

#     if http_request == 'POST':
#         requisicao = (http_request + '' + request+'/'+'HTTP/1.0\n\n').encode()
#         socketTCP.sendall(requisicao)
#         while True:
#             resultado = socketTCP.recv(1024)
#             print(resultado.decode('UTF-8'))
#     else:
#         requisicao = (http_request + '' + request+'/'+'HTTP/1.0\n\n').encode()
#         socketTCP.sendall(requisicao)

#         resposta_servidor = ''
#         while True:
#             resultado = socketTCP.recv(1)
#             resposta_servidor += resultado.decode('utf-8')
#             if resultado == ''.encode():
#                 break
#         print(resposta_servidor)

#     socketTCP.close()

def main():

    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketTCP.connect(("www.uni7.edu.br", 80))

    requisicao = input(str("Digite qual metodo <GET, POST, DELETE> vc deseja utilizar: ")).upper()
    while True:
        if requisicao == 'GET':

            print('Conexão iniciada!')

            print('Reposta HTTP:')

            socketTCP.sendall(
                b"GET / HTTP/1.1\r\nHost: uni7.edu.br\r\nAccept: text/plain\r\n\r\n")

            print(str(socketTCP.recv(1024).decode('UTF-8')))
            print('Conexão encerrada!')
            break


        elif requisicao == 'POST':
            print('Conexão iniciada!')

            print('Reposta HTTP:')

            socketTCP.sendall(
                b"POST / HTTP/1.1\r\nHost: uni7.edu.br\r\nAccept: text/plain\n\r um playload qualquer\n\r")

            print(str(socketTCP.recv(1024).decode('UTF-8')))
            print('Conexão encerrada!')
            break
        elif requisicao == 'DELETE':
            print('Conexão iniciada!')

            print('Reposta HTTP:')

            socketTCP.sendall(
                b"DELETE / HTTP/1.1\r\nHost: uni7.edu.br\r\nAccept: text/plain\n\r um playload qualquer\n")

            print(str(socketTCP.recv(1024).decode('UTF-8')))
            print('Conexão encerrada!')
            break

# get()
main()
