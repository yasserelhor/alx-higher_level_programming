#!/usr/bin/python3
"""this script  takes in a URL, sends a request
   to the URL and displays the body of
   the response (decoded in utf-8)."""
from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
