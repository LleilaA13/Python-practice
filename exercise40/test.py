import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, lista, expected, expectedLst):
        '''Implementation of the test
            - list : list of strings with characters in {'N', 'S', 'E', 'O'}.
            - expected : number of characters
            - expectedLst : list of integer
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es58(lista)
        self.assertEqual(type(result), int, "The result is not an integer")
        self.assertEqual(
            result, expected, f"The result should be {expected} instead of {result}")
        self.assertEqual(
            lista, expectedLst, f"The list should become {expectedLst} instead of {lista}")

    @data(
        (['NS', 'NEESS', 'NNOOO', 'NNEESSO'], 19, [0, 3, 5, 1]),
        (['NSO', 'NEESSO', 'NNOOOO', 'NNEESSOO'], 23, [1, 2, 6, 0])
    )
    @unpack
    def test(self, lista, expected, expectedLst):
        return self.do_test(lista, expected, expectedLst)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or by calling pytest in the directoryif __name__ == '__main__':
    Test.main()
