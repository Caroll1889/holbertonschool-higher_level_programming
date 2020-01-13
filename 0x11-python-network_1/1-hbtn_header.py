#!/usr/bin/python3
# script that takes in a URL, sends a request to the URL
# and displays the value of the X-Request-Id

from urllib.request import urlopen
import sys

if __name__ == "__main__":

    with urlopen(sys.argv[1]) as resp:
        html = resp.read()
    info = resp.info()
    print(info['X-Request-Id'])
