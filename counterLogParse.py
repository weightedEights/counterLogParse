#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""

The purpose is to read one or more log files, concatenate their data into one new file, and to generate a simple trend
plot (freq vs time).

This script is also an exercise in parsing command line switches. For example, choosing to only concatenate logs without
generating a plot. Or, generating a plot based on one log and not concatenating a range.

Usage = counterLogParse.py [-h] [-p] [-r] <logFileRangeStart> <logFileRangeEnd>

"""

import sys, getopt, os

def main(argv):

    cattedFilePath = os.getcwd()
    cattedFileName = "cattedLog.csv"

    cattedFile = cattedFileSetup(cattedFileName, cattedFilePath)

    cattedDatArray = loadLogs("test.data.txt")
    writeCattedFile(cattedFile)

    plotCattedTrend(cattedDatArray)

    inputFile = ''
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["inFile=", "outFile="])

    except getopt.GetoptError:
        print("USAGE")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("USAGE")
            sys.exit()

        elif opt in ("-i", "--inFile"):
            inputFile = arg

        elif opt in ("-o", "--outFile"):
            outputFile = arg


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
