#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""

Summary

"""

import sys, getopt, os

def main(argv):

    cattedFilePath = os.getcwd()
    cattedFileName = "cattedLog.csv"

    cattedFile = cattedFileSetup(cattedFileName, cattedFilePath)

    cattedDatArray = loadLogs("test.data.txt")
    writeCattedFile(cattedFile)

    if len(sys.argv) > 1 and sys.argv[1] == '-s' and sys.argv[2] == True:
        funcVal = secFunc(funcVal, sys.argv[2])

    plotCattedTrend(cattedDatArray)


def cattedFileSetup(name, path):

    return aFile


def loadLogs(file):
    with open(file, 'r') as fin:
        parsedList = [s for s in fin.read()]

    return parsedList


def writeCattedFile(dat):

    pass


def plotCattedTrend(data):

    pass


if __name__ == main():
    main()
