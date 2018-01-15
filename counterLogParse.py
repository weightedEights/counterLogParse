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

import os, fileinput, argparse, sys
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
    # logpath will eventually just be assumed to be root, but can be specified via argv switch
    logPath = os.getcwd() + "\logs.rotatingFormat"

    # file list must have specific argument, or ask "are you sure" before pulling in whole directory
    # also, in future include a printed list of what files are about ot be  processed with a y/n dialog
    monthArg = '05'
    fileList = [x for x in os.listdir(logPath) if x[-5:-3] == monthArg]

    # load just the data from the file list into one, large array
    # this should end up as a generator function, passing values to the file i/o or plotter
    cattedDatArray = loadFileListData(logPath, fileList)

    # writeCattedFile(cattedDatArray, cattedFile)
    """ end option [-r] """

    """ option [-p] """
    # generate plot or plots from either a catted log, or from an argv existing log
    # buildPlotCattedTrend(cattedDatArray)
    # showPlot()
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


def loadFileListData(path, fileList):

    fileNameList = [os.path.join(path, x) for x in fileList]

    # skips the first line of the csv, builds a list (date,data) tuples, then returns list sorted by datetime
    dataList = [s.rstrip().split(',') for s in fileinput.input(fileNameList) if not fileinput.isfirstline()]

    return sorted(dataList)


def writeCattedFile(data, name):

    with open(name, 'a') as log:
        for line in data:
            log.write(str(line[0]) + "," + str(line[1]) + "\n")


def buildPlotCattedTrend(data):

    # convert data list to numpy array with datetime objects
    timeFormat = "%Y-%m-%d %H:%M:%S.%f"
    numData = [[datetime.strptime(n[0], timeFormat), float(n[1])] for n in data]
    datArray = np.array(numData)

    # plotting individual log files creates discontinuities between x vals, so create one subplot per calendar day
    # x-values contain date elements: (YYYY, MM, DD, HH, MM, SS, uS). the SS elements will become the plotted values,
    # the HHMM for x-axis ticks, and the YYYYMMDD for the plot title

    # first define yVals, which will have the same range across all plots
    yVals = datArray[:, 1]
    yLims = [min(yVals) * 2, max(yVals) * 2]

    print(datArray)

    # create list of calendar days represented
    dayFormat = "%Y%m%d"
    daysInDat = sorted(list(set([dt.strftime(dayFormat) for dt in datArray[:,0]])))
    print(daysInDat)

    # x-axis should be 24 ticks for one whole day
    hourFormat = "%H%M"
    xTicks = [dt.strftime(hourFormat) for dt in datArray[:,0]]
    print(xTicks)

    # shift Y values by 10MHz, to only plot mHz centered around zero
    datArray[:,1] -= 10000000

    xVals = [dt.second for dt in datArray[:,0]]
    # xLims = [min(datArray[:,0]) - timedelta(hours=1), max(datArray[:,0]) + timedelta(hours=1)]

    # print(mdates.date2num(datArray[:,0]))

    # for plot date formatting, reference: http://matplotlib.org/examples/api/date_demo.html

    plt.figure()
    # first subplot gets the y-axis label
    plt.subplot(1, 2, 1)
    plt.ylabel('Deviation from 10MHz [Hz]')
    plt.scatter(xVals, yVals, color='b', alpha=0.5, marker='s', s=20)
    plt.gcf().autofmt_xdate()

    # x-axis label will be the date
    plt.xlabel(str(daysInDat[0]))

    plt.subplot(1, 2, 2)
    plt.scatter(xVals, yVals, color='b', alpha=0.5, marker='s', s=20)
    plt.gcf().autofmt_xdate()

    # x-axis label will be the date
    plt.xlabel(str(daysInDat[1]))



    # plt.xlim(xLims)
    plt.ylim(yLims)

    plt.show()


def showPlot():

    pass


if __name__ == main():
    # main(sys.argv[1:])
    main()
