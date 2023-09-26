import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, expected):
        '''Test implementation
            - f1 : json file with the list of integers
            - expected : expected tuple list
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.ex32(f1)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}/The result should be {expected} instead of {result}")

    @data(
        ('file1.json', [(2, 0), (0, 6), (4, 4), (1, 0), (7, 16)]), 
        ('file2.json', [(6, 8), (15, 0), (0, 0), (0, 10), (25, 20)])
    )
    @unpack
    def test(self, f1, expected):
        return self.do_test(f1, expected)


# The tests can be performed running program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
