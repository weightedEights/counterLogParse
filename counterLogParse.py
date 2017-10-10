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

SCOPE UNDER REVISION

"""

import os
import argparse
import sys
import numpy as np
from datetime import datetime

__appname__ = "counterLogParse.py"
__author__ = "J.Arndt, Sondrestrom Radar"
__version__ = "v0.1, 22Sep2017"
__doc__ = "Counter Logger Log File Utilities"

PATH_TO_LOGS = "./logs.rotatingFormat"


def main(pargs):
    """ docstring description """

    if pargs.version:
        print(__version__)

    if pargs.cat_logs:
        cat_logs(args.cat_logs)


def get_log_file_mean(log_file):
    data_array = np.genfromtxt(log_file, skip_header=0, delimiter=',', usecols=1)
    data_mean = np.mean(data_array, dtype=np.float64)
    return data_mean


def cat_logs(arg):
    # first check if path exists
    if not os.path.exists(PATH_TO_LOGS):
        raise Exception('ERROR: cat_logs: incorrect path')

    full_log_path = os.path.join(PATH_TO_LOGS, arg)

    # then check if the log file exists
    if not os.path.exists(full_log_path) and not os.path.isfile(full_log_path):
        raise Exception('ERROR: cat_logs: log file not found')

    print("Log file found. Reading...")

    # calculate the mean value for the whole log
    log_file_mean = get_log_file_mean(full_log_path)
    print("Average value for file {} is: {}".format(arg, log_file_mean))

    # get the date for the file


def get_arguments():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-v', '--version', action='store_true', help='Print version')
    parser.add_argument('-c', '--concatenate', action='store', dest='cat_logs', help='Pass arg after -c switch.')

    return parser.parse_args()


if __name__ == '__main__':
    try:
        args = get_arguments()
        main(args)

    except KeyboardInterrupt as e:
        sys.exit(0)
