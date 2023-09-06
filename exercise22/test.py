import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, img1, fcolors, img2, expected, expectedImg):
        '''Test implementation
            - img1          : input image
            - fcolors       : file with colors to change
            - img2          : where to save the image
            - expected      : expected number of modified pixels
            - expectedImg   : expected image
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es42(img1, fcolors, img2)
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")
        self.check_img_file(img2, expectedImg)


    @data(
        ('scacchiera.png', 'fcolori1.txt', 'out1.png', 7500, 'scacchieraOut1.png'),
        ('scacchiera.png', 'fcolori2.txt', 'out2.png', 4804, 'scacchieraOut2.png'),
        ('cubo.png', 'fcolori3.txt', 'out3.png', 10620, 'cuboOut.png')
    )
    @unpack
    def test(self, img1, fcolors, img2, expected, expectedImg):
        return self.do_test(img1, fcolors, img2, expected, expectedImg)


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
