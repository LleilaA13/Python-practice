import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, path, ext, par, expected):
        '''Test implementation
            - path : path of the directory from which to start with the search
            - ext : file extensions not to be searched
            - par : list of words to search
            - expected : expected dictionary
        '''
        try:
            isrecursive.decorate_module(program)
            program.es70(path, ext, par)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es70(path, ext, par)
        self.assertEqual(type(result), dict,
                         "Il risultato non è un dizionario/The returned value is not a dictionary")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}/The returned value should be {expected} instead of {result}")

    @data(
        ('t3', ['txt', 'testo'], ['PaperIno', 'MINNIE', 'EdI'],
         {'paperino': 2, 'minnie': 2, 'edi': 1, }),
        ('t3', ['testo'], ['Paperino', 'Pippo', 'Pluto', 'Clarabella', 'Orazio'], {
         'paperino': 3, 'pippo': 1, 'clarabella': 1, 'orazio': 1, })
    )
    @unpack
    def test(self, path, ext, par, expected):
        return self.do_test(path, ext, par, expected)


# TESTS ARE PERFORMED IF YOU ARE RUNNING program.py or by calling pytest in the directory
if __name__ == '__main__':
    Test.main()
