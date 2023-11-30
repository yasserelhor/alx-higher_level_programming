#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count = 0

    for i in sys.argv:
        count += 1
    if count > 1:
        print("{} arguments:".format(count-1))
    else:
        print("{} arguments.".format(count-1))
    
    count1 = 1
    for a in sys.argv:
        if a != sys.argv[0]:
            print("{}: {}".format(count1, a))
            count1 += 1

