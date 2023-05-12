#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    iterator = len(sys.argv) - 1
    if iterator == 0:
        print("0 arguments.")
    elif iterator == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(iterator))
    for i in range(iterator):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
