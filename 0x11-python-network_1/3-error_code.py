#!/usr/bin/python3
# print a status error


from urllib.request import urlopen
import sys

if __name__ == "__main__":

    try:
        with urlopen(sys.argv[1]) as resp:
            html = resp.read()
        print(html.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
