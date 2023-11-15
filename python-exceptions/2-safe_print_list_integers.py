#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (ValueError, TypeError, IndexError):
            if isinstance(my_list[i], int):
                raise
        finally:
            count += 1
    print()
    return printed

