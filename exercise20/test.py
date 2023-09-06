import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, s, k, expected):
        '''
        Implementation of the test
            - s : string of digits
            - k : integer> 0
            - expected : awaited sorted list
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es50(s, k)
        self.assertEqual(type(result), list, "The result is not a list")
        self.assertEqual(
            result, expected, f"The restult must be {expected} intead of {result}")

    @data(
        ('9135918246556', 3, ['359', '246', '135']),
        ('1234123412341234', 3, ['234', '123']),
        ('987654321', 3, [])
    )
    @unpack
    def test(self, s, k, expected):
        return self.do_test(s, k, expected)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py  or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
