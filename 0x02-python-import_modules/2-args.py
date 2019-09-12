#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    argnum = len(argv)

    print("{}".format(argnum - 1), end="")

    if argnum == 1:
        print(" arguments.")
    elif argnum == 2:
        print(" argument:")
    else:
        print(" arguments:")

    for i in range(1, argnum):
        print("{}: {}".format(i, argv[i]))
