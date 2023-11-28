#!/usr/bin/python3
for i in range(100):
    print(f"{', ' if i > 0 else ''}{i:02}", end='')
print("")
