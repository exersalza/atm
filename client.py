import time
import bcrypt

from server.client_conn import send, client
from server.sql.sql_conn import mydb


# todo:
#

## CURSOR / VAR ##

cursor = mydb.cursor(buffered=True)

f = True

## LOGIN PREPARE ## how does the computer scientist duck? NAT NAT NAT :)
mod = input('What do you want to do?: login/register ').lower()


def form():
    global usr_name, psw
    usr_name = input("Username: ")
    psw = input('Password: ')


def register(username, password):
    global psw, usr_name, f
    # print(cursor.execute(f"SELECT * FROM login_db WHERE username='{username}'"))

    if cursor.execute(f"SELECT * FROM main_db WHERE username='{username}'"):
        print('cocks')
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hashed_password = str(hashed_password).strip("b '")
        cursor.execute(f"INSERT INTO main_db (username, password) VALUES ('{str(username)}', '{hashed_password}')")
        f = False

        msg = client.recv(1024)
        print(msg.decode("utf-8"))

        return mydb.commit()


def login(username, password):
    global usr_name, psw, f
    cursor.execute(f"SELECT * FROM main_db WHERE username='{username}'")
    data = cursor.fetchone()
    check_psw = str.encode(password)
    if bcrypt.checkpw(check_psw, data[2].encode('utf-8')):
        send('login_redirect')

        msg = client.recv(1024)
        print(msg.decode("utf-8"))

        f = False
    else:
        print('Password or Username are incorrect!')
        usr_name = input("Username: ")
        psw = input('Password: ')

    send('!l')


## LOGIN / REGISTER ##

try:
    while f:
        if mod == 'login':
            usr_name = input("Username: ")
            psw = input('Password: ')

            login(usr_name, psw)
        elif mod == 'register':
            usr_name = input("Username: ")
            psw = input('Password: ')

            register(usr_name, psw)
        else:
            print('Enter a Valid value: login or register')
            send('!l')
            f = False

except Exception:
    send('!l')
    raise Exception

# send(username, password)

# time.sleep(0.5)
# send('!l')
