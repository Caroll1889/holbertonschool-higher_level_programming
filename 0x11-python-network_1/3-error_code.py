#!/usr/bin/python3
#


from urllib.request import urlopen
import sys

if __name__ == "__main__":

    try:
        with urlopen(sys.argv[1]) as resp:
            html = resp.read()
        print(html.decode())
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
        
