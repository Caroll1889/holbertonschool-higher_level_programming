#!/usr/bin/python3
#

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    x = requests.post(url, data=val)
    print(x.text)
