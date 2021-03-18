import socket
import sys

def main():
    
    try:
        argumentos = sys.argv
        requestUrl = argumentos[1]
        http_method = argumentos[2]

        socketTCP = socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socketTCP.connect((requestUrl, 80))

        if http_method.upper() == 'GET':
            print('Conectado com sucesso!')

            request = (http_method+" / HTTP/1.1\r\nHost: "+requestUrl +
                    "\r\nAccept: text/plain\r\n\r\n").encode()

            socketTCP.sendall(request)
            resposta_servidor = ''
            while True:
                dados = socketTCP.recv(1)
                resposta_servidor += dados.decode('UTF-8')
                if dados == b'':
                    break
            print('Metodo http utilizado: '+http_method)
            print(resposta_servidor)
            socketTCP.close()
            print('Conexão encerrada')

        elif http_method.upper() == 'POST':
            print('Conexão iniciada com sucesso!')

            payload = "username=trabalhoVP1&pass=umpayloadqualquer\n\n"
            header = ("""
                POST /index.php / HTTP/1.1
                Host: uni7.edu.br
                Accept: text/plain / 
                """+payload+"""
                """)
            contentLength = "Content-Length: " + str(len(payload)) + "\n\n"
            request = header.encode() + contentLength.encode() + payload.encode()
            socketTCP.sendall(request)
            response = socketTCP.recv(4096)
            print(response.decode('UTF-8') + '\n')
            socketTCP.close()
            print('Conexão encerrada')

        elif http_method.upper() == 'DELETE':
            print('Conectado com sucesso!')

            request = (http_method+" / HTTP/1.1\r\nHost: "+requestUrl +
                    "\r\nAccept: text/plain\r\n\r\n").encode()

            socketTCP.sendall(request)
            resposta_servidor = ''
            while True:
                dados = socketTCP.recv(1)
                resposta_servidor += dados.decode('UTF-8')
                if dados == b'':
                    break
            print('Metodo http utilizado: '+http_method)
            print(resposta_servidor)
            socketTCP.close()
            print('Conexão encerrada')
    except:
        print("Você deve enviar dois argumentos\nEx: www.un7.edu.br <GET | DELETE | POST>!")
main()