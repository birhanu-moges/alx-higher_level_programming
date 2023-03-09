#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    # Total number of argv n
    n = len(sys.argv) - 1
    if n <= 0:
        print("{} arguments".format(n))
    elif n > 0:
        print("{} arguments".format(n))
        arglist = sys.argv[1:]
        index = 1
        for element in arglist:
            print("{}: {}".format(index, element))
            index += 1
