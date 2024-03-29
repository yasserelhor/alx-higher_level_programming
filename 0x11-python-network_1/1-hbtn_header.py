#!/usr/bin/python3
"""this script request to the URL and displays
   the value of the X-Request-Id variable found
   in the header of the response."""
import sys
from urllib import request


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as res:
        print(res.info()["X-Request-Id"])
