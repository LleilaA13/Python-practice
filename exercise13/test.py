
# Esempio di test

# IMPORT NECESSARI
import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, textfile, expected):
        '''Test implementation
            - textfile : input text file
            - expected : expected number of trees in the forest
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.ex11(textfile)
        self.assertEqual(type(result), dict, "Il risultato non è un dizionario/The returned value is not a dictionary")
        self.assertEqual(result, expected, f"Il risultato deve essere {expected} invece che {result}/The result should be {expected} instead of {result}")

    @data(  
            ('ft10a.txt',{'prt': ['parto', 'porta'], 'r': ['era', 'ora'], 'pr': ['arpia', 'arpa'], 'cs': ['casa', 'cosa'], 'fll': ['follia', 'fallo', 'folla'], 'rt': ['otre', 'tre'], 'lp': ['piolo', 'polo']}),
            ('ft10b.txt',{'bcd': ['aabeeciidoo', 'abeciido', 'bcduuu', 'buucd', 'uubcd'], 'stz': ['azasata', 'uzusutu', 'ezeset'], '': ['aioa', 'aio', 'oio'], 'gh': ['aghaeiou', 'ghuuuuuu', 'aeiogh', 'agaaah', 'uguuuh'], 'c': ['cuuu', 'oco', 'ac', 'ca', 'cu']}),
            ('ft10c.txt',{'b': ['ab'], 'cd': ['cd'], 'f': ['ef'], 'gh': ['gh'], 'l': ['il'], 'mn': ['mno', 'mn'], 'p': ['op'], 'qr': ['qr'], 'st': ['stu', 'st'], 'v': ['via', 'uv'], 'z': ['za'], 'bcd': ['bcde', 'bcd'], 'fg': ['efg'], 'hl': ['hil'], 'pr': ['per'], 'fgh': ['fghi'], 'lmn': ['lmno'], 'pqrs': ['pqrs'], 'tvz': ['tuvz']})
        )
    @unpack
    def test(self, textfile, expected):
        return self.do_test(textfile, expected)

# The tests can be performed running program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()

