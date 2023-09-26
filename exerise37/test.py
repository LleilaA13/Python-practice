import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, fname, expected):
        '''Test implementation
            - fname : file containing the sequence of integers
            - expected : the expected number
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.ex41(fname)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}/The result should be {expected} instead of {result}")

    @data(
        ('fsequenza1.txt', 2),
        ('fsequenza2.txt', 7)
    )
    @unpack
    def test(self, fname, expected):
        return self.do_test(fname, expected)


# The tests can be performed running program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
