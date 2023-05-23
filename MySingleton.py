import pymysql
import json
from config import host, user, password, db_name


class DatabaseHandler():
    @staticmethod
    def database_create(text_rooms, text_students):
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

            try:
                with connection.cursor() as cursor:
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

                        with connection.cursor() as cursor:
                            for i in text_rooms:
                                insert_query = "INSERT INTO rooms (id, name) " \
                                               "VALUES ('%d', '%s');" \
                                               % (i['id'], i['name'])
                                cursor.execute(insert_query)
                                connection.cursor()
                                connection.commit()

                with connection.cursor() as cursor:
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
                        with connection.cursor() as cursor:
                            for i in text_students:
                                insert_query = "INSERT INTO students (id, name, birthday, room, sex) " \
                                               "VALUES ('%d', '%s', '%s', '%d', '%s');" \
                                               % (i['id'], i['name'], i['birthday'], i['room'], i['sex'])
                                cursor.execute(insert_query)
                                connection.cursor()
                                connection.commit()
            except:
                connection.close()

        except Exception as exx:
            print("Connection refused")
            print(exx)





