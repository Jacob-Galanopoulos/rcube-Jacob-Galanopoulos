'''
Created on Oct 6, 2020

@author: jakeg
'''
import unittest
import RCube.info as info


class Test(unittest.TestCase):


    def test100_010_ShouldReturnMyUserName(self):
        expectedResult = {'user': 'jdg0058'}
        parms = {'op': 'info'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_010_InfoWithExtraParameters(self):
        expectedResult = {'user': 'jdg0058'}
        parms = {'op': 'info',
                 'f': '123456'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)