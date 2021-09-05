import socket

from server.etc.config import PORT, FORMAT, S_HOST, HEADER

ADDR = (S_HOST, int(PORT))
DISCONNECT_MESSAGE = '!l'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
