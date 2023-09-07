import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, ls, c, expected, expectedLst):
        '''Implementation of the test
            - ls         : list of strings
            - c          : a character
            - expected   : expected list
            - expectedLst: how the list has to be modified
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es51(ls, c)
        self.assertEqual(
            ls, expectedLst, f"The input list must become {expectedLst} instead of {ls}")
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")

    @data(
        (['Angelo', 'Andrea', 'Fabio', 'Francesco',
          'Lucio', 'Luca', 'Ugo'], 'a', 5, ['Lucio', 'Ugo']),
        (['Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca', 'Ugo'],
         'G', 2, ['Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca']),
        (['Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca', 'Ugo'],
         'f', 2, ['Angelo', 'Andrea', 'Lucio', 'Luca', 'Ugo'])
    )
    @unpack
    def test(self, ls, c, expected, expectedLst):
        return self.do_test(ls, c, expected, expectedLst)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
