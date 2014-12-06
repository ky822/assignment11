'''
Created on Dec 5, 2014

@author: keye
'''
import numpy as np

def CollectStatsResult(filename,position,daily_ret):
    """
    This function creates a file to collect the mean and standard deviation of the daily return.
    It will store the means and standard deviations in a text file
    """
    filename.write('Position: {}\n'.format(position))
    filename.write('Mean: {}; Std: {}\n\n'.format(np.mean(daily_ret),np.std(daily_ret)))