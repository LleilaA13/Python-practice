import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, tabella, expected, expectedTab):
        '''Implementation of the test
            - table : table of integers in the form of a list of lists
            - expected : list
            - expectedTab : table modified with '*'.
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es56(tabella)
        self.assertEqual(type(result), list, "The result is not a list")
        self.assertEqual(
            result, expected, f"The result should be {expected} instead of {result}")
        self.assertEqual(
            tabella, expectedTab, f"The table should be changed in {expected} intead of {result}")


    @data(
        ([[3, 2, 1, 3], [2, 1, 3, 5], [1, 3, 2, 1]], [1, 3], [
         ['*', 2, '*', '*'], [2, '*', '*', 5], ['*', '*', 2, '*']]),
        ([[10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10]], [10], [
         ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                                         11, 12], [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                                                           13, 14, 15, 16], [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']])
    )
    @unpack
    def test(self, tabella, expected, expectedTab):
        return self.do_test(tabella, expected, expectedTab)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or by calling pytest in the directory
if __name__ == '__main__':
    Test.main()
