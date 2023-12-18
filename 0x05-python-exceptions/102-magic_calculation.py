#!/usr/bin/python3
def magic_calculation(a, b):
    fin = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            fin += a ** b / i
        except Exception:
            fin = b + a
            break

    return fin
