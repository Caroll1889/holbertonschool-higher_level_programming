#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

mod = abs(number) % 10

if number < 0:
    mod *= -1

if mod > 5:
    str = "greater than 5"
elif mod == 0:
    str = "0"

else:
    str = "less than 6 and not 0"
print("Last digit of {:d} is {:d} and is {:s}".format(number, mod, str))
