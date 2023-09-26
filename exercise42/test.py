import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, l, expected):
        '''Implementation of the test
            - l : list of integers
            - expected : string
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es64(l)
        self.assertEqual(type(result), str, "The result is not a string")
        self.assertEqual(
            result, expected, f"The result should be {expected} instead of {result}")

    @data(
        ([1, 23, 2000], "    2\n    0\n  2 0\n1 3 0"),
        ([1, 23, 2000, 900002], "      9\n      0\n    2 0\n    0 0\n  2 0 0\n1 3 0 2"),
        ([8000022233, 1, 23, 2000, 900002],
         "8        \n0        \n0        \n0        \n0       9\n2       0\n2     2 0\n2     0 0\n3   2 0 0\n3 1 3 0 2")
    )
    @unpack
    def test(self, l, expected, ):
        return self.do_test(l, expected)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or by calling pytest in the directory
if __name__ == '__main__':
    Test.main()
