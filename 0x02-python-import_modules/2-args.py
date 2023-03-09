#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n <= 0:
        print("{:d} arguments:".format(n))
    elif n > 0:
        print("{:d} arguments:".format(n))
        for index in range(n):
            print("{:d}: {:s}".format(index + 1, sys.argv[index + 1]))
