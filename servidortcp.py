import socket
import _thread as thread


def processar_nova_conexao(novoSocketDaConexao):
    linha = ""
    while True:
        data = novoSocketDaConexao.recv(1)
        linha += data.decode("UTF-8")
        if data == b"\n":
            print(linha)
            novoSocketDaConexao.send(bytes("resposta: " + linha, "UTF-8"))
            break
    novoSocketDaConexao.close()


def main():
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("criou o socket")

    socketTCP.bind(('', 8080))
    print("vinculou a porta 8080")

    socketTCP.listen()
    print("escutando novas conexoes")

    while True:
        print("aguardando conexão")

        novoSocketDaConexao, cliente = socketTCP.accept()
        print("nova conexao do cliente: ", cliente)

        thread.start_new_thread(processar_nova_conexao, tuple([novoSocketDaConexao]))


main()
