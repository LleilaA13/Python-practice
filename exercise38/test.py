import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, sel, m, n, matr, expected, expectedMatr):
        '''Implementation of the test
            - sel : character between 'r' and 'c'.
            - m : integer, row or column number
            - n : integer, row or column number
            - matr : matrix of integers
            - expected : tuple (min, max) 
            - expectedMatr : modified matrix 
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es55(sel, m, n, matr)
        self.assertEqual(type(result), tuple, "The result is not a tuple")
        self.assertEqual(
            result, expected, f"The result should be {expected} instead of {result}")
        self.assertEqual(
            matr, expectedMatr, f"The matrix must become {expectedMatr} instead of {matr}")

    @data(
        ('c', 0, 2, [[2, 0, -4], [5, 10, 20], [5, 1, -1]],
         (-4, 20), [[-4, 0, 2], [20, 10, 5], [-1, 1, 5]]),
        ('r', 0, 2, [[2, 0, -4, -20], [5, 100, 20, 3], [5, 1, -1, 1]],
         (-20, 100), [[5, 1, -1, 1], [5, 100, 20, 3], [2, 0, -4, -20]])
    )
    @unpack
    def test(self, sel, m, n, matr, expected, expectedMatr):
        return self.do_test(sel, m, n, matr, expected, expectedMatr)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or by calling pytest in the directory
if __name__ == '__main__':
    Test.main()
