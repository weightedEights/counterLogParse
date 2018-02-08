

#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import print_function


"""

Load, parse, and plot a single .csv file of counter logger data. 

"""


import os
import sys
import argparse
from datetime import datetime
import glob
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


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

    if pargs.plot_daily_mean:
        plot_daily_mean(args.plot_daily_mean)


def append_daily_csv(arg):
    # pd.options.display.float_format = "{:.7f}".format
    # pd.set_option('precision', 7)

    # check for existing daily mean/avg log, create if not exist
    daily_mean_log = "daily_mean_log.csv"
    if not os.path.exists(daily_mean_log):
        with open(daily_mean_log, "w") as log:
            log.write("Date,CounterMean\n")

    file_list = [x for x in glob.glob(os.path.join(arg, "counterLog*"))]

    with open(daily_mean_log, "a") as log:
        for f in file_list:
            print("Working on file: {}...".format(f))

            # for pandas dataframe, column "names" are defined, else it will use first row data
            working_frame = pd.read_csv(f, skiprows=0, names=['datetime', 'counter_val'], parse_dates=['datetime'])
            # print("Working frame: \n{}\n".format(working_frame))

            # get date from frame
            # get mean from one day of measurements, rounded to 7 sig figs, same as the measurements
            working_date = working_frame['datetime'][0].date()
            working_mean = working_frame['counter_val'].mean().round(7)
            print("Date: {}, Mean: {:.7f}\n".format(working_date, working_mean))

            # append to csv
            log.write("{},{:.7f}\n".format(working_date, working_mean))


def plot_daily_mean(arg):
    """
    source/guide for plotting:
    http://www.augustkleimo.com/import-and-plot-stock-price-data-with-python-pandas-and-seaborn/

    http://seaborn.pydata.org/examples/timeseries_from_dataframe.html

    https://zahidhasan.github.io/2017-04-13-ploting-with-seaborn/

    https://chrisalbon.com/python/data_wrangling/pandas_time_series_basics/

    http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html

    """
    print("Daily mean plotting goes here!")

    # index_col must be set to dates for pandas time series methods
    df = pd.read_csv(arg, parse_dates=['Date'], index_col=['Date'])

    df.resample('M').mean().plot()
    plt.show()

    # df.set_index('Date', inplace=True)
    # df['CounterMean'].plot()

    # time series is the wrong plot for this data
    # sns.tsplot(data=df, time="Date", value="CounterMean", unit="Hz", ci="sd")
    # plt.show()


def get_arguments():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-v', '--version', action='store_true', help='Print version')
    parser.add_argument('-a', '--append', action='store', dest='append_daily_csv',
                        help='Path to log files, e.g. "./logs"')
    parser.add_argument('-p', '--plot', nargs='?', const='./daily_mean_log.csv', action='store', dest='plot_daily_mean',
                        help='Path to daily_mean_log file, default "./"')

    return parser.parse_args()


if __name__ == '__main__':
    try:
        args = get_arguments()
        main(args)

    except KeyboardInterrupt as e:
        print("User interrupted:\n{}.".format(e.message))
        sys.exit(0)
