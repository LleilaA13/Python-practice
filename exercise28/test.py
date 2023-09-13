import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, fimm,fimm1,h1,w1, expected, expectedImg):
        result   = program.ex4(fimm,fimm1,h1,w1)
        self.assertEqual(result, expected, "Il valore restituito {result} non e' quello atteso {expected}/The result should be {expected} instead of {result}")
        self.check_img_file(fimm1, expectedImg)
    
    def test_1(self):
        ''' \nFirst test of the function es8 where the cube.png image is passed with h1=w1= 2 
        and created the image test8_1.png which must match the one in RisTest1.png'''
        #return self.do_test('cubo.png', 'test8_1.png', 2, 2, (185, 182, 187), 'RisTest1.png')
        return self.do_test('cubo.png', 'test8_1.png', 2, 2, (255, 255, 255), 'RisTest1.png')

    def test_2(self):
        ''' \nSecond test of the es8 function where the photoBN.png image is passed with h1=2 and w1=3 
        and created the image test8_2.png which must match the one in RisTest2.png'''
        #return self.do_test('fotoBN.png', 'test8_2.png', 2, 3, (255, 255, 255), 'RisTest2.png')
        return self.do_test('fotoBN.png', 'test8_2.png', 2, 3, (0, 0, 0), 'RisTest2.png')

    def test_3(self):
        ''' \nTThird test of the es8 function where the cube.png image is passed with h=1 and w=3 
        and created the image test8_3.png which must match the one in RisTest8_1.png'''
        #return self.do_test('cubo.png', 'test8_3.png', 1, 3, (185, 182, 187), 'RisTest3.png')
        return self.do_test('cubo.png', 'test8_3.png', 1, 3, (255, 255, 255), 'RisTest3.png')

if __name__ == "__main__":
    Test.main()
