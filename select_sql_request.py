import pymysql
from config import host, user, password, db_name
from write_file import FileHandler


class MyRequest():
    @staticmethod
    def get_connection():
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            connection.close()
        return connection

    @staticmethod
    def request_1(file_format):
        connection = MyRequest.get_connection()
        with connection.cursor() as cursor:
            request_1 = 'SELECT room, count(*) ' \
                        'AS students_count  ' \
                        'FROM my_bd.students group by room'
            cursor.execute(request_1)
            result = cursor.fetchall()
            if file_format == 'xml':
                FileHandler.write_xml(result, 1)
            elif file_format == 'json':
                FileHandler.write_json(result, 1)

    @staticmethod
    def request_2(file_format):
        connection = MyRequest.get_connection()
        with connection.cursor() as cursor:
            request_2 = 'SELECT room, year(NOW()) - ' \
                        'AVG(year(birthday)) AS avg_date ' \
                        'FROM my_bd.students GROUP ' \
                        'BY room ORDER BY avg_date LIMIT 5'
            cursor.execute(request_2)
            new_age = cursor.fetchall()
            if file_format == 'xml':
                FileHandler.write_xml(new_age, 2)
            elif file_format == 'json':
                FileHandler.write_json(new_age, 2)

    @staticmethod
    def request_3(file_format):
        connection = MyRequest.get_connection()
        with connection.cursor() as cursor:
            request_3 = 'SELECT room, MAX(year(birthday)) - ' \
                        'MIN(year(birthday)) ' \
                        'AS differense from students ' \
                        'GROUP BY room ORDER BY differense DESC limit 5 '
            cursor.execute(request_3)
            big_age = cursor.fetchall()
            if file_format == 'xml':
                FileHandler.write_xml(big_age, 3)
            elif file_format == 'json':
                FileHandler.write_json(big_age, 3)

    @staticmethod
    def request_4(file_format):
        connection = MyRequest.get_connection()
        with connection.cursor() as cursor:
            request_4 = 'SELECT s.room, r.name from students as s join rooms as r ' \
                        'on s.room = r.id GROUP BY s.room having ' \
                        'count(distinct s.sex) > 1 '
            cursor.execute(request_4)
            sex_M_F = cursor.fetchall()
            if file_format == 'xml':
                FileHandler.write_xml(sex_M_F, 4)
            elif file_format == 'json':
                FileHandler.write_json(sex_M_F, 4)

    def all_request(file_format):
        MyRequest.request_1(file_format)
        MyRequest.request_2(file_format)
        MyRequest.request_3(file_format)
        MyRequest.request_4(file_format)






