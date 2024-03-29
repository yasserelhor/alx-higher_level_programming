#!/usr/bin/python3
"""this script takes in a URL and an e_mail, sends
   a POST request to the passed URL with the e_mail a
   a parameter, and displays the body of the response (decoded in utf-8)"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    e_mail = sys.argv[2]
    i3dadat = {"e_mail": e_mail}
    i3dadat_utf = parse.urlencode(i3dadat).encode('utf-8')
    req = request.Request(url, data=i3dadat_utf, method='POST')
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
