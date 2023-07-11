
# Test example

# NEEDED IMPORTS
import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, file, k, expected):
        '''Test implementation
            - file: text file
            - k: integer 
            - expected      : expected number of trees in the forest
        '''

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es10(file, k)
        self.assertEqual(type(result), str, "The result is not a String")
        self.assertEqual(result, expected, f"The result must be {expected} instead of {result}")

    @data(  
            ('ft9.txt', 3, 'are'),
            ('ft9.txt', 6, 'figlia'),
            ('ft9.txt', 10, '')
            )
    @unpack
    def test(self, file, k, expected):
        return self.do_test(file, k, expected)

if __name__ == '__main__':
    Test.main()

