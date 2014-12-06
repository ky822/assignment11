'''
Created on Dec 5, 2014

@author: keye
'''
import sys
from exceptions import *

def Set_num_trials():
    """
    This function is to an input for the number of simulating days.
    
    return: num_trials
    
    """
    
    while True: 
        try:
            num_trials = eval(raw_input('Please input the number of simulating days: \n'))
            if type(num_trials) != int or num_trials <= 0:
                raise InvalidTrialNum() 
            elif type(num_trials) == int and num_trials > 0:
                break    
        
        except (NameError,SyntaxError,ValueError) as e:
            print '\n{}!\nYour input is not valid! You should input positive integers.\nPlease try again!\n'.format(e)
        except (KeyboardInterrupt, EOFError):
            print '\nYou are going to exit the program!\nBye!'
            sys.exit()
    
    return num_trials