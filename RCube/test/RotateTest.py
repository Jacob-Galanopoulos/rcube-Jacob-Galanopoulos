'''
Created on Nov 17, 2020

@author: jakeg
'''
import unittest
import RCube.rotate as rotate

class Test(unittest.TestCase):
    
    def test100_010_Nominal_f(self):
        expected = {'cube': 'ooooooooowggwggwggrrrrrrrrrbbybbybbywwwwwwbbbgggyyyyyy', 'integrity': '8449F88B8986E08AA51135B292FE968A6EB10050FC880348486EF853BC10A60B', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'f', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_015_Nominal_F(self):
        expected = {'cube': 'oooooooooyggyggyggrrrrrrrrrbbwbbwbbwwwwwwwgggbbbyyyyyy', 'integrity': '0725FE3DE940D22412488858679E49038627A91F615FE641A3CA897B08F14C09', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'F', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_020_Nominal_b(self):
        expected = {'cube': 'oooooooooggyggyggyrrrrrrrrrwbbwbbwbbgggwwwwwwyyyyyybbb', 'integrity': 'CF7F7CA7F091782686E19721F50C78B9D46408A00A992E414D8B2D33C999D9B9', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'b', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_025_Nominal_B(self):
        expected = {'cube': 'oooooooooggwggwggwrrrrrrrrrybbybbybbbbbwwwwwwyyyyyyggg', 'integrity': '0734348E61CFFD1BFDDD3989819FC035ED5128230E2A04B4C1346BE1086934E1', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'B', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_030_Nominal_l(self):
        expected = {'cube': 'woowoowoogggggggggrryrryrrybbbbbbbbbrwwrwwrwwoyyoyyoyy', 'integrity': '50FAFE62BF3BB0CF259572E7992AC528A4DFEE0BEB8B0F4EAC768E68262262D1', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'l', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_035_Nominal_L(self):
        expected = {'cube': 'yooyooyoogggggggggrrwrrwrrwbbbbbbbbbowwowwowwryyryyryy', 'integrity': 'C323A402B51C4594101DB8EF9DD2808100987459684AB6C7B433D4A54D3DD605', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'L', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_040_Nominal_r(self):
        expected = {'cube': 'ooyooyooygggggggggwrrwrrwrrbbbbbbbbbwwowwowwoyyryyryyr', 'integrity': '84DF9D66A7A22B043BD6B77947DD548ADA1A74091E8F544E31C1DB2B8F4FE5FB', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'r', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_045_Nominal_R(self):
        expected = {'cube': 'oowoowoowgggggggggyrryrryrrbbbbbbbbbwwrwwrwwryyoyyoyyo', 'integrity': '343D9B61D1F3FA8206CC7569F9D64A2A8B796E8487A1234CC5FCABD44BEDE263', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'R', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_050_Nominal_t(self):
        expected = {'cube': 'gggoooooorrrggggggbbbrrrrrrooobbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'E03151E1977723626C4896A60618759D4821F62EAF753955D97B8B70DDA2DE0B', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 't', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_055_Nominal_T(self):
        expected = {'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'T', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_060_Nominal_u(self):
        expected = {'cube': 'oooooobbbggggggooorrrrrrgggbbbbbbrrrwwwwwwwwwyyyyyyyyy', 'integrity': 'BA29EA321B8E33BF21FFCFFBA10A0F81509AEC5208BC37179A4C613093B0FEFD', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'u', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_065_Nominal_U(self):
        expected = {'cube': 'oooooogggggggggrrrrrrrrrbbbbbbbbbooowwwwwwwwwyyyyyyyyy', 'integrity': '72BD1F1E2822F5FE5A0EB5A75F6E926709A2FD455503016F549EC4E449F954B6', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'U', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test100_070_Nominal_Extra_Params(self):
        expected = {'cube': 'oooooogggggggggrrrrrrrrrbbbbbbbbbooowwwwwwwwwyyyyyyyyy', 'integrity': '72BD1F1E2822F5FE5A0EB5A75F6E926709A2FD455503016F549EC4E449F954B6', 'status': 'rotated'}
        parms = {'op': 'rotate', 'cube': 'ooooooooogggggggggrrrrrrrrrbbbbbbbbbwwwwwwwwwyyyyyyyyy', 'side': 'U', 'integrity': '26BF4FF19CDC0D418DF7317E5F8EEF32C21C5B8CBDA492BDC1BF536F34421116', 'stuff': 'stuff'}
        actual = rotate._rotate(parms)
        self.assertEqual(expected, actual)
        
    def test200_910_Missing_Cube_Key(self):
        expectedResult = {'status': 'error: missing cube key'}
        parms = {'side': 'f',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_920_Missing_Side_Key(self):
        expectedResult = {'status': 'error: missing side key'}
        parms = {'cube':'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy',
                 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_930_Missing_Integrity_Key(self):
        expectedResult = {'status': 'error: missing integrity key'}
        parms = {'side': 'f',
                 'cube':'gggggggggbbbbbbbbbyyyyyyyyyrrrrrrrrriiiiiiiiisssssssss'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_940_Invalid_Cube_Key(self):
        expectedResult = {'status': 'error: incorrect integrity value'}
        parms = {'side': 'f','cube': 'gggggggggbbbbbbbbbyyyyyyyyyrrrrrrrrriiiiiiiiissssssssss',
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
        parms = {'side': 'f','cube': 'gggggggggbbbbbbbbbyyyyyyyyyrrrrrrrrriiiiiiiiisssssssss',
                 'integrity': '547F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_010_Nominal_rotateFront_f(self):
        expectedResult = {'rotatedCube': 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'f'
        actualResult = rotate._rotateFront(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_020_Nominal_rotateFront_F(self):
        expectedResult = {'rotatedCube': 'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy'}
        cubeFaces = ['ggggggggg','rrrrrrrrr','bbbbbbbbb','ooooooooo','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'F'
        actualResult = rotate._rotateFront(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_030_Nominal_rotateBack_b(self):
        expectedResult = {'rotatedCube': 'oooooooooggyggyggyrrrrrrrrrwbbwbbwbbgggwwwwwwyyyyyybbb'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'b'
        actualResult = rotate._rotateBack(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_040_Nominal_rotateBack_B(self):
        expectedResult = {'rotatedCube': 'oooooooooggwggwggwrrrrrrrrrybbybbybbbbbwwwwwwyyyyyyggg'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'B'
        actualResult = rotate._rotateBack(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test110_050_Nominal_rotateLeft_l(self):
        expectedResult = {'rotatedCube': 'woowoowoogggggggggrryrryrrybbbbbbbbbrwwrwwrwwoyyoyyoyy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'l'
        actualResult = rotate._rotateLeft(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_060_Nominal_rotateLeft_L(self):
        expectedResult = {'rotatedCube': 'yooyooyoogggggggggrrwrrwrrwbbbbbbbbbowwowwowwryyryyryy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'L'
        actualResult = rotate._rotateLeft(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_070_Nominal_rotateRight_r(self):
        expectedResult = {'rotatedCube': 'ooyooyooygggggggggwrrwrrwrrbbbbbbbbbwwowwowwoyyryyryyr'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'r'
        actualResult = rotate._rotateRight(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_080_Nomina_rotateRight_R(self):
        expectedResult = {'rotatedCube': 'oowoowoowgggggggggyrryrryrrbbbbbbbbbwwrwwrwwryyoyyoyyo'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'R'
        actualResult = rotate._rotateRight(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_085_Nominal_rotateTop_t(self):
        expectedResult = {'rotatedCube': 'gggoooooorrrggggggbbbrrrrrrooobbbbbbwwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 't'
        actualResult = rotate._rotateTop(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_090_Nominal_rotateTop_T(self):
        expectedResult = {'rotatedCube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'T'
        actualResult = rotate._rotateTop(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test110_095_Nominal_rotateBottom_u(self):
        expectedResult = {'rotatedCube': 'oooooobbbggggggooorrrrrrgggbbbbbbrrrwwwwwwwwwyyyyyyyyy'}
        cubeFaces = ['ooooooooo','ggggggggg','rrrrrrrrr','bbbbbbbbb','wwwwwwwww','yyyyyyyyy']
        rotateDirection = 'u'
        actualResult = rotate._rotateBottom(cubeFaces, rotateDirection)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_100_Nominal_rotateBottom_U(self):
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