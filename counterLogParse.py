#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""

The purpose is to read one or more log files, concatenate their data into one new file, and to generate a simple trend
plot (freq vs time).

This script is also an exercise in parsing command line switches. For example, choosing to only concatenate logs without
generating a plot. Or, generating a plot based on one log and not concatenating a range.

Usage:

counterLogParse.py [-h] [-p] [-r] <logFileRangeStart> <logFileRangeStop>

[-h]
    Print this usage
[-p] <logFile>
    Generate plot, requires either log file or..
[-r] <logFile1> <logFile2> <logFile#>
    Concatenate a list of log files into one, new log file. New file can be used as the source data to plot.

"""

import sys, os, fileinput
from datetime import datetime
import argparse

def main():

    # these function groups will be contained within argparse statements, to control when they run

    # create a directory for a new file, set generic file name, create a CSV file with an index and header
    # cattedFilePath = os.getcwd()
    # cattedFileName = "cattedLog"
    # cattedFile = cattedFileSetup(cattedFileName, cattedFilePath)

    # load data from argv logs, in date order, and write to the empty file created by cattedFileSetup
    # will have to be careful to check that dates are consecutive
    # time formatting: "%Y-%m-%d %H:%M:%S.%f"
    singleDatArray = loadLogSingle("test.data.txt")

    cattedDatArray = loadLogList(["testLog.20161219.002.csv", "testLog.20161220.001.csv", "testLog.20161219.001.csv"])

    # writeCattedFile(cattedFile)

    # generate plot from either a catted log, or from an argv existing log
    plotCattedTrend(singleDatArray)


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


def loadLogSingle(file):

    with open(file, 'r') as fin:
        # ignore the first row which is the header
        # return a list of lists, (time string, measurement string)
        parsedList = [s.rstrip().split(',') for s in fin.readlines()][1:]
    # convert measurement element to float
    parsedList = [[n[0], float(n[1])] for n in parsedList]

    return parsedList


def loadLogList(fileList):

    dataList = [s.rstrip().split(',') for s in fileinput.input(fileList) if not fileinput.isfirstline()]
    sortedList = sorted(dataList)

    return sortedList


def writeCattedFile(dat):

    pass


def plotCattedTrend(data):

    pass


if __name__ == main():
    main()
