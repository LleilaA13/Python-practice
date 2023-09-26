import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):
    
    def do_test(self, ls, ftext, expected, expectedLs):
        '''Implementation of the test:
            - ls: list of strings
            - ftext: path to a text file
            - expected: expected result
            - expectedLs: expected modified list
        '''
        with    self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result   = program.es2(ls, ftext)
        self.assertEqual(result, expected, "The answer is not correct")
        self.assertEqual(ls, expectedLs, "The ls list has not been modified correctly")
    
    def test_1(self):
        ''' \nFirst es2 function test with ls=['b', 'abba', 'babc','ccc', 'bba', 'bb' ]
        and text file 'ft1.txt' '''
        ls = ['b', 'abba', 'babc','ccc', 'bba', 'bb' ]
        res_ls = ['b', 'babc', 'bba', 'bb']
        return self.do_test(ls, "ft1.txt", 2, res_ls)

    def test_2(self):
        ''' \nSecond es2 function test with ls=[ 'bab', 'abba','bc', 'cc', 'ccc' ] and  
        text file 'ft1.txt' '''
        ls = [ 'bab', 'abba','bc', 'cc', 'ccc' ]
        res_ls = []
        return self.do_test(ls, "ft1.txt", 5, res_ls)
    
    def test_3(self):
        ''' \nThird es2 function test with ls=['b', 'ab', 'ba', 'b', 'c' 'c' 'cc']
        and  text file 'ft1.txt' '''
        ls = ['b', 'ab', 'ba', 'b', 'c' 'c' 'cc']
        res_ls = ['b', 'ab', 'ba', 'b', 'cccc']
        return self.do_test(ls, "ft1.txt", 0, res_ls)

if __name__ == "__main__":
    Test.main()
