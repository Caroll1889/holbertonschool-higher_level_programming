#!/usr/bin/python3
# My github

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    u_name = sys.argv[1]
    ps_wd = sys.argv[2]

    g_hub = requests.get('https://api.github.com/user',
                         auth=('u_name', 'ps_wd'))
    try:
        print(g_hub.json()['id'])

    except Exception:
        pass
