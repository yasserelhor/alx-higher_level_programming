#!/usr/bin/python3
"""This takes 2 arguments in order to solve this challenge."""
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    req = requests.get(url)
    com = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(com[i].get("sha"),
                  com[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
