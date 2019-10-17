#!/usr/bin/python3
""" """
import sys
import json


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    lista = load_from_json_file('add_item.json')
except:
    lista = list()

for i in range(1, len(sys.argv)):
    lista.append(sys.argv[i])
save_to_json_file('add_item.json', lista)
