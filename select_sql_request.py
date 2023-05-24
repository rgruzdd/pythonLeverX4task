import pymysql
from config import host, user, password, db_name
from write_file import FileHandler
from Tables import DatabaseHandler


class MyRequest():

    @staticmethod
    def list_rooms(connection, file_format):
        with connection.cursor() as cursor:
            list_rooms = 'SELECT room, count(*) ' \
                         'AS students_count  ' \
                         'FROM my_bd.students group by room'
            cursor.execute(list_rooms)
            result = cursor.fetchall()
            if file_format == 'xml':
                FileHandler.write_xml(result, 1)
            elif file_format == 'json':
                FileHandler.write_json(result, 1)

    @staticmethod
    def top_5_min_age_students(connection, file_format):
        with connection.cursor() as cursor:
            top_5_min_age_students = 'SELECT room, year(NOW()) - ' \
                                     'AVG(year(birthday)) AS avg_date ' \
                                     'FROM my_bd.students GROUP ' \
                                     'BY room ORDER BY avg_date LIMIT 5'
            cursor.execute(top_5_min_age_students)
            min_age = cursor.fetchall()
            for i in min_age:
                i['avg_date'] = str(i['avg_date'])
            if file_format == 'xml':
                FileHandler.write_xml(min_age, 2)
            elif file_format == 'json':
                FileHandler.write_json(min_age, 2)

    @staticmethod
    def top_5_big_difference_students(connection, file_format):
        with connection.cursor() as cursor:
            top_5_big_difference_students = 'SELECT room, MAX(year(birthday)) - ' \
                                            'MIN(year(birthday)) ' \
                                            'AS differense from students ' \
                                            'GROUP BY room ORDER BY differense DESC limit 5 '
            cursor.execute(top_5_big_difference_students)
            difference_age = cursor.fetchall()
            for i in difference_age:
                i['differense'] = str(i['differense'])
            if file_format == 'xml':
                FileHandler.write_xml(difference_age, 3)
            elif file_format == 'json':
                FileHandler.write_json(difference_age, 3)

    @staticmethod
    def difference_sex(connection, file_format):
        with connection.cursor() as cursor:
            difference_sex = 'SELECT s.room, r.name from students as s join rooms as r ' \
                             'on s.room = r.id GROUP BY s.room having ' \
                             'count(distinct s.sex) > 1 '
            cursor.execute(difference_sex)
            sex_M_F = cursor.fetchall()
            if file_format == 'xml':
                FileHandler.write_xml(sex_M_F, 4)
            elif file_format == 'json':
                FileHandler.write_json(sex_M_F, 4)

    @staticmethod
    def all_request(connection, file_format):
        MyRequest.list_rooms(connection, file_format)
        MyRequest.top_5_min_age_students(connection, file_format)
        MyRequest.top_5_big_difference_students(connection, file_format)
        MyRequest.difference_sex(connection, file_format)






