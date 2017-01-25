#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""

Summary

"""


def main():

    datArray = loadprob("test.data.txt")

    funcVal = firstFunc(datArray)

    secVal = secFunc(funcVal)

    displayResult(secVal)


def loadprob(file):
    with open(file, 'r') as fin:
        parsedList = [s for s in fin.read()]

    return parsedList


def firstFunc(num):

    return num


def secFunc(num):

    return num


def displayResult(data):

    print(data)


if __name__ == main():
    main()
