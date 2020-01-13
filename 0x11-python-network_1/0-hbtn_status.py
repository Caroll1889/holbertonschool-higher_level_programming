#!/usr/bin/python3
#Python script that fetches https://intranet.hbtn.io/status

from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as resp:
        html = resp.read()
        enc = html.decode()
    print('Body response:')
    print('    - type:', (type(html)))
    print('    - content:', html)
    print('    - utf8 content:', enc)
