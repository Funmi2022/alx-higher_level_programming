#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
        print("Last digit of {number:d} is {digit:d} and is ", end="")
    elif digit > 5:
            print("Last digit of {number:d} is {digit:d} and is greater than 5")
        elif digit == 0:
                print("Last digit of {number:d} is {digit:d} and is 0")
            else:
                    print("Last digit of {number:d} is {digit:d} and is less than 6 and not 0")
