#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    one = sorted(dir(hidden_4))
    for i in one:
        if i[0] != '_':
            print(i)
