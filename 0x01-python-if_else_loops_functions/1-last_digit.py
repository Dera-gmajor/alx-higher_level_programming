#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
number = -98

if number < 0:
        LD = -(abs(number) % 10)
    else:
        LD = abs(number) % 10
        print(f"Last digit of {number:d} is {LD:d} and is ", end="")

        if LD > 5:
            print("greater than 5")
        elif LD == 0:
            print("0")
        else:
            print("less than 6 and not 0")
