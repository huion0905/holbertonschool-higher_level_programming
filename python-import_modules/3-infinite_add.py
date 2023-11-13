#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    result = 0

    for argument in argv[1:]:
        if (argument < '0'):
            argument = int(argument)
        result += int(argument)

    print("{:d}".format(result))
