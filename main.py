import time

from server.client_conn import send
from server.sql.sql_conn import mydb

## CURSOR ##
cursor = mydb.cursor()

## LOGIN ##
firstName = input('First Name: ')
name = input('Last Name: ')
password = input('Password: ')

send(firstName)
send(name)
send(password)

time.sleep(0.5)
send('!l')

