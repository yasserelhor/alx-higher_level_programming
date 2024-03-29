#!/usr/bin/python3
"""this script takes your GitHub credentials (user and password)
   and uses the GitHub API to display your id"""
import sys
import requests

if __name__ == "__main__":
    paswd = sys.argv[2]
    user = sys.argv[1]
    headers = {'Authorization': f'Bearer {paswd}'}
    res = requests.get("https://api.github.com/user", headers=headers)
    if (res.status_code >= 400):
        print("None")
    else:
        print(res.json()["id"])
