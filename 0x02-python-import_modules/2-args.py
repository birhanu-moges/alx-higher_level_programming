#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n <= 0:
        print("{:d} arguments:".format(n))
    elif n > 0:
        print("{:d} arguments:".format(n))
        arglist = sys.argv[1:]
        index = 1
        for element in arglist:
            print("{:d}: {:s}".format(index, element))
            index += 1
