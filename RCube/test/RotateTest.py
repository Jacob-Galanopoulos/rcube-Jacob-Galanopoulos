'''
Created on Nov 17, 2020

@author: jakeg
'''
import unittest
import RCube.rotate as rotate

class Test(unittest.TestCase):
    
    def test100_010_NominalRotateFrontRight(self):
        expectedResult = {'status':'rotated', 
                          'cube':'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy', 
                          'integrity':'0F3BDBE402C16D85756959CDEE1649281296A8507CDDF29EC328C72CC758DA28'}
        parms = {'side': 'f','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_015_NominalRotateFrontLeft(self):
        expectedResult = {'status': 'rotated', 
                          'cube': 'oooooooooyggyggyggrrrrrrrrrbbwbbwbbwwwwwwwgggbbbyyyyyy', 
                          'integrity': '0725FE3DE940D22412488858679E49038627A91F615FE641A3CA897B08F14C09'}
        parms = {'side': 'F','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_020_NominalRotateBackRight(self):
        expectedResult = {'status': 'rotated', 
                          'cube': 'oooooooooggyggyggyrrrrrrrrrwbbwbbwbbgggwwwwwwyyyyyybbb', 
                          'integrity': 'CF7F7CA7F091782686E19721F50C78B9D46408A00A992E414D8B2D33C999D9B9'}
        parms = {'side': 'b','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_025_NominalRotateBackLeft(self):
        expectedResult = {'status': 'rotated', 
                          'cube': 'oooooooooggwggwggwrrrrrrrrrybbybbybbbbbwwwwwwyyyyyyggg', 
                          'integrity': '0734348E61CFFD1BFDDD3989819FC035ED5128230E2A04B4C1346BE1086934E1'}
        parms = {'side': 'B','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_030_NominalRotateLeftRight(self):
        expected = {'cube': 'woowoowoogggggggggrryrryrrybbbbbbbbbrwwrwwrwwoyyoyyoyy', 'integrity': '50FAFE62BF3BB0CF259572E7992AC528A4DFEE0BEB8B0F4EAC768E68262262D1', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'l', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_035_NominalRotateLeftLeft(self):
        expected = {'cube': 'yooyooyoogggggggggrrwrrwrrwbbbbbbbbbowwowwowwryyryyryy', 'integrity': 'C323A402B51C4594101DB8EF9DD2808100987459684AB6C7B433D4A54D3DD605', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'L', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_040_NominalRotateRightRight(self):
        expected = {'cube': 'ooyooyooygggggggggwrrwrrwrrbbbbbbbbbwwowwowwoyyryyryyr', 'integrity': '84DF9D66A7A22B043BD6B77947DD548ADA1A74091E8F544E31C1DB2B8F4FE5FB', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'r', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_045_NominalRotateRightLeft(self):
        expected = {'cube': 'oowoowoowgggggggggyrryrryrrbbbbbbbbbwwrwwrwwryyoyyoyyo', 'integrity': '343D9B61D1F3FA8206CC7569F9D64A2A8B796E8487A1234CC5FCABD44BEDE263', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'R', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_050_NominalRotateTopRight(self):
        expected = {'cube': 'gggoooooorrrggggggbbbrrrrrrooobbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'E03151E1977723626C4896A60618759D4821F62EAF753955D97B8B70DDA2DE0B', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 't', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_055_NominalRotateTopLeft(self):
        expected = {'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'T', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_060_NominalRotateUnderRight(self):
        expected = {'cube': 'oooooobbbggggggooorrrrrrgggbbbbbbrrrwwwwwwwwwyyyyyyyyy', 'integrity': 'BA29EA321B8E33BF21FFCFFBA10A0F81509AEC5208BC37179A4C613093B0FEFD', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'u', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_065_NominalRotateUnderLeft(self):
        expected = {'cube': 'oooooogggggggggrrrrrrrrrbbbbbbbbbooowwwwwwwwwyyyyyyyyy', 'integrity': '72BD1F1E2822F5FE5A0EB5A75F6E926709A2FD455503016F549EC4E449F954B6', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'U', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_070_NominalRotateExtraParameters(self):
        expected = {'cube': 'oooooogggggggggrrrrrrrrrbbbbbbbbbooowwwwwwwwwyyyyyyyyy', 'integrity': '72BD1F1E2822F5FE5A0EB5A75F6E926709A2FD455503016F549EC4E449F954B6', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'U', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116', 'stuff': 'stuff'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test200_910_MissingCubeKey(self):
        expectedResult = {'status': 'error: missing cube key'}
        parms = {'side': 'f',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_920_MissingSideKey(self):
        expectedResult = {'status': 'error: missing side key'}
        parms = {'cube':'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_930_MissingIntegrityKey(self):
        expectedResult = {'status': 'error: missing side key'}
        parms = {'side': 'f',
                 'cube':'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_940_InvalidCubeKey(self):
        expectedResult = {'status': 'error: cube does not exactly have 9 of each element'}
        parms = {'side': 'f','cube': 'ggggggggggrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_950_InvalidSideKey(self):
        expectedResult = {'status': 'error: invalid side value'}
        parms = {'side': 'z','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_960_InvalidIntegrityKey(self):
        expectedResult = {'status': 'error: incorrect integrity value'}
        parms = {'side': 'f','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '547F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_010_NominalRotateFrontRight(self):
        expectedResult = {'rotatedCube': 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'f'
        actualResult = rotate._rotateFront(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_020_NominalRotateFrontLeft(self):
        expectedResult = {'rotatedCube': 'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'F'
        actualResult = rotate._rotateFront(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_030_NominalRotateBackRight(self):
        expectedResult = {'rotatedCube': 'oooooooooggyggyggyrrrrrrrrrwbbwbbwbbgggwwwwwwyyyyyybbb'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'b'
        actualResult = rotate._rotateBack(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_040_NominalRotateBackLeft(self):
        expectedResult = {'rotatedCube': 'oooooooooggwggwggwrrrrrrrrrybbybbybbbbbwwwwwwyyyyyyggg'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'B'
        actualResult = rotate._rotateBack(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test110_050_NominalRotateLeftRight(self):
        expectedResult = {'rotatedCube': 'woowoowoogggggggggrryrryrrybbbbbbbbbrwwrwwrwwoyyoyyoyy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'l'
        actualResult = rotate._rotateLeft(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_060_NominalRotateLeftLeft(self):
        expectedResult = {'rotatedCube': 'yooyooyoogggggggggrrwrrwrrwbbbbbbbbbowwowwowwryyryyryy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'L'
        actualResult = rotate._rotateLeft(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_070_NominalRotateRightRight(self):
        expectedResult = {'rotatedCube': 'ooyooyooygggggggggwrrwrrwrrbbbbbbbbbwwowwowwoyyryyryyr'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'r'
        actualResult = rotate._rotateRight(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_080_NominalRotateRightLeft(self):
        expectedResult = {'rotatedCube': 'oowoowoowgggggggggyrryrryrrbbbbbbbbbwwrwwrwwryyoyyoyyo'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'R'
        actualResult = rotate._rotateRight(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_085_NominalRotateTopRight(self):
        expectedResult = {'rotatedCube': 'gggoooooorrrggggggbbbrrrrrrooobbbbbbwwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 't'
        actualResult = rotate._rotateTop(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_090_NominalRotateTopLeft(self):
        expectedResult = {'rotatedCube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'T'
        actualResult = rotate._rotateTop(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test110_095_NominalRotateBottomRight(self):
        expectedResult = {'rotatedCube': 'oooooobbbggggggooorrrrrrgggbbbbbbrrrwwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'u'
        actualResult = rotate._rotateBottom(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_100_NominalRotateBottomLeft(self):
        expectedResult = {'rotatedCube': 'oooooogggggggggrrrrrrrrrbbbbbbbbbooowwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'U'
        actualResult = rotate._rotateBottom(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_910_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        rotateDirection = 'f'
        actualResult = rotate._rotateFront(rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_920_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        actualResult = rotate._rotateFront()
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_930_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        rotateDirection = 'f'
        actualResult = rotate._rotateBack(rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_940_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        actualResult = rotate._rotateBack()
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_950_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        rotateDirection = 'f'
        actualResult = rotate._rotateLeft(rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_960_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        actualResult = rotate._rotateLeft()
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_970_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        rotateDirection = 'f'
        actualResult = rotate._rotateRight(rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_975_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        actualResult = rotate._rotateRight()
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_980_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        rotateDirection = 'f'
        actualResult = rotate._rotateTop(rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_985_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        actualResult = rotate._rotateTop()
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_990_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        rotateDirection = 'f'
        actualResult = rotate._rotateBottom(rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_995_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        actualResult = rotate._rotateBottom()
        self.assertDictEqual(expectedResult, actualResult)