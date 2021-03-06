import socket

socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket UDP criado")

socketUDP.sendto(b"mensagem do processo 1", ("10.0.0.106", 3546))
print("Mensagem UDP enviada")

mensagem, remetente = socketUDP.recvfrom(5000)
print(mensagem)
