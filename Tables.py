import pymysql
import json
from config import host, user, password, db_name


class DatabaseHandler():
    def __init__(self):
        self.connection = DatabaseHandler.create_connection()

    @staticmethod
    def create_connection():
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected")
        except Exception as exx:
            print("Connection refused")
            print(exx)
        return connection

    def database_create(self, text_rooms, text_students):
            try:
                with self.connection.cursor() as cursor:
                    stmt = "SHOW TABLES LIKE 'rooms'"
                    cursor.execute(stmt)
                    result = cursor.fetchone()
                    if result:
                        print("Table rooms was already created")
                    else:
                        creat_table_query = "CREATE TABLE rooms(id INT," \
                                            "name varchar(32), PRIMARY KEY (id));"
                        cursor.execute(creat_table_query)
                        print("Table rooms created successfully")

                        with self.connection.cursor() as cursor:
                            for i in text_rooms:
                                insert_query = "INSERT INTO rooms (id, name) " \
                                               "VALUES ('%d', '%s');" \
                                               % (i['id'], i['name'])
                                cursor.execute(insert_query)
                                self.connection.cursor()
                                self.connection.commit()

                with self.connection.cursor() as cursor:
                    stmt = "SHOW TABLES LIKE 'students'"
                    cursor.execute(stmt)
                    result = cursor.fetchone()
                    if result:
                        print("Table students was already created")
                    else:
                        creat_table_query = "CREATE TABLE students(id INT," \
                                        "name varchar(32)," \
                                        "birthday DATETIME," \
                                        "room INT," \
                                        "sex varchar(5), PRIMARY KEY (id)," \
                                        "FOREIGN KEY (room) REFERENCES rooms(id));"
                        cursor.execute(creat_table_query)
                        print("Table students created successfully")
                        with self.connection.cursor() as cursor:
                            for i in text_students:
                                insert_query = "INSERT INTO students (id, name, birthday, room, sex) " \
                                               "VALUES ('%d', '%s', '%s', '%d', '%s');" \
                                               % (i['id'], i['name'], i['birthday'], i['room'], i['sex'])
                                cursor.execute(insert_query)
                                self.connection.cursor()
                                self.connection.commit()
            except:
                self.connection.close()
            try:
                with self.connection.cursor() as cursor:
                    index = 'CREATE INDEX stud_ind ' \
                        'ON students (id, name, birthday, room, sex) '
                cursor.execute(index)
                indexx = cursor.fetchall()
                print('Index was created')

            except:
                 print('Index is already existed')






