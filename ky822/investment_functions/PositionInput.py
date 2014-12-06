'''
Created on Dec 5, 2014

@author: keye
'''
import sys
from exceptions import *

def PositionInput():
    """
    This function is to input a list of the number of shares to buy.
    """
    while True:
        
        try:
            positions = raw_input('Please input a list of the number of shares to buy in parellel: e.g. [1, 10, 100, 1000]\n' )
            
            #Check if the input of positions is invalid.
            positions_list = ExaminePosition(positions)         
            break
        
        except IndexError as e:
            print '\n{}!\nThe format of input is not valid!\n'.format(e)  
        except (NameError,SyntaxError,ValueError) as e:
            print '\n{}!\nYour input is not valid!\nPlease try again!\n'.format(e)       
        except (KeyboardInterrupt, EOFError):
            print '\nYou are going to exit the program!\nBye!'
            sys.exit()
            
    return positions_list


def ExaminePosition(positions):
    """
    This function is to check if the positions is in a valid format and a valid value. 
    """
    try:
        #Remove the leading and trailing whitespaces.
        positions = positions.strip()
        positions_list = []
        
        #Exception handling    
        if positions[0]!='[' or positions[-1]!=']':
            raise InvalidFormat()
            
        positions = positions[1:-1].split(',')
        
        for position in positions:     
            if all(int(position) != p for p in (1, 10, 100, 1000)):
                raise InvalidPosition()             
            else:
                position = int(position)
                positions_list.append(position)
        return positions_list     
      
    except (KeyboardInterrupt, EOFError):
            print '\nYou are going to exit the program!\nBye!'
            sys.exit()