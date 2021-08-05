import time
import bcrypt

from server.client_conn import send
from server.sql.sql_conn import mydb


# todo:
#   login knallen

## CURSOR / VAR ##

cursor = mydb.cursor(buffered=True)

form = True

## LOGIN PREPARE ## how does the computer scientist duck? NAT NAT NAT :)
mod = input('What do you want to do?: login/register ')


def form():
    global usr_name, psw
    usr_name = input("Username: ")
    psw = input('Password: ')


def register(username, password):
    global psw, usr_name, form
    # print(cursor.execute(f"SELECT * FROM login_db WHERE username='{username}'"))

    if cursor.execute(f"SELECT * FROM login_db WHERE username='{username}'"):
        print('cocks')
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hashed_password = str(hashed_password).strip("b '")
        cursor.execute(f"INSERT INTO login_db (username, password) VALUES ('{str(username)}', '{hashed_password}')")
        form = False
        return mydb.commit()


def login(username, password):
    global usr_name, psw
    cursor.execute(f"SELECT * FROM login_db WHERE username={username}")
    data = cursor.fetchone()
    check_psw = str.encode(password)
    if bcrypt.checkpw(check_psw, data[2].encode('utf-8')):
        print('redirect to interface')
    else:
        print('Password or Username are incorrect!')
        usr_name = input("Username: ")
        psw = input('Password: ')

    send('!l')


## LOGIN / REGISTER ##

try:
    while form:
        usr_name = input("Username: ")
        psw = input('Password: ')

        if mod == 'login':
            login(usr_name, psw)
        elif mod == 'register':
            register(usr_name, psw)


except Exception:
    send('!l')
    raise Exception

# send(username, password)

# time.sleep(0.5)
# send('!l')
