import os.path
import mysql.connector

if os.path.isfile('config.py'):
    from config import HOST, USER, PASSWORD, DB # kann man das so machen? ka funktioniert also alles gut! :)
else:
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = ''
    DB = 'atm'

try:
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB
    )
except Exception as error:
    err = str(error)
    if '1049' in err:
        db_to_create = mysql.connector.connect(
            host='localhost',
            user='root'
        )

        cur = db_to_create.cursor()
        cur.execute('CREATE DATABASE atm')

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            database='atm'
        )

        cur = mydb.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS `main_db` (
                `ID` INT(11) NOT NULL AUTO_INCREMENT,
                `username` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
                `password` VARCHAR(256) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
                PRIMARY KEY (`ID`) USING BTREE
            )
            COMMENT='Main_DB for the project ATM by exersalza'
            COLLATE='utf8mb4_general_ci'
            ENGINE=InnoDB
            AUTO_INCREMENT=2
            """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS `second_db` (
                `ID` INT(11) NOT NULL AUTO_INCREMENT,
                `Name` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
                `FirstName` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
                `CreateDay` DATE NOT NULL,
                `IBAN` BIGINT(20) NOT NULL DEFAULT '0',
                `Bank` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
                `Currency` TINYTEXT NOT NULL COLLATE 'utf8mb4_general_ci',
                `Value` INT(11) NOT NULL,
                PRIMARY KEY (`ID`) USING BTREE
            )
            COMMENT='Information DB'
            COLLATE='utf8mb4_general_ci'
            ENGINE=InnoDB
            """)
    else:
        raise Exception


