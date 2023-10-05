#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    from sys import argv

    count = len(argv)
    i = 1

    if count == 1:
        print("{} arguments.".format(count - 1))
    elif count == 2:
        print("{} Hello:".format(count-1))
