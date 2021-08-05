import socket

HEADER = 64
PORT = 5050
SERVER = '127.0.1.1'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
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
