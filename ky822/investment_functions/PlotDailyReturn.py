'''
Created on Dec 5, 2014

@author: keye
'''
import matplotlib.pyplot as plt

def PlotDailyReturn(position,daily_ret):
    """
    This function is to plot the result of the trials in a histogram with X axis from -1.0 to +1.0 and Y axis as the number of trials
    with that result for each position.
    """
    plt.figure()
    #Plot the result of the trials in a histogram with X axis from -1.0 to +1.0 and Y axis as the number of trials.
    plt.hist(daily_ret,100,range=[-1,1])
    plt.xlabel('Daily return')
    plt.ylabel('The number of trials')
    plt.title('The histogram of daily return for position ={}'.format(position))
    plt.savefig('histogram_{}_pos.pdf'.format(str(position).zfill(4)))
