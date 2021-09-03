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


class Server:
    def __init__(self, server=''):
        self.SERVER_NAME = server
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())
        # print(SERVER)
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = '!l'

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

    def login(self, name, fname, psw):

        pass

    def handle_client(self, conn, addr):
        print(f'\u001b[32m[NEW CONNECTION] {addr} connected.\n\u001b[0m')

        connected = True
        data = []
        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)

                if msg == self.DISCONNECT_MESSAGE:
                    print(f'\u001b[31m[DISCONNECT]\u001b[0m User: {addr} Disconnected!')
                    connected = False
                    data.clear()
                else:
                    data.append(msg)

                print(f'[{addr}] {msg}, {data}')
                conn.send('Msg received'.encode(self.FORMAT))

    def start(self):
        print('\u001b[33m[STARTING] server is starting...\u001b[0m')
        self.server.listen()
        print(f'\u001b[32m[LISTENING]\u001b[0m Server is listening to {self.SERVER}')
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f'\u001b[34m[ACTIVE CONNECTIONS]\u001b[0m {threading.activeCount() - 1}')


Server.start()