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

import sys, os, time
import argparse

def main():

    # these function groups will be contained within argparse statements, to control when they run

    # create a directory for a new file, set generic file name, create a CSV file with an index and header
    cattedFilePath = os.getcwd()
    cattedFileName = "cattedLog"
    cattedFile = cattedFileSetup(cattedFileName, cattedFilePath)

    # load data from argv logs, in date order, and write to the empty file created by cattedFileSetup
    # will have to be careful to check that dates are consecutive
    cattedDatArray = loadLogs("test.data.txt")
    writeCattedFile(cattedFile)

    # generate plot from either a catted log, or from an argv existing log
    plotCattedTrend(cattedDatArray)


def cattedFileSetup(name, path):

    logFilePath = os.path.join(path, "cattedLogs")
    if not os.path.exists(logFilePath):
        os.mkdir(logFilePath)

    ind = 1
    logFile = os.path.join(logFilePath, "{}.{:03d}.csv".format(name, ind))

    while os.path.exists(logFile):
        ind += 1
        logFile = os.path.join(logFilePath, "{}.{:03d}.csv".format(name, ind))

    with open(logFile, "w") as log:
        log.write("Time, CounterData\n")

    return logFile


def loadLogs(file):
    with open(file, 'r') as fin:
        parsedList = [s for s in fin.read()]

    return parsedList


def writeCattedFile(dat):

    pass


def plotCattedTrend(data):

    print(data)


if __name__ == main():
    main()
