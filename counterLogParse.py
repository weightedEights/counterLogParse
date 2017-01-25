#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""

Summary

"""

import sys

def main():

    datArray = loadprob("test.data.txt")

    funcVal = firstFunc(datArray)

    if len(sys.argv) > 1 and sys.argv[1] == '-s' and sys.argv[2]:
        funcVal = secFunc(funcVal, sys.argv[2])

    displayResult(funcVal)


def loadprob(file):
    with open(file, 'r') as fin:
        parsedList = [s for s in fin.read()]

    return parsedList


def firstFunc(num):

    return num


def secFunc(dat, add):

    dat += add

    return dat


def displayResult(data):

    print(data)


if __name__ == main():
    main()
