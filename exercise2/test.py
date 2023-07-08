import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, table, column, value, expected, expectedTab):
        '''Test implementation
            - table       : table in the form of a list of dictionaries
            - column       : column name
            - value        : value to compare
            - expected      : expected number of rows deleted
            - expectedTab   : expected modified table
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es27(table, column, value)
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")
        self.assertEqual(
            table, expectedTab, f"The result must be {expectedTab} instead of {table}")

    @data(
        ([{'C1': 2, 'C2': 1, 'C3': 'd'}, {'C1': 4, 'C2': 7, 'C3': 'a'}, {'C1': 6, 'C2': 1, 'C3': 'b'}, {
         'C1': 8, 'C2': 3, 'C3': 'c'}], 'C2', 1, 2, [{'C1': 2, 'C3': 'd'}, {'C1': 6, 'C3': 'b'}]),
        ([{'C1': 2, 'C2': 1, 'C3': 'd'}, {'C1': 4, 'C2': 7, 'C3': 'a'}, {
         'C1': 6, 'C2': 1, 'C3': 'b'}, {'C1': 8, 'C2': 3, 'C3': 'c'}], 'C1', 3, 4, [])
    )
    @unpack
    def test(self, table, column, value, expected, expectedTab):
        return self.do_test(table, column, value, expected, expectedTab)


# The tests are performed either by running program.py or by calling pytest from the directory
if __name__ == '__main__':
    Test.main()
