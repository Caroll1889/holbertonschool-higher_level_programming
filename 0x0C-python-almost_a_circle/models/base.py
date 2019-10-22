#!/usr/bin/python3
"""model Base"""
import json


class Base:
    """private class attribute """
    __nb_objects = 0

    
    def __init__(self, id=None):
        """constructor"""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_n = cls.__name__ + ".json"
        cont = " "
        new_list = []

        for a in list_objs:
            new_list.append(a.to_dictionary())
        cont = cls.to_json_string(new_list)

        with open(file_n, "w", encoding='utf-8') as file:
            file.write(cont)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            new = cls(1, 0, 0)

        if cls.__name__ == "Rectangle":
            new = cls(1, 1, 0, 0)

        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            return
        else:
            return []
