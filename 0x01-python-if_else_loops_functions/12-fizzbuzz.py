#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(F"FizzBuzz ", end="")
        elif i % 3 == 0:
            print(F"Fizz ", end="")
        elif i % 5 == 0:
            print(F"Buzz ", end="")
        else:
            print(i)
