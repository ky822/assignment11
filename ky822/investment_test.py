'''
Created on Dec 6, 2014

@author: keye
'''
import unittest
from investment_functions.Exceptions import *
from investment_functions.PositionInput import *
from investment_functions.Set_num_trials import Set_num_trials

class Test_PositionInput(unittest.TestCase):
    """
    Test the PositionInput function.
    """
    
    def setUp(self):
        """
        Initializing for test.
        """
        pass

    def tearDown(self):
        pass
    
    def test_InvalidFormat(self):
        """
        Test for invalid format of the input.
        """
        self.assertRaises(InvalidFormat, PositionInput, '\n' )
        self.assertRaises(InvalidFormat, PositionInput, '(1,1,1)' )
        self.assertRaises(InvalidFormat, PositionInput, '1,1,1,' )
        self.assertRaises(InvalidFormat, PositionInput, '[1,1' )
        
    def test_InvalidPosition(self):
        """
        Test for invalid input of position value.
        """
        self.assertRaises(InvalidPosition, PositionInput,'[1.1,2.5]')
        self.assertRaises(InvalidPosition, PositionInput,'[-1]')
        self.assertRaises(InvalidPosition, PositionInput,'[22,22,22]')
        self.assertRaises(InvalidPosition, PositionInput,'[1,+1008]')
        self.assertRaises(InvalidPosition, PositionInput,'[1,a,b]')
         

class Test_Set_num_trials(unittest.TestCase):
    """
    Test the Set_num_trials function.
    """                 
    
    def setUp(self):
        """
        Initializing for test.
        """
        pass

    def tearDown(self):
        pass
    
    def test_InvalidTrialNum(self):
        """
        Test for invalid input of trial number.
        """
        self.assertRaises(InvalidTrialNum, Set_num_trials,'-1')
        self.assertRaises(InvalidTrialNum, Set_num_trials,'1.1')
        self.assertRaises(InvalidTrialNum, Set_num_trials,'adfas')
        self.assertRaises(InvalidTrialNum, Set_num_trials,'2,2')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
