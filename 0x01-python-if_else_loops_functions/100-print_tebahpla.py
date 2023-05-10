#!/usr/bin/python3
iterator = 0
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - iterator)), end="")
    iterator = 32 if iterator == 0 else 0
