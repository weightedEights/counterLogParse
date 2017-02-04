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

import os, fileinput, argparse
from datetime import datetime, timedelta
from pylab import savefig as sf
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

def main():
    """ argparse begin"""
    # these function groups will be contained within argparse statements, to control when they run

    """ option [-r] """
    # create a directory for a new file, set generic file name, create a CSV file with an index and header
    # cattedFilePath = os.getcwd()
    # cattedFileName = "cattedLog"
    # cattedFile = cattedFileSetup(cattedFileName, cattedFilePath)

    # load data from argv logs, either a single file or a list doesnt matter
    singleFile = "test.data.txt"
    fileList = ["testLog.20161219.002.csv", "testLog.20161220.001.csv", "testLog.20161219.001.csv"]
    cattedDatArray = loadLogList(fileList)
    # writeCattedFile(cattedDatArray, cattedFile)
    """ end option [-r] """

    """ option [-p] """
    # generate plot from either a catted log, or from an argv existing log
    buildPlotCattedTrend(cattedDatArray)
    showPlot()
    """ end option [-p] """


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


def loadLogList(fileList):

    dataList = [s.rstrip().split(',') for s in fileinput.input(fileList) if not fileinput.isfirstline()]
    sortedList = sorted(dataList)

    return sortedList


def writeCattedFile(data, name):

    with open(name, 'a') as log:
        for line in data:
            log.write(str(line[0]) + "," + str(line[1]) + "\n")


def buildPlotCattedTrend(data):

    # generate list of dates represented
    dateList = []
    for n in data:
        if n[0].split(" ")[0] not in dateList:
            dateList.append(n[0].split(" ")[0])

    # convert data list to numpy array with datetime objects
    timeFormat = "%Y-%m-%d %H:%M:%S.%f"
    numData = [[datetime.strptime(n[0], timeFormat), float(n[1])] for n in data]
    datArray = np.array(numData)

    # shift Y values by 10MHz, to only plot mHz centered around zero
    datArray[:,1] -= 10000000

    xVals = [datArray[:,0]]
    yVals = [datArray[:,1]]

    plt.figure()
    plt.subplot(1, 1, 1)
    plt.scatter(xVals, yVals)

    plt.show()


def showPlot():

    pass


if __name__ == main():
    main()
