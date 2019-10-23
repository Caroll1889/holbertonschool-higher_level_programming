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
        """returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        file_n = cls.__name__ + ".json"
        new_list = []

        with open(file_n, "w", encoding='utf-8') as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                for a in list_objs:
                    new_list.append(a.to_dictionary())
                cont = cls.to_json_string(new_list)
                file.write(cont)

    @staticmethod
    def from_json_string(json_string):
        """return the list of the JSON string representation"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instancewith all attributes"""
        if cls.__name__ == "Square":
            new = cls(1, 0, 0)

        if cls.__name__ == "Rectangle":
            new = cls(1, 1, 0, 0)

        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """return a list of instance"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as file:
                content = file.read()
                data = cls.from_json_string(content)
            lst = []
            for i in data:
                lst.append(cls.create(**i))
            return lst
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the JSON string representation"""
        file_n = cls.__name__ + ".csv"
        new_list = []

        with open(file_n, "w", encoding='utf-8') as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                for a in list_objs:
                    new_list.append(a.to_dictionary())
                cont = cls.to_json_string(new_list)
                file.write(cont)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, encoding="utf-8") as file:
                content = file.read()
                data = cls.from_json_string(content)
            lst = []
            for i in data:
                lst.append(cls.create(**i))
            return lst
        except FileNotFoundError:
            return []
