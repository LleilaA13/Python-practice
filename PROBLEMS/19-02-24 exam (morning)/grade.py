# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import glob
import hashlib
import tree
from testlib import my_print, COL, check_expected

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print(  'WARNING: Save program.empty.py as program.py\n'
            'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
#############################################################################

import program

#############################################################################
#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
DEBUG = True
#DEBUG = False
#############################################################################

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #

# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################





def test_personal_data_entry(run=True):
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname    != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'MATRICULATION NUMBER', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Student info: {program.name} {program.surname} {program.student_id}{COL["RST"]}')
    else:
        assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Informazioni studente: {program.nome} {program.cognome} {program.matricola}{COL["RST"]}')
    return 1e-9

def add_docstring(f, local):
    S = ''
    if 'run' in local: del local['run']
    for key, val in local.items():
        S += f'\n{key} = {val}'
    f.__doc__ = S


###############################################################################

# ----------------------------------- FUNC. 1 --------------------------------
def do_func1_tests(list1, list2, expected):
    res = program.func1(list1, list2)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dict is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return .5

def test_func1_1(run=True):
    '''
    list1: [ 'a', 'Bc', 'a', 'b', 'cR', 'e', 'a', 'qrt', 'st' ]
    list2: [ 'a', 'cd', 'f', 'bC', 'cr', 'E', 'bn', 'c' ]
    expected:  {1: {'e', 'E', 'a'}, 2: {'Bc', 'bC', 'cR', 'cr'}}
    '''
    list1 = ['a', 'Bc', 'a', 'b', 'cR', 'e', 'a', 'qrt', 'st']
    list2 = ['a', 'cd', 'f', 'bC', 'cr', 'E', 'bn', 'c']
    expected = {1: {'e', 'E', 'a'}, 2: {'Bc', 'bC', 'cR', 'cr'}}
    return do_func1_tests(list1, list2, expected)



def test_func1_2(run=True):
    '''
    list1 = ['wNYVf', 'uf', 'stdL', 'lwCuZZStP', 'l', 'WEcTYd', 'yAkBG', 'gNHkS', 'vABbtAAO', 'adO', 'WRgNCRin',
             'iGMRQYD', 'VG', 'lQhvmoVMg', 'EA']
    list2 = ['onT', 'VG', 'XmNIED', 'WRgNCRin', 'adO', 'vABbtAAO', 'iUhkop', 'xj', 'YL', 'gNHkS', 'wDWQL', 'ndXwyhSJK',
             'gAi', 'Htn', 'DDnMnTwenR']
    expected = {2: {'VG'}, 5: {'gNHkS'}, 8: {'WRgNCRin', 'vABbtAAO'}, 3: {'adO'}}
    '''
    list1 = ['wNYVf', 'uf', 'stdL', 'lwCuZZStP', 'l', 'WEcTYd', 'yAkBG', 'gNHkS', 'vABbtAAO', 'adO', 'WRgNCRin',
             'iGMRQYD', 'VG', 'lQhvmoVMg', 'EA']
    list2 = ['onT', 'VG', 'XmNIED', 'WRgNCRin', 'adO', 'vABbtAAO', 'iUhkop', 'xj', 'YL', 'gNHkS', 'wDWQL', 'ndXwyhSJK',
             'gAi', 'Htn', 'DDnMnTwenR']
    expected = {2: {'VG'}, 5: {'gNHkS'}, 8: {'WRgNCRin', 'vABbtAAO'}, 3: {'adO'}}
    return do_func1_tests(list1, list2, expected)

def test_func1_3(run=True):
    '''
    list1 = ['j', 'IHRgP', 'sAITqZ', 'dBpmo', 'etDaY', 'CN', 'jRcYVIk', 'uKTMtYfg', 'Irw', 'qM', 'GjcaRLVQ', 'yZDNU',
             'BF', 'O', 'YWzNa', 'nm', 'zMIVdiiD', 'ocZ', 'uZpJESx', 'aCScomc', 'JZTAB', 'CKQeDxHmj', 'DdGkGGoIjZ',
             'zriGAlUN', 'GYBKMEXi', 'AUCeOpV', 'JoIUANMIq', 'i', 'dYLDmjYf', 'DnoXzXHcW']
    list2 = ['NgfHdnlT', 'Lo', 'gxgX', 'aCScomc', 'nX', 'Gpms', 'WLxXxQCpo', 'GYBKMEXi', 'nm', 'JewKWInq', 'iRhmADPAx',
             'BF', 'DdGkGGoIjZ', 'WnH', 'XQZ', 'AnlbuHbOnT', 'qM', 'EZKehpOgNM', 'CN', 'LAUWNmnp', 'QsUYWt', 'Ba',
             'dYLDmjYf', 'EzHgiE', 'OvEqQDm', 'SEZ', 'etDaY', 'XIiqz', 'ShUV', 'j']
    expected = {2: {'nm', 'qM', 'CN', 'BF'}, 7: {'aCScomc'}, 8: {'GYBKMEXi', 'dYLDmjYf'}, 5: {'etDaY'},
    '''
    list1 = ['j', 'IHRgP', 'sAITqZ', 'dBpmo', 'etDaY', 'CN', 'jRcYVIk', 'uKTMtYfg', 'Irw', 'qM', 'GjcaRLVQ', 'yZDNU',
             'BF', 'O', 'YWzNa', 'nm', 'zMIVdiiD', 'ocZ', 'uZpJESx', 'aCScomc', 'JZTAB', 'CKQeDxHmj', 'DdGkGGoIjZ',
             'zriGAlUN', 'GYBKMEXi', 'AUCeOpV', 'JoIUANMIq', 'i', 'dYLDmjYf', 'DnoXzXHcW']
    list2 = ['NgfHdnlT', 'Lo', 'gxgX', 'aCScomc', 'nX', 'Gpms', 'WLxXxQCpo', 'GYBKMEXi', 'nm', 'JewKWInq', 'iRhmADPAx',
             'BF', 'DdGkGGoIjZ', 'WnH', 'XQZ', 'AnlbuHbOnT', 'qM', 'EZKehpOgNM', 'CN', 'LAUWNmnp', 'QsUYWt', 'Ba',
             'dYLDmjYf', 'EzHgiE', 'OvEqQDm', 'SEZ', 'etDaY', 'XIiqz', 'ShUV', 'j']
    expected = {2: {'nm', 'qM', 'CN', 'BF'}, 7: {'aCScomc'}, 8: {'GYBKMEXi', 'dYLDmjYf'}, 5: {'etDaY'},
                10: {'DdGkGGoIjZ'}, 1: {'j'}}
    return do_func1_tests(list1, list2, expected)


def test_func1_4(run=True):
    list1 = ['xcaldDdyz', 'pgO', 'nlBd', 'pLrkHEm', 'Mz', 'OfVQsFpUU', 'VmWtb', 'bY', 'jtV', 'mrJgOMFPyY', 'M',
             'vCCfvAm', 'jcKwvEceU', 'EnF', 'L', 'UZAtgZcR', 'yts', 'TK', 'ObYZkm', 'ezRQRydg', 'KGphZlnFn', 'SwNpRk',
             'QNYCYheuB', 'iaFOILqz', 'Ad', 'fDafD', 'QjNNPrVREV', 'qkP', 'tfbo', 'YUIurm', 'BzJcPA', 'XEuJBJ',
             'mTtAlR', 'aq', 'i', 'yPs', 'HLfk', 'XrcaoWXYd', 'jM', 'aYo', 'TAyQ', 'KdF', 'E', 'ZLGVilMDn', 'v',
             'bifRnwbMnS', 'ZjRHsRD', 'iWAmFxjL', 'vyGDwLfjMh', 'wHGOFkQSz', 'E', 'mW', 'QUZtvCtoJ', 'Y', 'c', 'uTl',
             'gTGrzzwqr', 'h', 'RjpyqiK', 'lW', 'ecJkodvm', 'XI', 'fLXCUc', 'us', 'UH', 'zpRt', 'qaJRDjD', 'mNCw',
             'UGtt', 'lwjaNY', 'qyKjP', 'rWx', 'sqsw', 'QMZ', 'FgnooKxas']
    list2 = ['YUIurm', 'OTjV', 'SmVDOxCbF', 'rgEATCw', 'mW', 'QNYCYheuB', 'PKra', 'qkWtWdZEmB', 'HGnGbRz', 'kRQU',
             'ZLGVilMDn', 'XBGg', 'QjNNPrVREV', 'Mz', 'apRTmlq', 'TV', 'QatwWbIhe', 'qtKZmVYlU', 'aYo', 'QUZtvCtoJ',
             'dTFdGZAd', 'iSJkukR', 'UuKS', 'DFG', 'VjKZmEYBY', 'amKeXDQ', 'keWy', 'hrHPOrn', 'Y', 'ZjRHsRD',
             'vmUPSRGaGx', 'mrGFEGzZiP', 'BcXwJ', 'wty', 'TOIeaRP', 'ObYZkm', 'lwjaNY', 'wHGOFkQSz', 'nlBd', 'Ad',
             'ipMhJ', 'fDafD', 'pLrkHEm', 'Ud', 'OJw', 'kfqQ', 'c', 'oEmgrkamt', 'uelF', 'SwNpRk', 'nDtJBdOKn', 'EnF',
             'mTtAlR', 'KefIbphyih', 'WdT', 'v', 'W', 'XEuJBJ', 'WJP', 'UH', 'QdfBRK', 'SKmlqgAT', 'gxs', 'g', 'Ma',
             'YtAsbiRg', 'XPEhxht', 'kinpHYRWq', 'EnvmSMb', 'IFDsAWdDX', 'p', 'Kpn', 'iaFOILqz', 'KPT', 'L']
    expected = {6: {'mTtAlR', 'YUIurm', 'XEuJBJ', 'SwNpRk', 'ObYZkm', 'lwjaNY'}, 2: {'Mz', 'UH', 'Ad', 'mW'},
                7: {'pLrkHEm', 'ZjRHsRD'}, 3: {'aYo', 'EnF'}, 9: {'wHGOFkQSz', 'QNYCYheuB', 'QUZtvCtoJ', 'ZLGVilMDn'},
                1: {'Y', 'c', 'L', 'v'}, 10: {'QjNNPrVREV'}, 4: {'nlBd'}, 5: {'fDafD'}, 8: {'iaFOILqz'}}
    return do_func1_tests(list1, list2, expected)

def do_func2_tests(dicts, expected):
    res = program.func2(dicts)
    if res == None:
        return 0
    testlib.check_dict(res, expected)
    return 0.5


def test_func2_1(run=True):
    dicts = [{1:'iac', 2:'andrea',3:'mau', 5:'angelo'},
             {2:'sterbini', 3:'mancini',1:'masi', 5:'spognardi'}]
    expected = {1: 'aaciims', 2: 'aabdeeiinnrrst', 3: 'aaciimmnnu', 5: 'aadeggilnnooprs'}
    add_docstring(test_func2_1, locals())
    return do_func2_tests(dicts, expected) if run else None


def test_func2_2(run=True):
    dicts = [{1: 'iac', 2: 'andrea', 3: 'mau', 5:'angelo'},
             {2: 'sterbini', 3: 'mancini', 1: 'masi', 5: 'spognardi'},
             {2 : 'professor', -1: 'student', 5 : 'office manager', 100: 'nulla'}]
    expected = {1: 'aaciims', 2: 'aabdeeefiinnooprrrrssst', 3: 'aaciimmnnu', 5: ' aaaacdeeeffgggiilmnnnoooprrs', -1: 'densttu', 100: 'allnu'}
    add_docstring(test_func2_2, locals())
    return do_func2_tests(dicts, expected) if run else None



def test_func2_3(run=True):
    dicts = [{2: 'sterbini', 3: 'mancini', 1: 'masi', 5: 'spognardi'},
             {200 : 'apple', -1000: 'banana', 1000 : 'pineapple', 1: 'kiwi'},
             {1: 'iac', 2: 'andrea', 3: 'mau', 5:'angelo'},
             {-1001 : 'pantera', -1000: 'bufalo', 1: 'leone', 23: 'gazzella', 7 : 'giraffa'}]
    expected = {1: 'aaceeiiiiklmnosw', 2: 'aabdeeiinnrrst', 3: 'aaciimmnnu', 5: 'aadeggilnnooprs', 200: 'aelpp', -1000: 'aaaabbflnnou', 1000: 'aeeilnppp', -1001: 'aaenprt', 23: 'aaegllzz', 7: 'aaffgir'}
    add_docstring(test_func2_3, locals())
    return do_func2_tests(dicts, expected) if run else None



def test_func2_4(run=True):
    dicts = [{-9: 'spp30r6c03v9uc9529c5',
              18: 'amf945a0boszupp2af6t',
              17: '0nf0qpfsfreb6s4brzlt',
              6: '9n3bf88pf5rvc71zvt46',
              -2: 'f6i4trz7hvcthtisen5m',
              3: 'mse24of2htrn8ofp8ec5',
              7: 'fcvhr391fslf27t0gbo4',
              9: 'p1pa5q7qm23bfv2gtlf6',
              -12: 'nzc6ap7c5b2s49spfp39',
              -19: '8q0ssftlsi1718ec9ui8',
              -15: '91z750nfpfvn2u5mhm2o',
              -6: 'nbeisllez33bsl54nn4u',
              13: '7n7sprlcoprfz0p30gql',
              1: 'pa4vzooruv0e586t7pou',
              0: 'hmga4gvebla4fezuamcv'},
             {-15: '5r9u8lfqco72e3qssabs',
              -13: '5t7r735vn3l73fn7amqr',
              -5: 'icfzf6oetlsh67sa9srl',
              -1: 'mnlp06uomc8b3890l7es',
              -9: '2b0ocu1z4ep8hc090u9q'},
             {-9: 'lf2hp4hi2lm1ac7u0o0u',
              -12: 'i2oifeqvn9q7ol6t520q',
              -18: 'itc6vm47garf4089siie',
              -2: '14994r6e550v0hfaf9q1',
              2: 'clf5acrh0m7vcifpa328',
              -15: 'ihf3q9ap80hobc19f0qv',
              -16: 're6an3o38lo97hn5eq7u',
              17: 'z3rg04if9e1rsbg5sqmi',
              8: 'f7fvvufi59mbvifsol64',
              15: 't9f3cighn7tr2qt4ot4f',
              16: 's97g0nfg2i5r9vpnhf9b',
              -4: '2963g5i12uftosievlrm',
              -11: '6r4219b1247getr0ms6g',
              1: '0fvbvlrlgt1onbtf3ifi',
              -10: 'etf8cnt3hhhf6a80nm27',
              10: 'cblfn0co44294i3m62nv',
              -13: 'm3qlmss8csp853u3n2zq',
              12: 'u9l2hqtgmf2qoqbp2eq9',
              -8: 'h99vrt6ae607rtve1ehf',
              4: '38tge5amctbat4pul4hu',
              0: 'e8zslsnez4ft88s5p7hs',
              -17: 'rc9fsv4uq68spqsb6tmn'}
             ]
    expected = {-9: '000000011222233445567899999abccccccefhhhillmooppppqrsuuuuuvz', 18: '024569aaabffmoppstuz', 17: '0001344569bbbeeffffggiilmnpqqrrrrsssstzz', 6: '134567889bcffnprtvvz', -2: '0011444555667999aceefffhhhiimnqrrstttvvz', 3: '224588ceeffhmnooprst', 7: '0123479bcfffghlorstv', 9: '1223567abffglmppqqtv', -12: '022234556677999abcceffiilnnoopppqqqsstvz', -19: '01178889cefiilqssstu', -15: '000112223355577889999aabbccefffffhhhilmmnnoooppqqqqrsssuuvvz', -6: '33445bbeeilllnnnssuz', 13: '00377cfgllnopppqrrsz', 1: '001345678abbefffgiillnoooopprrtttuuvvvvz', 0: '44457888aaabceeeeffgghhllmmnpsssstuvvzzz', -13: '2333333555777788acfllmmmnnnpqqqrrssstuvz', -5: '6679aceffhillorssstz', -1: '00367889bcellmmnopsu', -18: '0446789acefgiiimrstv', 2: '023578aacccffhilmprv', -16: '33567789aeehlnnooqru', 8: '45679bffffiilmosuvvv', 15: '234479cffghinoqrtttt', 16: '0257999bffgghinnprsv', -4: '1223569efgiilmorstuv', -11: '01122446679beggmrrst', -10: '0236788aceffhhhmnntt', 10: '022344469bccfilmnnov', 12: '22299befghlmopqqqqtu', -8: '0166799aeeefhhrrttvv', 4: '34458aabceghlmptttuu', -17: '46689bcfmnpqqrssstuv'}
    add_docstring(test_func2_4, locals())
    return do_func2_tests(dicts, expected) if run else None


def do_func3_tests(lists, expected):
    res = program.func3(lists)
    if res == None:
        return 0
    testlib.check_val(res, expected)
    return 0.5


def test_func3_1(run=True):
    lists = [[[]], [[[[[[]]]]]], [[]]]
    expected = 6
    add_docstring(test_func3_1, locals())
    return do_func3_tests(lists, expected) if run else None


def test_func3_2(run=True):
    lists = []
    expected = 0
    add_docstring(test_func3_2, locals())
    return do_func3_tests(lists, expected) if run else None

def test_func3_3(run=True):
    lists = [[]]
    expected = 1
    add_docstring(test_func3_3, locals())
    return do_func3_tests(lists, expected) if run else None


def test_func3_4(run=True):
    lists = [[], [], [], [[[]]], [[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]],]
    expected = 19
    add_docstring(test_func3_4, locals())
    return do_func3_tests(lists, expected) if run else None


# ----------------------------------- EX.1 ----------------------------------- #

def do_func4_tests(ID, expected):
    input_filename  = f'func4/func4_test{ID}.txt'
    output_filename = f'func4/func4_out{ID}.txt'
    expected_filename = f'func4/func4_exp{ID}.txt'
    res = program.func4(input_filename, output_filename)
    if res == None:
        return 0
    testlib.check_list(res, list(expected))
    testlib.check_text_file(output_filename, expected_filename)
    return 2


def test_func4_1(run=True):
    ID = 1
    expected = (772, 892, 950)
    add_docstring(test_func4_1, locals())
    return do_func4_tests(ID, expected) if run else None


def test_func4_2(run=True):
    ID = 2
    expected = (0, 0, 0, 0, 0, 0, 0, 0, 502, 546, 660, 1035, 1362, 1439, 1727, 1992, 2373, 2642, 2751, 3066)
    add_docstring(test_func4_2, locals())
    return do_func4_tests(ID, expected) if run else None


def test_func4_3(run=True):
    ID = 3
    expected = (565, 586, 629, 644, 650, 794, 910, 936, 1551, 1665, 1890, 2057, 3050, 3549, 4113, 4920, 6001, 7242, 11214)
    add_docstring(test_func4_3, locals())
    return do_func4_tests(ID, expected) if run else None


def do_test_func5(ID,H, W, sx, sy, expected):
    img_out = f'func5/func5_out{ID}.png'
    img_exp = f'func5/func5_exp{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(H, W, sx, sy, img_out)
    if res == None:
        return 0
    testlib.check_val(res, expected, f'''{'*'*50}\n[ERROR] Il numero di segmenti colorati è sbagliato! / The number of colored segments is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
    testlib.check_img_file(img_out, img_exp)
    return 1.5


def test_func5_1(run=True):
    ID = 1
    H = 9
    W = 17
    sx = 3
    sy = 1
    expected = 105
    add_docstring(test_func5_1, locals())  
    return do_test_func5(ID, H, W, sx, sy, expected)


def test_func5_2(run=True):
    ID = 2
    H = 17
    W = 129
    sy = sx = 3
    expected = 1041
    add_docstring(test_func5_2, locals())  
    return do_test_func5(ID, H, W, sx, sy, expected)


def test_func5_3(run=True):
    ID = 3
    H = 1
    W = 10
    sy = sx = 0
    expected = 10
    add_docstring(test_func5_3, locals())  
    return do_test_func5(ID, H, W, sx, sy, expected)


def test_func5_4(run=True):
    ID = 4
    H = 201
    W = 101
    sy = 19
    sx = 9
    expected = 3201
    add_docstring(test_func5_4, locals())  
    return do_test_func5(ID, H, W, sx, sy, expected)

# ----------------------------------- EX.1 ----------------------------------- #

def do_ex1_test(root, expected, score=2):
    res = program.ex1(root)
    if res == None:
        return 0
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR]Il valore ritornato non è corretto! / The returned value is incorrect!!\nReturned={res}, expected={expected}''')
        return 0
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(root)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)
    return score


