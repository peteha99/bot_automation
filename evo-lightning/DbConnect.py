
import mysql.connector


class Database:
    my_db = cursor = None

    def __init__(self):
        try:
            global my_db, cursor
            my_db_init = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )
            cursor_init = my_db_init.cursor()
            
            # creating database_cursor to perform SQL operation
            # executing cursor with execute method and pass SQL query
            cursor_init.execute("CREATE DATABASE IF NOT EXISTS automation")
            # get list of all databases
            cursor_init.execute("SHOW DATABASES")
            #print all databases
            
            my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="automation"
            )
            cursor = my_db.cursor()
            mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS profile (
                                        id int NOT NULL AUTO_INCREMENT,
                                        name varchar(255) NOT NULL,
                                        solution_code int NOT NULL,
                                        balance int,
                                        descrition text,
                                        winrate float,
                                        create_at timestamp,
                                        PRIMARY KEY(id)
                                        ) """
            
            cursor.execute(mySql_Create_Table_Query)
            
            cursor.execute("""CREATE TABLE IF NOT EXISTS game_history (
                            id int NOT NULL AUTO_INCREMENT,
                            color varchar(255),
                            stack int,
                            create_at timestamp,
                            PRIMARY KEY(id)
                            )""")
            
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS profile_history (
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
                
        

class Profile(Database):

    def all_profile(self, mode='ASC'):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="automation"
            )
        cursor = my_db.cursor()
        sql = "SELECT * FROM profile ORDER BY id {}".format(mode)

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            
            # print("Total number of rows selected : ", cursor.rowcount)

            # print("\nSelected data are -")

            for row in result:
                # print("Id : ",row[0])
                # print("Name : ",row[1])
                print("Solution Code : ",row[2])
                print("balance : ",row[3])
                # print("descrition : ",row[4])
                # print("winrate : ",row[4])
        except Exception as e:
            return e
        
        if(my_db.is_connected()):
            cursor.close()
            my_db.close()
            
        return result
    
    def profile_history_insert(self,data):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="automation"
            )
        insert_history = """INSERT INTO automation.profile_history
                            (profile_id, game_history_id, win, create_at)
                            VALUES(%s, %s, %s, %s);
                            """
        cursor = my_db.cursor()
        try:
            cursor.executemany(insert_history, data)
        except Exception as e:
            return e
        my_db.commit()
        print("Data inserted successfully.")
        response = cursor.lastrowid
        if(my_db.is_connected()):
            cursor.close()
            my_db.close()
            
        return response
    
    def update_profile(self, balance,id):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="automation"
            )
        cursor = my_db.cursor()
        data = (balance,id)
        sql = """UPDATE profile SET balance=%s WHERE id = %s"""

        
        try:
            cursor.execute(sql, data)
            my_db.commit()
            result = cursor.fetchall()
            
        except Exception as e:
            return e
        if(my_db.is_connected()):
            cursor.close()
            my_db.close()
            
        
        return result

class Game(Database):
    def save_game_history(self,data):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="automation"
            )
        insert_history = """INSERT INTO automation.game_history
                            (color, stack, create_at)
                            VALUES(%s, %s, %s);
                            """
        cursor = my_db.cursor()
        try:
            cursor.executemany(insert_history, data)
        except Exception as e:
            return e
        my_db.commit()
        print("Data inserted successfully.")
        response = cursor.lastrowid
        if(my_db.is_connected()):
            cursor.close()
            my_db.close()
            
        return response