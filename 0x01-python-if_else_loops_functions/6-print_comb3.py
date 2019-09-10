#!/usr/bin/python3

i = 0
while i < 8:
    j = i
    while j <= 9:
        if j != i:
            print("{:d}{:d}".format(i, j), end=", ")
        j = j + 1
    i = i + 1
print("{:d}{:d}".format(i, j - 1), sep="")
