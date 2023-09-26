import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):
    def do_test(self, set1, set2, expected):
        with    self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es3(set1, set2)

        self.assertEqual(result, expected, "the answer is not correct")

    def test_1(self):
        ''' \nFirst test for function ex3 with set1={2,4,5,6,8,9} and set2={5,15,19,25}.'''
        ls = [(2, 4, 9), (2, 5, 8), (4, 5, 6), (2, 8, 9), (4, 6, 9), (5, 6, 8)]
        set1 = {2,4,5,6,8,9}
        set2 = {5,15,19,25}
        return self.do_test(set1, set2, ls)

    def test_2(self):
        ''' \nSecond test for function ex3 with set1={1,2,4,5,6,8,9} and set2={16,18}.'''
        ls = [(1, 6, 9), (2, 5, 9), (2, 6, 8), (1, 8, 9), (4, 5, 9), (4, 6, 8)]
        set1 = {1,2,4,5,6,8,9}
        set2 = {16,18}
        return self.do_test(set1, set2, ls)

    def test_3(self):
        ''' \nThird test for function ex3 with set1={2,4,6,8,10,12,14,16,18,20} and set2={5,15,19,25}.'''
        ls = [(2, 4, 14), (2, 6, 12), (2, 8, 10), (4, 6, 10), (2, 14, 20), (2, 16, 18),
            (4, 12, 20), (4, 14, 18), (6, 10, 20), (6, 12, 18), (6, 14, 16), (8, 10, 18),
            (8, 12, 16), (10, 12, 14), (2, 18, 20), (4, 16, 20), (6, 14, 20), (6, 16, 18),
            (8, 12, 20), (8, 14, 18), (10, 12, 18), (10, 14, 16)]
        set1 = {2,4,6,8,10,12,14,16,18,20}
        set2 = {20,40,36}
        return self.do_test(set1, set2, ls)

if __name__ == "__main__":
    Test.main()
