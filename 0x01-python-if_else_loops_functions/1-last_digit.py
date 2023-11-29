#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
LD = abs(num) % 10
if num < 0:
    LD = -LD
    print(f"Last digit of {num:d} is {LD:d} and is ", end="")
    if LD > 5:
        print("greater than 5")
    elif LD == 0:
        print("0")
    else:
        print ("less than 6 and not 0")
