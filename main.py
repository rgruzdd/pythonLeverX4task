from Tables import DatabaseHandler
from select_sql_request import MyRequest
from write_file import FileHandler
import sys

bd_handler = DatabaseHandler()
# with connection.cursor() as cursor:
#     index = 'CREATE INDEX stud_ind '\
#             'ON students (id, name, birthday, room, sex) '
#     cursor.execute(index)
#     indexx = cursor.fetchall()
# print(indexx)

# students_data = FileHandler.read(sys.argv[1])
# rooms_data = FileHandler.read(sys.argv[2])
# DatabaseHandler.database_create(rooms_data, students_data)
# MyRequest.all_request(sys.argv[3])

students_data = FileHandler.read(sys.argv[1])
rooms_data = FileHandler.read(sys.argv[2])
bd_handler.database_create(rooms_data, students_data)
MyRequest.all_request(bd_handler.connection, sys.argv[3])