def test_ex1_1(run=True):
    '''
        root      
    ______25______ 
   |             |  
   8__        ___2___ 
      |      |       |  
      3      9       1  

      expected = [{25}, {8, 2}, {9, 3, 1}]
    '''
    root = tree.BinaryTree.fromList([25, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
    expected = [{25}, {8, 2}, {9, 3, 1}]
    return do_ex1_test(root, expected)


def test_ex1_2(run=True):
    '''
              root       
          ______2______  
         |             | 
      __ 7__        ___15___  
     |      |      |       | 
    _4_     3_    _0_     _5_  
   |   |      |  |   |   |   | 
   2   -1     1  8   3   2  -9 

       expected = [{2}, {15, 7}, {0, 3, 4, 5}, {1, 2, 3, -9, 8, -1}]
    '''
    root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [15, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [-9, None, None]]]])
    expected = [{2}, {15, 7}, {0, 3, 4, 5}, {1, 2, 3, -9, 8, -1}]
    return do_ex1_test(root, expected)


def test_ex1_3(run=True):
    '''
    A big tree
    expected = [{-2}, {20, 5}, {-5, 20, 13}, {17, 19, 23, -7, 13}, {2, 5, 8, 12, 14, 20, -1, -10, -7, -2}, {2, 4, 6, 9, 11, 12, 14, 16, 17, 20, 21, 26, 27, -2, -6, -4, -1}, {1, 3, 5, 6, 10, 12, 14, 16, 17, 18, 21, 26, 27, 28, 29, 30, -10, -9, -8, -4, -3, -2}, {0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 17, 18, 19, 20, 21, 22, -9, 24, 25, 26, 28, 29, 30, -1, -10, -5, -4, -2}, {0, 1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 17, 19, 20, 21, 23, 24, 25, 28, 29, 30, -10, -9, -8, -4, -3, -2}, {1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, -8, -10, -9, -1, -7, -6, -5, -4, -3, -2}, {0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 30, -10, -8, -7, -6, -4, -3, -2}, {0, 2, 3, 4, 5, 7, 10, 12, 14, 15, 16, 17, 21, 22, 23, 24, 25, 27, 30, -10, -9, -1, -5, -4, -2}, {10, 3, -2, 7}, {12}]
    '''
    root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    expected = [{-2}, {20, 5}, {-5, 20, 13}, {17, 19, 23, -7, 13}, {2, 5, 8, 12, 14, 20, -1, -10, -7, -2}, {2, 4, 6, 9, 11, 12, 14, 16, 17, 20, 21, 26, 27, -2, -6, -4, -1}, {1, 3, 5, 6, 10, 12, 14, 16, 17, 18, 21, 26, 27, 28, 29, 30, -10, -9, -8, -4, -3, -2}, {0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 17, 18, 19, 20, 21, 22, -9, 24, 25, 26, 28, 29, 30, -1, -10, -5, -4, -2}, {0, 1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 17, 19, 20, 21, 23, 24, 25, 28, 29, 30, -10, -9, -8, -4, -3, -2}, {1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, -8, -10, -9, -1, -7, -6, -5, -4, -3, -2}, {0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 30, -10, -8, -7, -6, -4, -3, -2}, {0, 2, 3, 4, 5, 7, 10, 12, 14, 15, 16, 17, 21, 22, 23, 24, 25, 27, 30, -10, -9, -1, -5, -4, -2}, {10, 3, -2, 7}, {12}]
    return do_ex1_test(root, expected, score=3)


