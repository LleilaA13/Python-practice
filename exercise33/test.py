import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, table1, table2, col, expected, expectedTab):
        '''Test implementation
            - table1      : table in the form of a list of dictionaries
            - table2      : table in the form of a list of dictionaries
            - col           : column name 
            - expected      : expected number of rows added
            - expectedTab   : expected table
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es29(table1, table2, col)
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")
        self.assertEqual(table1, expectedTab,"Table1 has not been modified correctly")

    @data(
        ([{'C1': 1, 'C2': 'x'},{'C1': 3, 'C2': 'a'},{'C1': 4, 'C2':'a'},{'C1': 5, 'C2': 'a'},{'C1': 7, 'C2': 'b'}], [{'C1': 2, 'C2': 'a'},{'C1': 3, 'C2': 'b'},{'C1': 5, 'C2':'a'},{'C1': 6, 'C2': 'b'},{'C1': 7, 'C2': 'a'}], 'C1', 2, [{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'}, {'C1': 3,'C2':'a'},{'C1': 4, 'C2': 'a'},{'C1': 5, 'C2': 'a'},{'C1': 6, 'C2': 'b'}, {'C1': 7, 'C2':'b'}]),
        ([{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'},{'C1': 3, 'C2':'a'}], [{'C1': 3, 'C2': 'b'},{'C1': 4, 'C2': 'b'},{'C1': 5, 'C2':'a'}], 'C1', 2, [{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'}, {'C1': 3,'C2':'a'},{'C1': 4, 'C2': 'b'}, {'C1': 5, 'C2':'a'}]),
        ([{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'},{'C1': 3, 'C2':'a'}], [{'C1': 1, 'C2': 'y'},{'C1': 2, 'C2': 'z'},{'C1': 3, 'C2':'t'}], 'C1', 0, [{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'},{'C1': 3, 'C2':'a'}])
    )
    @unpack
    def test(self, table1, table2, col, expected, expectedTab):
        return self.do_test(table1, table2, col, expected, expectedTab)


# The tests are performed either by running program.py or by calling pytest from the directory
if __name__ == '__main__':
    Test.main()
