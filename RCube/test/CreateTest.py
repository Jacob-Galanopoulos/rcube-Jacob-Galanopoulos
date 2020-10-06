'''
Created on Oct 6, 2020

@author: jakeg
'''
import unittest
import RCube.create as create

class Test(unittest.TestCase):


    def test100_010_HappyPathNominalNumberOfFaces(self):
        expectedResult = {'cube': '111111111222222222333333333444444444555555555666666666', 
                          'integrity': '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED', 
                          'status':'ok'}
        parms = {'op': 'create',
                 'faces': '123456'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_020_HappyPathDefaultEmptyFaceValue(self):
        expectedResult = {'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 
                          'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 
                          'status':'ok'}
        parms = {'op': 'create',
                 'faces': ''}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_030_HappyPathFacesMissingOverall(self):
        expectedResult = {'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 
                          'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 
                          'status':'ok'}
        parms = {'op': 'create'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_040_HappyPathExtraneousParms(self):
        expectedResult = {'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 
                          'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 
                          'status':'ok'}
        parms = {'op': 'create',
                 'f': '123456'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_910_SadPathTooManyFaces(self):
        expectedResult = {'status': 'error: Incorrect length of faces - must be exactly 6 faces'}
        parms = {'op': 'create',
                 'faces': '1234567'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test200_920_SadPathTooFewFaces(self):
        expectedResult = {'status': 'error: Incorrect length of faces - must be exactly 6 faces'}
        parms = {'op': 'create',
                 'faces': '12345'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_930_SadPathDuplicateFaceValue(self):
        expectedResult = {'status': 'error: No duplicate faces are allowed'}
        parms = {'op': 'create',
                 'faces': '112345'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)