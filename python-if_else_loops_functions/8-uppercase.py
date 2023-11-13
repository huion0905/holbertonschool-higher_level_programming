#!/usr/bin/python3

def uppercase(str):
    result = ""

    for char in str:
        if (ord('a') <= ord(char) <= ord('z')):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += uppercase_char
        else:
            result += char

    print("{}".format(result))
