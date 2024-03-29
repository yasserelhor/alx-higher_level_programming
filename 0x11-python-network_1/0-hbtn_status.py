#!/usr/bin/python3
"""this script fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as res:
        data = res.read()
        par_data = data.decode('utf-8')
        r_type = type(data)
        print(f"Body response:\n\t- type: {r_type}\n\t\
              - content: {data}\n\t- utf8 content: {par_data}")
