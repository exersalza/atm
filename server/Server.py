import socket
import threading
import os
import platform

from sql.sql_conn import mydb

## CURSOR ##
cursor = mydb.cursor()

platform = platform.system()

if platform == 'Windows':
    clear = lambda: os.system('cls')
    clear()
elif platform == 'Linux':
    clear = lambda: os.system('clear')
    clear()

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!l'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def login(name, fname, psw):
    
    pass


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.\n')

    connected = True
    data = []
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
                data.clear()
            else:
                data.append(msg)

            print(f'[{addr}] {msg}, {data}')
            conn.send('Msg received'.encode(FORMAT))


def start():
    server.listen()
    print(f'[LISTENING] Server is listening to {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')


print('[STARTING] server is starting...')
start()
