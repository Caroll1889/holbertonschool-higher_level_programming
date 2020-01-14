#!/usr/bin/python3
#

import requests
import sys

if __name__ == "__main__":

    resp = requests.get(sys.argv[1])
    info = resp.headers
    print(info.get('X-Request-Id'))
