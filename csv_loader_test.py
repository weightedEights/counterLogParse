#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import print_function


"""

Load, parse, and plot a single .csv file of counter logger data. 

"""


# import os
# from datetime import datetime
import glob
import pandas as pd
# from matplotlib import pyplot as plt
# import seaborn as sns
# import numpy as np


def main():

    pd.options.display.float_format = "{:.7f}".format
    # pd.set_option('precision', 7)

    # create empty data frame to populate, for future this will be a new file to write daily data points
    # csv write format: call_df.to_csv('D:/Call.csv', date_format='%Y-%m-%d %H:%M:%S')
    running_frame = pd.DataFrame(columns=['Date', 'CounterAvg'])

    file_list = [x for x in glob.glob("testLog.2016[12]*")]

    for f in file_list:
        print("Working on file: {}...".format(f))

        # sep= resolves the issue of spaces in the column names when importing
        working_frame = pd.read_csv(f, sep='\s*,\s*', skiprows=0, parse_dates=['Time'], engine='python')
        print("Working frame: \n{}\n".format(working_frame))

        # get date from frame
        # get mean from one day of measurements
        working_date = working_frame['Time'][0].date()
        working_mean = working_frame['CounterData'].mean()
        print("Date: {}, Avg: {:.7f}\n".format(working_date, working_mean))

        # create new row to concat to running_frame using standard dict format
        working_dict = {"Date": working_date, "CounterAvg": working_mean}
        print("Working dict: {}\n".format(working_dict))

        # append to running frame
        running_frame.append(working_dict, ignore_index=True)
        print("Running frame: \n{}\n".format(running_frame))


if __name__ == '__main__':
    main()
