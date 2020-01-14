#!/usr/bin/python3
#

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    x = requests.get(url)
    if x.status_code >= 400:
        print('Error code: {}'.format(x.status_code))
    else:
        print(x.text)
