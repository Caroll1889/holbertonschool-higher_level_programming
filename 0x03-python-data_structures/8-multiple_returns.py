#!/usr/bin/python3


def multiple_returns(sentence):

    lon = len(sentence)

    if lon == 0:
        c = None

    else:
        c = sentence[0]

    return (lon, c)
