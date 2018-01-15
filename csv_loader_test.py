#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import print_function


"""

Load, parse, and plot a single .csv file of counter logger data. 

"""


import os
import glob
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


def main():

    pd.options.display.float_format = "{:.7f}".format

    # create empty data frame to populate
    new_frame = pd.DataFrame()

    file_list = [x for x in glob.glob("testLog.2016[12]*")]

    for f in file_list:
        print("Working on file: {}...".format(f))
        working_frame = pd.read_csv(f, skiprows=0, parse_dates=['Time'])
        # print(working_frame)
        new_frame = new_frame.append(working_frame)
        # print(new_frame)

    print(new_frame)

    # create the unordered set first, then convert to list.ordered()
    the_days = set(d.day for d in new_frame["Time"])

    print(the_days)

if __name__ == '__main__':
    main()
