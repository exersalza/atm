import mysql.connector

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        database='jfklöds'
    )
except Exception as error:
    err = str(error)
    if '1049' in err:
        db_to_create = mysql.connector.connect(
            host='localhost',
            user='root'
        )

        table_to_create = [
            """
            CREATE TABLE `main_db` (
                `ID` INT(11) NOT NULL AUTO_INCREMENT,
                `username` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
                `password` VARCHAR(256) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
                PRIMARY KEY (`ID`) USING BTREE
            )
            COMMENT='Main_DB for the project ATM by exersalza'
            COLLATE='utf8mb4_general_ci'
            ENGINE=InnoDB
            AUTO_INCREMENT=2
            """,

            """
            
            """
        ]

        cur = db_to_create.cursor()
        cur.execute('CREATE DATABASE atm')
