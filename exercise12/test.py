
# Test example

# NEEDED IMPORTS
import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive
import treenode

import program 

@ddt
class Test(testlib.TestCase):

    def do_test(self, level, expected):
        '''Test implementation
            - level       : tree level
            - expected      : expected tree
        '''
        try:
            isrecursive.decorate_module(program)
            program.es12(level)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es12(level)
        self.assertEqual(treenode.toLista(result), expected, f"Result must be {expected} instead of {result}, input k={level}")

    @data(  
            (1, [3,[[1,[]],[2,[]]]]),
            (2, [10,[[3,[[1,[]],[2,[]]]],[7,[[3,[]],[4,[]]]]]]),
            (3, [36,[[10,[[3,[[1,[]],[2,[]]]],[7,[[3,[]],[4,[]]]]]],[26,[[11,[[5,[]],[6,[]]]],[15,[[7,[]],[8,[]]]]]]]])
        )
    @unpack
    def test(self, level, expected):
        return self.do_test(level, expected)

if __name__ == '__main__':
    Test.main()

