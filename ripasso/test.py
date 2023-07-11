import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, f2, f3, expected, expectedDec):
        '''Test implementation
            - f1 : file with coded string
            - f2 : file containing the character encodings
            - f3 : file where to save the decoded string
            - expected : number of characters '?' expected
            - expectedDec : Decoded string expected
        '''
        with self.ignored_function('builtins.print'), \
            self.forbidden_function('os.walk'):
            #self.timer(2):
            result = program.ex30(f1, f2, f3)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}/The result should be {expected} instead of {result}")
        with open(f3,'r', encoding='utf8') as f:
            testo_dec = f.read()
        self.assertEqual(
            testo_dec, expectedDec, f"La decodifica {testo_dec} deve essere invece {expectedDec}/The decoded text {testo_dec} is wrong, it should be {expectedDec}")
        

    @data(
        ('ftesto1.txt','ftesto1b.txt','risposta1.txt', 2,'tutt?      a    n?nna?'),
        ('ftesto2.txt','ftesto2b.txt','risposta2.txt', 2, '?hi stu?ia passa!')
    )
    @unpack
    def test(self, f1, f2, f3, expected, expectedDec):
        return self.do_test(f1, f2, f3, expected, expectedDec)


# The tests can be performed running program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
