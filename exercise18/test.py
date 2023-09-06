import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, matrix, expected, expectedMtr):
        '''Implementation of the test
            - matrix : matrix of integers in the form of a list of lists
            - expected : new matrix of integers
            - expectedMtr : the input matrix must not change
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es62(matrix)
        self.assertEqual(
            result, expected, f"The result should be {expected} instead of {result}")
        self.assertEqual(
            matrix, expectedMtr, f"The original matrix {expectedMtr} has been modified in {matrix}")

    @data(
        ([[2, 0, -4], [5, 10, 20], [5, 1, -1]],
         [[5, 10, 20], [2, 0, -4], [5, 1, -1]]),
        ([[2, 0, -4], [5, 10, 10], [25, 1, -1]],
         [[-1, 1, 25], [10, 10, 5], [-4, 0, 2]]),
        ([[52, 0,  -4, 19], [5, 10, 10, 52], [25, 1, -95, -80], [-95, 14, 17, 42]],
         [[19, 0,  -4, 52], [42, 14, 17, -95], [-80, 1, -95, 25], [52, 10, 10, 5]])
    )
    @unpack
    def test(self, matrix, expected):
        return self.do_test(matrix, expected, matrix)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or by calling pytest in the directory
if __name__ == '__main__':
    Test.main()
