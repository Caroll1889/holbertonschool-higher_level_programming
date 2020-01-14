#!/usr/bin/python3
# Search API

import requests
import sys

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    response = requests.post(url, data={'q': q})
    try:
        json_response = response.json()
        if len(json_response) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(json_response.get('id'),
                  json_response.get('name')))
    except ValueError:
        print('Not a valid JSON')
