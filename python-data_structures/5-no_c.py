#!/usr/bin/python3
def no_c(my_string):
    cadena = ""
    for char in my_string:
        word_ascii = ord(char)
        if word_ascii != 99 and word_ascii != 67:
            cadena += char
    return cadena
