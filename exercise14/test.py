import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, string, k, expected):
        '''Test implementation
            - string       : character string
            - k             : an integer
            - expected      : list of string substrings
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es16(string, k)
        self.assertEqual(type(result), list, "The result is not a list")
        self.assertEqual(
            result, expected, f"Result must be {expected} instead of {result}")

    @data(
        ('aabbb', 1, ['bbb', 'aa', 'bb', 'a', 'b']),
        ('bcafedg', 3, ['afe', 'bca', 'caf', 'edg', 'fed']),
        ('ccaabbdd', 3, ['aabbdd', 'ccaabb', 'aabbd',
                         'abbdd', 'caabb', 'ccaab', 'abbd', 'caab'])
    )
    @unpack
    def test(self, string, k, expected):
        return self.do_test(string, k, expected)


# Tests are performed executing program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
