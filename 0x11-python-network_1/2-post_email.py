#!/usr/bin/python3
# script that takes in a URL and an email, sends a POST request to the
# passed URL with the email as a parameter, and displays the body
# of the response

from urllib.request import urlopen
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":

    url = sys.argv[1]
    val = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(val)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urlopen(req) as resp:
        html = resp.read()
    print(html.decode())
