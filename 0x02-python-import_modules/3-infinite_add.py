#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    num = len(argv)

    num2 = 0

    for i in range(1, num):
        num2 += int(argv[i])
    print("{}".format(num2))
