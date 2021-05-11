import socket
import numpy as np

socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
transmissor = ("127.0.0.1", 53595)
receptor = ("127.0.0.1", 12854)
socketUDP.bind(receptor)
buff_size = 10000
next_sequence_number = 0
once_thru = 0

def calculate_checksum(data):
    data_sum = np.uint16(0)
    for element in data:
        data_sum += element
    return np.invert(data_sum)

def udt_send(packet):
    print(packet)
    socketUDP.sendto(packet.tobytes(), transmissor)

def verify_checksum(data):
    data_sum = np.uint16(0)
    for element in data:
        data_sum += element
    return np.invert(data_sum) == 0xFFFF


def rdt_rcv():
    while True:
        message, source = socketUDP.recvfrom(buff_size)
        if source == transmissor:
            return np.frombuffer(message, dtype=np.uint16)    

rcvpkt = rdt_rcv()

def deliver_data(data):
    socketUDP.sendto(data.tobytes(), transmissor)
    vlr=data.tobytes()
    return (bytes(vlr))

def extract(rcvpkt,data):
    is_corrupt = verify_checksum(rcvpkt)
    has_seq=rcvpkt[0]

    if has_seq == 0 and not is_corrupt:
        print(f"Valor da sequencia:{has_seq}")
        print("Extraindo todos os dados...")
        recv_data=""    
        for dados in rcvpkt:
            recv_data+=str(dados)+' '
        print(recv_data)

        is_ack = rcvpkt[2] == True
        is_nack = rcvpkt[2] == False

        sndpkt = np.array([], np.uint16)
        sndpkt = np.append(sndpkt, np.uint16(is_ack))
        sndpkt = np.append(sndpkt, np.uint16(next_sequence_number))
        sndpkt = np.append(sndpkt, np.uint16(0))  # checksum

        sndpkt[2] = calculate_checksum(rcvpkt)
        is_corrupt = verify_checksum(rcvpkt)
        is_ack = rcvpkt[2] == True
        is_nack = rcvpkt[2] == False

        if is_corrupt or has_seq == 0:
            udt_send(sndpkt)
        if not is_corrupt and has_seq == 1:
            extract(rcvpkt,data)
            pass
        print(sndpkt)
if next_sequence_number == 0:
    next_sequence_number = 1
else:
    next_sequence_number = 0
if once_thru == 0:
    once_thru = 1
else:
    once_thru = 0
    
if __name__=='__main__':
    data=deliver_data(rcvpkt)
    extract(rcvpkt,data)
    print(f"Numero da sequencia:{next_sequence_number}")
    print(f"once:{once_thru}")