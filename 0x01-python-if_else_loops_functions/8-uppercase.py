#!/usr/bin/python3
def uppercase(str):
    x = 0
    for char in str:
        if (ord(char) >= 0 and ord(char) <= 9) or (ord(char) >= 65 and ord(char) <= 90):
            char = char;
        elif ord(char) >= 97 and ord(char) <= 122:
            char -= 32
        if x != len(str):
            print('{:c}'.format(char), end="")
        else:
            print('{:c}'.format(char))
        x++
