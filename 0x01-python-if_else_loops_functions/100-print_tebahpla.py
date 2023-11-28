#!/usr/bin/python3
output = ""

for i in reversed(range(97, 123)):
    output += chr(i) if i % 2 == 0 else chr(i - 32)
print(output, end='')
