import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, ftesto, expected):
        '''Test implementation
            - ftesto : text file containing the integers
            - expected : expected list
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es43(ftesto)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}/The result should be {expected} instead of {result}")


    @data(
        ('finteri1.txt', [10, 10, 15]),
        ('finteri2.txt', [7, 9, 9, 7, 3, 6]),
        ('finteri3.txt', [191, 163, 132, 98, 61, 21])
    )
    @unpack
    def test(self, ftesto, expected):
        return self.do_test(ftesto, expected)


# TESTS ARE PERFORMED IF YOU ARE PERFORMING program.py or by calling pytest in the directory
if __name__ == '__main__':
    Test.main()
