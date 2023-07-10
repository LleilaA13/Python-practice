import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, dirname, extensions, expected):
        '''Implementazione del test
            - dirname      : pathname of a directory to explore
            - extensions   : list of string with extensions to search for
            - expected     : expected dictionary
        '''

        try:
            isrecursive.decorate_module(program)
            program.es68(dirname, extensions)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es68(dirname, extensions)
        self.assertEqual(type(result), dict, "Il risultato non è un dizionario/The returned value is not a dictionary")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}/The returned value should be {expected} instead of {result}")

    @data(
        ('t1', ['txt', 'jpg'], {'txt': 3, 'jpg': 1, }),
        ('t2', ['txt', 'jpg', 'png', 'testo', 'ttt'],
         {'png': 2, 'txt': 5, 'jpg': 2})
    )
    @unpack
    def test(self, dirname, extensions, expected):
        return self.do_test(dirname, extensions, expected)


# TESTS can be performed running program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
