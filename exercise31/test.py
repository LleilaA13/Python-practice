import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, string, expected):
        '''Test implementation
            - string       : a string with words separated by spaces
            - expected      : expected string of integers
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es20(string)
        self.assertEqual(type(result),  str, "The result is not a string")
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")

    @data(
        ('Angelo Monti Andrea Sterbini e Angelo Spognardi', '48 63 39 88 5 48 93'),
        ('Aa bB Cc dD', '2 4 6 8')
    )
    @unpack
    def test(self, string, expected):
        return self.do_test(string, expected)

# The tests are performed either by running program.py or by calling pytest from the directory
if __name__ == '__main__':
    Test.main()
