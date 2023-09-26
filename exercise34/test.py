import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, f2, expected, expectedGen):
        '''Test implementation
            - f1            : input text file
            - f2            : path where to save the result
            - expected      : expected number of transformed characters
            - expectedGen   : expected generated string
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es31(f1, f2)
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")
        with open(f2, 'r', encoding='utf8') as f:
            testo = f.read()
        self.assertEqual(
            testo, expectedGen, f"The generated text must be {expected} instead of {result}")

    @data(
        ('ftesto3.txt', 'risposta3.txt', 7, 'MoNtI, SterBINI e SPoGNArDI'),
        ('ftesto4.txt', 'risposta4.txt', 8, '''SalvE, Ho Una doManda:\nMa lo zERo E' Un nUMERo paRi o diSpaRi?\nSo cHE pUo' SEMbRaRE Una banaliTa', a naSo diREi cHE lo zERo E' Un nUMERo paRi\nMa non SapREi coME GiUSTificaRE la RiSpoSTa.\nConfido nEl voSTRo aiUTo!''')
    )
    @unpack
    def test(self, f1, f2, expected, expectedGen):
        return self.do_test(f1, f2, expected, expectedGen)


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
