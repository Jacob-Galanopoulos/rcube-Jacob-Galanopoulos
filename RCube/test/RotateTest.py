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
        expectedResult = {'status': 'rotated', 
                          'cube': 'woowoowoogggggggggrryrryrrybbbbbbbbbrwwrwwrwwoyyoyyoyy', 
                          'integrity': '50FAFE62BF3BB0CF259572E7992AC528A4DFEE0BEB8B0F4EAC768E68262262D1'}
        parms = {'side': 'l','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_035_NominalRotateLeftLeft(self):
        expectedResult = {'status': 'rotated', 
                          'cube': 'yooyooyoogggggggggrrwrrwrrwbbbbbbbbbowwowwowwryyryyryy', 
                          'integrity': 'C323A402B51C4594101DB8EF9DD2808100987459684AB6C7B433D4A54D3DD605'}
        parms = {'side': 'L','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_040_NominalRotateRightRight(self):
        expectedResult = {'status': 'rotated',
                          'cube': 'ooyooyooygggggggggrwwrwwrwwbbbbbbbbbwwwwwwooorrryyyyyy', 
                          'integrity': 'E12EB8E84A67626CCC8AC3DDFB61D714B6BD7624ED08B9CAE2789FFE016276AF'}
        parms = {'side': 'r','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_045_NominalRotateRightLeft(self):
        expectedResult = {'status': 'rotated', 
                          'cube': 'oowoowoowgggggggggyrryrryrrbbbbbbbbbwwwwwwrrroooyyyyyy', 
                          'integrity': 'B621AC498B7852185B388A6F8A165D7D8086ABBEC7240ED2EF82CD41B34179A8'}
        parms = {'side': 'R','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_050_NominalRotateTopRight(self):
        expectedResult = {'status': 'rotated', 
                          'cube': 'gggoooooorrrggggggbbbrrrrrrooobbbbbbwwwwwwwwwyyyyyyyyy', 
                          'integrity': 'E03151E1977723626C4896A60618759D4821F62EAF753955D97B8B70DDA2DE0B'}
        parms = {'side': 't','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_055_NominalRotateTopLeft(self):
        expectedResult = {'status': 'rotated', 
                          'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy', 
                          'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        parms = {'side': 'T','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_060_NominalRotateUnderRight(self):
        expectedResult = {'status': 'rotated',
                          'cube': 'oooooobbbggggggooorrrrrrgggbbbbbbrrrwwwwwwwwwyyyyyyyyy', 
                          'integrity': 'BA29EA321B8E33BF21FFCFFBA10A0F81509AEC5208BC37179A4C613093B0FEFD'}
        parms = {'side': 'u','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_065_NominalRotateUnderLeft(self):
        expectedResult = {'status': 'rotated', 
                          'cube': 'oooooogggggggggrrrrrrrrrbbbbbbbbbooowwwwwwwwwyyyyyyyyy', 
                          'integrity': '72BD1F1E2822F5FE5A0EB5A75F6E926709A2FD455503016F549EC4E449F954B6'}
        parms = {'side': 'U','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_070_NominalRotateExtraParameters(self):
        expectedResult = {'status':'rotated', 
                          'cube':'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy', 
                          'integrity':'0F3BDBE402C16D85756959CDEE1649281296A8507CDDF29EC328C72CC758DA28'}
        parms = {'side': 'f','cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF',
                 'stuff': 'stuff'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
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
        
    def test110_010_NominalFrontBackRotate_f(self):
        expectedResult = {'rotatedCube': 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'f'
        actualResult = rotate._execFrontAndBack(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_020_NominalFrontBackRotate_F(self):
        expectedResult = {'rotatedCube': 'oooooooooyggyggyggrrrrrrrrrbbwbbwbbwwwwwwwgggbbbyyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'F'
        actualResult = rotate._execFrontAndBack(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_030_NominalFrontBackRotate_b(self):
        expectedResult = {'rotatedCube': 'oooooooooggyggyggyrrrrrrrrrwbbwbbwbbgggwwwwwwyyyyyybbb'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'b'
        actualResult = rotate._execFrontAndBack(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_040_NominalFrontBackRotate_B(self):
        expectedResult = {'rotatedCube': 'oooooooooggwggwggwrrrrrrrrrybbybbybbbbbwwwwwwyyyyyyggg'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'B'
        actualResult = rotate._execFrontAndBack(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_910_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        rotateDirection = 'f'
        actualResult = rotate._execFrontAndBack(rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_920_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        actualResult = rotate._execFrontAndBack()
        self.assertDictEqual(expectedResult, actualResult)
        
    def test120_010_NominalLeftRightRotate_l(self):
        expectedResult = {'rotatedCube': 'woowoowoogggggggggrryrryrrybbbbbbbbbrwwrwwrwwoyyoyyoyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'l'
        actualResult = rotate._execLeftAndRight(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test120_020_NominalLeftRightRotate_L(self):
        expectedResult = {'rotatedCube': 'yooyooyoogggggggggrrwrrwrrwbbbbbbbbbowwowwowwryyryyryy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'L'
        actualResult = rotate._execLeftAndRight(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test120_030_NominalLeftRightRotate_r(self):
        expectedResult = {'rotatedCube': 'ooyooyooygggggggggrwwrwwrwwbbbbbbbbbwwwwwwooorrryyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'r'
        actualResult = rotate._execLeftAndRight(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test120_040_NominalLeftRightRotate_R(self):
        expectedResult = {'rotatedCube': 'oowoowoowgggggggggyrryrryrrbbbbbbbbbwwwwwwrrroooyyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'R'
        actualResult = rotate._execLeftAndRight(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test220_910_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        rotateDirection = 'r'
        actualResult = rotate._execLeftAndRight(rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test220_920_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        actualResult = rotate._execLeftAndRight()
        self.assertDictEqual(expectedResult, actualResult)
        
    def test130_010_NominalTopBottomRotate_t(self):
        expectedResult = {'rotatedCube': 'gggoooooorrrggggggbbbrrrrrrooobbbbbbwwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 't'
        actualResult = rotate._execTopAndBottom(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test130_020_NominalTopBottomRotate_T(self):
        expectedResult = {'rotatedCube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'T'
        actualResult = rotate._execTopAndBottom(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test130_030_NominalTopBottomRotate_u(self):
        expectedResult = {'rotatedCube': 'oooooobbbggggggooorrrrrrgggbbbbbbrrrwwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'u'
        actualResult = rotate._execTopAndBottom(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test130_040_NominalTopBottomRotate_U(self):
        expectedResult = {'rotatedCube': 'oooooogggggggggrrrrrrrrrbbbbbbbbbooowwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'U'
        actualResult = rotate._execTopAndBottom(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test230_910_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        rotateDirection = 't'
        actualResult = rotate._execTopAndBottom(rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test230_920_MissingcubeFaces(self):
        expectedResult = {'error': 'missing input'}
        actualResult = rotate._execTopAndBottom()
        self.assertDictEqual(expectedResult, actualResult)