# ----------------------------------- EX. 2----------------------------------- #


def do_ex2_test(alfa, expected, score=2):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(alfa)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(alfa)
    if res == None:
        return 0
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR]Il valore ritornato non è corretto! / The returned value is incorrect!!\nReturned={res}, expected={expected}''')
        return 0
    return score


def test_ex2_1(run=True):
    alfabet = 'icA'
    #expected = {'iAc', 'cAi', 'Ai', 'Ac'}
    expected = {'i', 'Ai', 'cAi', 'iAc', 'Ac', 'cA', 'c', 'A', 'iA'}
    add_docstring(test_ex2_1, locals())
    return do_ex2_test(alfabet, expected)


def test_ex2_2(run=True,):
    alfabet = 'superW'
    expected = {'u', 'Wp', 'uWe', 'rW', 'eWr', 'pWu', 'uWs', 'sWp',
                'e', 'p', 'sWu', 'eWs', 'r', 'rWe', 'sW', 'pWs', 'Wr',
                'W', 'We', 'eW', 'rWp', 'eWp', 'uWr', 'pWr', 's',
                'pW', 'uW', 'pWe', 'sWr', 'eWu', 'sWe', 'rWs', 'rWu',
                'Wu', 'uWp', 'Ws'}
    add_docstring(test_ex2_2, locals())
    return do_ex2_test(alfabet, expected)


def test_ex2_3(run=True):
    alfabet = 'AbCdEz'
    #expected = {'bCdEzA', 'CdEbAz', 'dAbEzC', 'CzEbAd', 'CbEdAz', 'zCdEbA', 'CbEzAd', 'CbAdEz', 'bAzCdE', 'EzAbCd', 'bEdCzA', 'dAzEbC', 'EdAbCz', 'CbAzEd', 'CdEzAb', 'AzEdCb', 'bCzEdA', 'dEbAzC', 'zAdEbC', 'zCdAbE', 'CzAdEb', 'zEbAdC', 'dCbAzE', 'AdEbCz', 'AdCzEb', 'dCzEbA', 'dAzCbE', 'bAzEdC', 'EzCbAd', 'bCzAdE', 'EdCzAb', 'zCbEdA', 'AzCbEd', 'CdAzEb', 'dEbCzA', 'EbAzCd', 'AdEzCb', 'zEdAbC', 'dEzCbA', 'CzAbEd', 'EzAdCb', 'bEzCdA', 'dCzAbE', 'AdCbEz', 'zAdCbE', 'dEzAbC', 'AbCdEz', 'bEzAdC', 'zAbCdE', 'bAdEzC', 'bEdAzC', 'dCbEzA', 'AbEzCd', 'EbCzAd', 'EdAzCb', 'bCdAzE', 'EbCdAz', 'zCbAdE', 'EdCbAz', 'AzEbCd', 'EzCdAb', 'bAdCzE', 'zEdCbA', 'dAbCzE', 'EbAdCz', 'AbCzEd', 'CdAbEz', 'CzEdAb', 'AbEdCz', 'zAbEdC', 'zEbCdA', 'AzCdEb'}
    expected = {'bAd', 'dEbA', 'CdEb', 'EdAbC', 'AdCbE', 'Ez', 'CdAzE', 'AzC', 'EbAz', 'dEz', 'bEzA', 'bCdEzA', 'AbEd', 'EbC', 'AzCd', 'EdCbAz', 'zEd', 'dAbE', 'bA', 'AdEz', 'zEbCdA', 'dEb', 'EzCbA', 'CzEbA', 'bEdAz', 'EzCb', 'dAbCzE', 'bCz', 'dCzEbA', 'Az', 'CbEd', 'EdAzCb', 'dAzCbE', 'dAzEbC', 'zAbCdE', 'EbAd', 'bEdAzC', 'Cd', 'AdCbEz', 'bEzCd', 'dAz', 'EzAdCb', 'dEzA', 'bAdEz', 'dEzCbA', 'EzCdAb', 'AbEz', 'EbAdC', 'zCdEbA', 'dEzCb', 'bAdC', 'zCd', 'EdC', 'zA', 'dAzC', 'bEd', 'zCdAbE', 'EzC', 'zE', 'dCzA', 'Eb', 'EzAb', 'dEzAb', 'bEzAdC', 'dCbE', 'dEbC', 'zCdE', 'zAbEd', 'AzCbEd', 'bAzCdE', 'Cz', 'dA', 'AzCdE', 'EdAzC', 'EbA', 'EbAdCz', 'EbAzC', 'zAdEbC', 'AzCb', 'CzEbAd', 'zAb', 'CzAbEd', 'EdAz', 'dAbEz', 'bEzC', 'bAdE', 'CzAb', 'CdEzA', 'AbCd', 'bAz', 'CdA', 'CdAzEb', 'bCdAzE', 'EdCzAb', 'CdEbA', 'CbAd', 'zCbAd', 'EzCdA', 'dEbAz', 'CbAdE', 'bEdA', 'CbEzAd', 'AzEbCd', 'AdEzC', 'bCdAz', 'bAdCzE', 'CdEz', 'dAbCz', 'CzAdEb', 'dEbCzA', 'dCz', 'zEbCd', 'bCzAd', 'EzAbCd', 'CdAbE', 'AzE', 'AbEdCz', 'CzEdAb', 'dAbC', 'AzEbC', 'bCzE', 'zCbA', 'zCbAdE', 'dCbEzA', 'EdCb', 'E', 'bAdEzC', 'zCbEd', 'zEdAb', 'z', 'CzAd', 'EdAbCz', 'CbE', 'bAzE', 'CzAdE', 'EzCbAd', 'bAzC', 'zAbC', 'zCdAb', 'AzEdCb', 'CbAz', 'bAdCz', 'AzEd', 'zAdCb', 'CdAz', 'dCb', 'zEdC', 'EzA', 'dEbCz', 'd', 'EbCd', 'bEzAd', 'AbEdC', 'CbAzE', 'CdEzAb', 'bC', 'Ad', 'dAzCb', 'bEz', 'dCbEz', 'zCdA', 'zAd', 'EbCdAz', 'AdCb', 'AzEdC', 'dEbAzC', 'EbCzAd', 'AbCdEz', 'EzAdC', 'CbEdAz', 'zAbE', 'dAzEb', 'CdAbEz', 'bEdC', 'bAzCd', 'EbAzCd', 'zEbC', 'zEdA', 'bEdCz', 'AbCdE', 'CbAdEz', 'zEbAdC', 'bCdA', 'zEdCb', 'AdEbCz', 'bCzA', 'AzCbE', 'EdCzA', 'bCzAdE', 'AbEzCd', 'Ed', 'zCbE', 'Cb', 'CdAb', 'b', 'EdCz', 'EdAb', 'AdEzCb', 'zAdCbE', 'AdE', 'dC', 'dCzE', 'dCbA', 'CzAbE', 'bE', 'zAdC', 'zAbEdC', 'AbE', 'zCbEdA', 'dEzC', 'EdCbA', 'bEdCzA', 'CzEb', 'AbCz', 'dCbAzE', 'zAbCd', 'CzEdA', 'AdC', 'bAzEdC', 'zEdCbA', 'zAdEb', 'zEbAd', 'bCzEd', 'dCzAb', 'dAbEzC', 'C', 'AbC', 'zAdE', 'dAzE', 'EzCd', 'EzAd', 'A', 'dCzEb', 'dE', 'EdA', 'EbCzA', 'bCzEdA', 'CzE', 'zEbA', 'AbCzEd', 'bCdEz', 'AzEb', 'CbEz', 'dCbAz', 'AdEb', 'dEzAbC', 'Ab', 'zEb', 'CzEd', 'AbEzC', 'AdEbC', 'zEdAbC', 'AdCz', 'dCzAbE', 'AbCzE', 'AzCdEb', 'bCd', 'zCb', 'dAb', 'CdE', 'zC', 'EzAbC', 'bEzCdA', 'AdCzEb', 'EbCdA', 'AdCzE', 'CdEbAz', 'CbAzEd', 'CzA', 'bCdE', 'zCdEb', 'bAzEd', 'CbEdA', 'EbCz', 'CbA', 'CbEzA'}
    add_docstring(test_ex2_3, locals())
    return do_ex2_test(alfabet, expected, score=3)



################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,  test_ex1_2, test_ex1_3,
    test_ex2_1,  test_ex2_2, test_ex2_3,
    test_personal_data_entry,
]


if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(   tests,
                        verbose=True,
                        logfile='grade.csv',
                        stack_trace=DEBUG)
    testlib.check_exam_constraints()
    if 'matricola' in program.__dict__:
        print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')
################################################################################
