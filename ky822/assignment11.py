'''
Created on Dec 5, 2014

@author: keye
'''
import sys
from investment_functions.PositionInput import *
from investment_functions.CollectStatsResult import *
from investment_functions.PlotDailyReturn import *
from investment_functions.Set_num_trials import *
from investment_functions.simulation import *

def main():
    """
    1.This function gets inputs from user for the positions and the number of trials.
    2.This function simulates positions, plot the results of the trials in a histogram with X axis 
      from -1.0 to +1.0 and Y axis as the number of trials with that result for each position.
    3.This function collects the means and standard deviations and store them in a text file.
    """
    
    #Get inputs from user for a list of positions and a number of trials(how many times to randomly repeat the test). 
    positions = PositionInput()
    num_trials = Set_num_trials()
   
    print 'Mission 2 Completed!\n'
    
    try:
        #Create a file for statistics.
        results_txt = open('results.txt','w')
        
        #Do the simulation and Plot a histogram for each position in the list of positions. Afterwards, get the mean and standard deviation of the daily return and write them into the file for statistics.
        for position in positions:
            daily_ret = simulation(position, num_trials)
            PlotDailyReturn(position,daily_ret)
            CollectStatsResult(results_txt,position,daily_ret)
        results_txt.close()     
        
        print 'Mission 3 Completed!\n'   
    
    except IOError as e:
        print '\n{}!\nCheck the file.\n'.format(e)
    except (KeyboardInterrupt, EOFError):
        print '\nYou are going to exit the program!\nBye!'
        sys.exit()
        
if __name__ == '__main__':
    main()