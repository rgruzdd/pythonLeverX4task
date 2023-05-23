import sys
import xml.etree.ElementTree as ET
import json
import sys


class FileHandler():
    @staticmethod
    def read(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)

        except FileNotFoundError:
            print('FileNotFoundError')
            sys.exit()

    @staticmethod
    def write_xml(data, request_number):
        if request_number == 1:
            sub_element = 'students_count'
        elif request_number == 2:
            sub_element = 'avg_date'
        elif request_number == 3:
            sub_element = 'differense'
        elif request_number == 4:
            sub_element = 'name'
        p = ET.Element('rooms')
        for room in data:
            room_node = ET.SubElement(p, 'room' + str(room['room']))
            id_node = ET.SubElement(room_node, 'room_id')
            id_node.text = str(room['room'])
            sub_node = ET.SubElement(room_node, sub_element)
            sub_node.text = str(room[sub_element])
        tree = ET.ElementTree(p)
        file_name = 'request' + str(request_number) + '.xml'
        tree.write(file_name)
        print('Files xml created successfully')

    @staticmethod
    def write_json(data, request_number):
        file_name = 'request' + str(request_number) + '.json'
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)
        print('Files json created successfully')