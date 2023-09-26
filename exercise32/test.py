import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, matrix, expected, expectedMtr):
        '''Test implementation
            - matrix       : character matrix
            - expected      : expected character matrix 
            - expectedMtr   : matrix of characters equal to the input one
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es21(matrix)
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")
        self.assertEqual(
            matrix, expectedMtr, f"the matrix {expectedMtr} has been modified to {matrix}")

    @data(
        ([['q','s','g','g'],['b','a','m','f'],['a','b','n','z']], [['a', 'a', 'g', 'f'], ['b', 'b', 'm', 'g'], ['q', 's', 'n', 'z']], [['q','s','g','g'],['b','a','m','f'],['a','b','n','z']]),
        ([['d','c','a','d'],['c','d','d','a'],['b','a','c','b'],['a','b','b','c']], [['a','a','a','a'], ['b','b','b','b'], ['c','c','c','c'], ['d','d','d','d']], [['d','c','a','d'],['c','d','d','a'],['b','a','c','b'],['a','b','b','c']])
    )
    @unpack
    def test(self, matrix, expected, expectedMtr):
        return self.do_test(matrix, expected, expectedMtr)


# The tests are performed either by running program.py or by calling pytest from the directory
if __name__ == '__main__':
    Test.main()
