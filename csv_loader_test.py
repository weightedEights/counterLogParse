

#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import print_function


"""

Load, parse, and plot a single .csv file of counter logger data. 

"""


import os
import sys
import argparse
# from datetime import datetime
import glob
import pandas as pd
# from matplotlib import pyplot as plt
# import seaborn as sns
# import numpy as np


__appname__ = "csv_loader_test.py"
__author__ = "J.Arndt, Sondrestrom Radar"
__version__ = "v0.1, 17Jan2018"
__doc__ = "Counter Logger Log File Utilities"


def main(pargs):
    """ docstring description """

    if pargs.version:
        print(__version__)

    if pargs.append_daily_csv:
        append_daily_csv(args.append_daily_csv)


def append_daily_csv(arg):
    # pd.options.display.float_format = "{:.7f}".format
    # pd.set_option('precision', 7)

    # check for existing daily mean/avg log, create if not exist
    daily_mean_log = "daily.mean.log.csv"

    with open(daily_mean_log, "w") as log:
        log.write("Date,CounterMean\n")

    file_list = [x for x in glob.glob(os.path.join(arg, "counterLog*"))]

    for f in file_list:
        print("Working on file: {}...".format(f))

        # sep= resolves the issue of spaces in the column names when importing
        working_frame = pd.read_csv(f, skiprows=0, names=['datetime', 'counter_val'], parse_dates=['datetime'])
        print("Working frame: \n{}\n".format(working_frame))

        # get date from frame
        # get mean from one day of measurements, rounded to 7 sig figs, same as the measurements
        working_date = working_frame['datetime'][0].date()
        working_mean = working_frame['counter_val'].mean().round(7)
        print("Date: {}, Mean: {:.7f}\n".format(working_date, working_mean))

        # append to csv
        with open(daily_mean_log, "a") as log:
            log.write(str(working_date) + "," + str(working_mean) + "\n")


def get_arguments():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-v', '--version', action='store_true', help='Print version')
    parser.add_argument('-a', '--append', action='store', dest='append_daily_csv', help='Path to log files, e.g. "./logs"')

    return parser.parse_args()


if __name__ == '__main__':
    try:
        args = get_arguments()
        main(args)

    except KeyboardInterrupt as e:
        sys.exit(0)
