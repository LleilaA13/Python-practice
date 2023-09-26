import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, directory, strSet, expected):
        '''Test implementation
            - directory     : directory where to search for files
            - strSet        : set of strings to look for
            - expected      : Expected word dictionary
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es35(directory, strSet)
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")

    @data(
        ('A', {'a', 'b', 'c', 'd'}, {'a': (5, 3), 'c': (3, 2), 'b': (1, 1)}),
        ('A', {'bb', 'x', 'y', 'z'}, {'x': (1, 1), 'z': (5, 2)})
    )
    @unpack
    def test(self, directory, strSet, expected):
        return self.do_test(directory, strSet, expected)


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
