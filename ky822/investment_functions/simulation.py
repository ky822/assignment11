'''
Created on Dec 5, 2014

@author: keye
'''
import numpy as np

def simulation(position, num_trials):
    """
    This function simulates the outcome of one day of investment.
    """
    daily_ret = []
    position_value = 1000/position
    
    for trial in xrange(num_trials):
        cumu_ret = sum(np.random.choice([0,2],position,p=[0.49,0.51])) * position_value
        daily_ret.append(float(cumu_ret)/1000 - 1)
        
    return daily_ret
    