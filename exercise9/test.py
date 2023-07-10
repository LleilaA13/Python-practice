import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, word_set, expected):
        with self.ignored_function('builtins.print'), \
                self.forbidden_function('os.walk'):
                #self.timer(2):
            result = program.es8(word_set)
        self.assertEqual(type(result), list, "You must return a list")
        self.assertEqual(result, expected, "The answer is not correct")

    @data(  
        ({  'aaaa', 'acde', 'aacd', 'aaaade'},  ['aaaaaade', 'aaaaade', 'aaaacd', 'aaaade', 'aacde']),
        ({  'baxyy', 'abcabc', 'abccba', 'yyxab'}, ['abcabccba', 'abccbaxyy', 'baxyyxab', 'yyxabcabc', 'yyxabccba']),
        ({  'xabc', 'xab', 'xxyy', 'yyxx'}, ['xabc', 'xxyyxx', 'yyxxyy'])
        )
    @unpack
    def test(self, word_set, expected):
        return self.do_test(word_set, expected)



if __name__ == '__main__':
    Test.main()

