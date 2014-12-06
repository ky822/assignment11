'''
Created on Dec 5, 2014

@author: keye
'''

class InvalidTrialNum():
    def __repr__(self):
        return 'The number of simulating days is not valid! You should input positive integers.\nPlease try again!\n'
        
class InvalidFormat():
    def __repr__(self):
        return 'The format of input is not valid!\nPlease input a list of the number of shares to buy in parellel: e.g. [1, 10, 100, 1000]\n'
        
class InvalidPosition():
    def __repr__(self):
        return 'The input value of the positions is not valid!\nPlease input a list of the number of shares to buy in parellel: e.g. [1, 10, 100, 1000]\nThe input position should be 1, 10, 100 or 1000.\n'
        