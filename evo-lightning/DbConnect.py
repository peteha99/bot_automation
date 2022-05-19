import mysql.connector


class Database:
    my_db = cursor = None

    def __init__(self):
        global my_db, cursor
        try:
            my_db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="mysql"
            )
            cursor = my_db.cursor()
            
            # creating database_cursor to perform SQL operation
            db_cursor = my_db.cursor()
            # executing cursor with execute method and pass SQL query
            db_cursor.execute("CREATE DATABASE automation")
            # get list of all databases
            db_cursor.execute("SHOW DATABASES")
            #print all databases
        finally:
            print("intit successfully")
        for db in db_cursor:
            print(db)
        
    def connection(self):
            
        try:
            my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="automation"
            )
            
            mySql_Create_Table_Query = """CREATE TABLE profile (
                                        id int NOT NULL AUTO_INCREMENT,
                                        name varchar(255) NOT NULL,
                                        solution_code int NOT NULL,
                                        balance int,
                                        descrition text,
                                        winrate float,
                                        create_at timestamp,
                                        PRIMARY KEY(id)
                                        ) """

            cursor = my_db.cursor()
            cursor.execute(mySql_Create_Table_Query)
            
            cursor.execute("""CREATE TABLE game_history (
                            id int NOT NULL AUTO_INCREMENT,
                            color varchar(255),
                            stack int,
                            create_at timestamp,
                            PRIMARY KEY(id)
                            )""")
            
            cursor.execute("""
                        CREATE TABLE profile_history (
                        id int NOT NULL AUTO_INCREMENT,
                        profile_id int NOT NULL,
                        game_history_id int NOT NULL,
                        win boolean,
                        create_at timestamp,
                        PRIMARY KEY(id),
                        FOREIGN KEY (profile_id) REFERENCES profile(id),
                        FOREIGN KEY (game_history_id) REFERENCES game_history(id)
                        )""")
            
            print("Laptop Table created successfully ")

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if my_db.is_connected():
                cursor.close()
                my_db.close()
                print("MySQL connection is closed")


class Profile(Database):

    def all_profile(self, mode='DESC'):
        sql = "SELECT * FROM profile ORDER BY id {}".format(mode)

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            
            print("Total number of rows selected : ", cursor.rowcount)

            print("\nSelected data are -")

            for row in result:
                print("Id : ",row[0])
                print("Name : ",row[1])
                print("Solution Code : ",row[2])
                print("balance : ",row[3])
                print("descrition : ",row[4])
                print("winrate : ",row[4])
        except Exception as e:
            return e
        

        return result

    def insert(self, data):

        sql = "INSERT INTO students (name,roll,address) VALUES (%s , %s, %s)"

        try:
            cursor.execute(sql, data)
        except Exception as e:
            return e

        return cursor.lastrowid

    def insert_many(self, data):
        sql = "INSERT INTO students (name,roll,address) VALUES (%s , %s, %s)"

        try:
            cursor.executemany(sql, data)
        except Exception as e:
            return e

    def delete(self, id):
        sql = "DELETE FROM students WHERE id = {}".format(id)

        try:
            cursor.execute(sql)
        except Exception as e:
            return e

    def update(self, id, data):

        # sql = "UPDATE customers SET name = %s,roll = %s,address = %s WHERE id = {}".format(
        #     id)
        sql = "UPDATE students SET name = %s ,roll = %s, address = %s WHERE id = {}".format(
            id)

        val = (data[0], data[1], data[2])

        try:
            cursor.execute(sql, val)

        except Exception as e:
            return e

    def truncate(self):

        sql = "TRUNCATE TABLE students"
        try:
            cursor.execute(sql)
        except Exception as e:
            return e

        return True

# Database().__init__()
Database().connection()