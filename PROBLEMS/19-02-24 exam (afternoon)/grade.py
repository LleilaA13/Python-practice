# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys

import nary_tree
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
#DEBUG = True
DEBUG = False
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
# ----------------------------------- FUNC. 1 -------------------------------- #


def do_func1_tests(int_list, expected):
    res = program.func1(int_list)
    if res == None:
        return 0
    testlib.check_list(res, expected)
    return 0.5


def test_func1_1(run=True):
    lists = [[4, 4, 10, 4, 1], [4, 2, 1], [1, 4]]
    expected = [4, 1]
    ## We could use a decorator but could mess up things
    add_docstring(test_func1_1, locals())
    return do_func1_tests(lists, expected) if run else None

def test_func1_2(run=True):
    lists = [[-4, 5, 5, -1, 8, 6, -5, 3, 2, 3], [7, -7, -2, -3, -8, 2, 2, -3, -8, -5], [-10, -4, 4, -1, 7, 1, -8, -8, 1, -5]]
    expected = [-5]
    ## We could use a decorator but could mess up things
    add_docstring(test_func1_2, locals())
    return do_func1_tests(lists, expected) if run else None


def test_func1_3(run=True):
    lists = [[-4, 5, 5, -1, 8, 6, -5, 3, 2, 3], [7, -7, 5, -2,8, -3, -8, 2, 2, -3, -8, -5], [-10, -4, 4, -1, 7, 1,5,8, -8, -8, 1, -5]]
    expected = [8, 5, -5]
    ## We could use a decorator but could mess up things
    add_docstring(test_func1_3, locals())
    return do_func1_tests(lists, expected) if run else None


def test_func1_4(run=True):
    lists = [[36, -92, 12, 42, 89, -63, -52, 8, 38, 12, -3, 6, -80, 57, 83, -43, 69, -19, -25, 65],
             [-63, 6, 12, 38, 89, -19, -25, 36, -43, -3, -92, 57, 12, 8, 42, 69, -52, -80, 65, 83],
             [69, 12, -43, 6, 57, 89, 36, -92, 42, -52, -19, -3, 12, -25, 83, -80, 65, 38, 8, -63]]
    expected = [89, 83, 69, 65, 57, 42, 38, 36, 12, 8, 6, -3, -19, -25, -43, -52, -63, -80, -92]
    ## We could use a decorator but could mess up things
    add_docstring(test_func1_4, locals())
    return do_func1_tests(lists, expected) if run else None

# ----------------------------------- FUNC. 2 -------------------------------- #

def do_func2_tests(text, expected):
    res = program.func2(text)

    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il risultato è sbagliato! / The returned value is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 0.5


def test_func2_1(run=True):
    '''
    text = 'sOtto lA panca 1234La ca3212Pra Canta 4S5o6p7r8a LA Panca La CaPra crepa'
    expected   = 3212
    '''
    text = 'sOtto lA panca 1234La ca3212Pra Canta 4S5o6p7r8a LA Panca La CaPra crepa'
    expected = 3212
    return do_func2_tests(text, expected)

def test_func2_2(run=True):
    '''
    text = "z2s726Hf1V8B92Q o4dwQ9zY 5c6x6 t5q9P09219Ejhu4 01QOs 8 5ib9575296V5wo2n7  R97v46zs3 Z5y4 L 5BS42d0Pm"
    expected = 9575296
    '''
    text = "z2s726Hf1V8B92Q o4dwQ9zY 5c6x6 t5q9P09219Ejhu4 01QOs 8 5ib9575296V5wo2n7  R97v46zs3 Z5y4 L 5BS42d0Pm"
    expected = 9575296
    return do_func2_tests(text, expected)

def test_func2_3(run=True):
    text = """E4 3 5 1LA7HM0oo 6GXT28Z p 04tFQ2Ug 1El I9Sx8 5V8 2asj08q93sc3W 5 J 
            32o O417Ri8e11a2v61fd6N  C1S38Ryqyw12R91aw6UW  pVg1O5wXqCz42i3HrP1F1477832 OtU9038C  
            2d8z7zVH Y6HvWIg KfC85 27t8xtR8128f1tm 0Ufq 88J"""
    expected = 1477832
    return do_func2_tests(text, expected)

def test_func2_4(run=True):
    text = """4wOp1VCec DO   8m9oI0G0ElbK
        86YJdGU  Ur4 125Rt7S68M5kzNxMA08YP g0 3vnZSf2  xiZG1j7WJ 9ztsW bAq7Qr4k4985D d8kv3 86638gO  
        4N8g 88180 j2 7d78o 51 bE7 h a01j55j54   35 7W80 40933HiBX8b26Z5O5DAmB94 218dc 2J17TXE4b844132
        2 7  DED 3Qh83 Crm  u150OE2Z yvUqw"""
    expected = 844132
    return do_func2_tests(text, expected)


# ----------------------------------- FUNC. 3 ----------------------------------- #

def do_func3_tests(ID, expected):
    input_filename    = f'func3/in_{ID}.txt'
    output_filename   = f'func3/your_output_{ID}.txt'
    expected_filename = f'func3/expected_{ID}.txt'

    # remove the previous output each time if it is there
    if os.path.exists(output_filename):
        os.remove(output_filename)

    res = program.func3(input_filename, output_filename)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_text_file(output_filename, expected_filename)
    return 1


def test_func3_1(run=True):
    '''
    textfile_in  = 'func3/in_1.txt'
    textfile_out = 'func3/your_output_1.txt'
    expected     = 'func3/expected_1.txt'
    '''
    ID = 1
    expected = (236, 93)
    return do_func3_tests(ID, expected)

def test_func3_2(run=True):
    '''
    textfile_in  = 'func3/in_2.txt'
    textfile_out = 'func3/your_output_2.txt'
    expected     = 'func3/expected_2.txt'
    '''
    ID = 2
    expected = (1308, -1002)
    return do_func3_tests(ID, expected)

def test_func3_3(run=True):
    '''
    textfile_in  = 'func3/in_3.txt'
    textfile_out = 'func3/your_output_3.txt'
    expected     = 'func3/expected_3.txt'
    '''
    ID = 3
    expected = (1230, 1483)
    return do_func3_tests(ID, expected)

def test_func3_4(run=True):
    '''
    textfile_in  = 'func3/in_4.txt'
    textfile_out = 'func3/your_output_4.txt'
    expected     = 'func3/expected_4.txt'
    '''
    ID = 4
    expected = (3706, 107)
    return do_func3_tests(ID, expected)


# ----------------------------------- FUNC. 4 ----------------------------------- #


def do_func4_tests(ID, expected):
    input_filename  = f'func4/in_{ID}.txt'
    res = program.func4(input_filename)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il risultato è sbagliato! / The result is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 1


def test_func4_1(run=True):
    '''
    input_filename = 'func4/in_1.txt'
    expected =  3843772
    '''
    ID = 1
    expected = 3843772
    return do_func4_tests(ID, expected)

def test_func4_2(run=True):
    '''
    input_filename = 'func4/in_2.txt'
    expected = -45
    '''
    ID = 2
    expected = -45
    return do_func4_tests(ID, expected)


def test_func4_3(run=True):
    '''
    input_filename = 'func4/in_3.txt'
    '''
    ID = 3
    expected = 691
    return do_func4_tests(ID, expected)

def test_func4_4(run=True):
    '''
    input_filename = 'func4/in_4.txt'
    '''
    ID = 4
    expected = -974064605025447936000228
    return do_func4_tests(ID, expected)

# ----------------------------------- FUNC. 5 ----------------------------------- #

def do_test_func5(ID, expected):
    png_in  = f'func5/in_{ID}.png'
    # remove the previous image each time if it is there
    res = program.func5(png_in)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero stelline è sbagliato! / The number of stars are incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 6/4


def test_func5_1(run=True):
    '''
    png_file = func5/in_1.txt
    expected = {(210, 104, 67): 1, (191, 202, 206): 1, (189, 228, 132): 1, (249, 188, 166): 1, (57, 27, 115): 1,
                (15, 179, 174): 1, (175, 9, 74): 1, (173, 165, 145): 1, (209, 96, 126): 1}
    '''
    ID = 1
    expected = {(210, 104, 67): 1, (191, 202, 206): 1, (189, 228, 132): 1, (249, 188, 166): 1, (57, 27, 115): 1,
                (15, 179, 174): 1, (175, 9, 74): 1, (173, 165, 145): 1, (209, 96, 126): 1}
    return do_test_func5(ID, expected)

def test_func5_2(run=True):
    '''
    png_file = func5/in_2.png
    expected = {(150, 200, 150): 3, (200, 150, 125): 4, (125, 175, 200): 2, (125, 100, 125): 3, (125, 175, 125): 4, (200, 100, 150): 2}
    '''
    ID = 2
    expected = {(150, 200, 150): 3, (200, 150, 125): 4, (125, 175, 200): 2, (125, 100, 125): 3, (125, 175, 125): 4, (200, 100, 150): 2}
    return do_test_func5(ID, expected)


def test_func5_3(run=True):
    '''
    png_file = func5/in_3.png
    '''
    ID = 3
    expected = {(175, 175, 150): 18, (150, 175, 200): 4, (200, 175, 125): 4, (125, 100, 100): 4, (200, 175, 150): 2,
                (125, 200, 150): 4, (175, 200, 150): 7, (175, 125, 200): 5, (200, 150, 150): 6, (200, 175, 200): 7,
                (200, 125, 150): 3, (125, 125, 200): 3, (100, 100, 100): 6, (125, 200, 125): 3, (100, 175, 200): 3,
                (200, 200, 100): 5, (150, 175, 125): 3, (150, 125, 200): 2, (175, 100, 175): 2}

    return do_test_func5(ID, expected)


def test_func5_4(run=True):
    '''
    png_file = func5/in_4.png
    '''
    ID = 4
    expected = {(200, 175, 100): 4, (175, 150, 125): 3, (200, 100, 200): 3, (125, 125, 100): 9, (100, 175, 100): 10,
                (100, 200, 150): 5, (100, 125, 200): 2, (100, 150, 100): 9, (200, 150, 100): 11, (150, 175, 175): 6,
                (175, 125, 175): 3, (100, 150, 125): 8, (200, 200, 200): 1, (200, 150, 175): 4, (175, 125, 100): 7,
                (150, 125, 150): 2, (125, 150, 175): 3, (200, 100, 175): 3, (150, 100, 150): 11, (150, 175, 100): 1,
                (175, 175, 175): 4, (175, 200, 200): 6, (100, 175, 175): 2, (200, 125, 125): 3, (100, 100, 100): 4,
                (200, 150, 200): 1, (125, 175, 100): 3, (200, 100, 150): 3, (175, 175, 150): 3, (150, 150, 125): 4,
                (100, 175, 200): 5, (125, 175, 125): 3, (100, 100, 150): 1, (125, 200, 175): 4, (175, 150, 200): 3,
                (150, 125, 175): 7, (125, 150, 200): 9, (125, 100, 150): 1, (175, 200, 100): 6, (125, 150, 100): 1,
                (125, 175, 150): 1, (125, 200, 150): 5, (200, 175, 175): 2, (100, 125, 150): 4, (200, 100, 100): 1,
                (100, 150, 200): 1, (175, 100, 150): 1, (150, 125, 100): 1, (175, 125, 125): 1}
    return do_test_func5(ID, expected)

# ----------------------------------- EX. 1 ----------------------------------- #

def do_test_ex1(rootlist, expected):
    if not DEBUG:
        root = nary_tree.NaryTree.fromList(rootlist.copy())
        try:
            isrecursive.decorate_module(program)
            program.ex1(root)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)
    root     = nary_tree.NaryTree.fromList(rootlist.copy())
    expected1 = expected[:2]
    res = program.ex1(root)
    testlib.check(res[:2], expected1, None,
                  f'''{'*' * 50}\n[ERROR]I due percorsi tornati non sono corretti! / Incorrect paths!\nReturned={res}, expected={expected1}''')
    if len(res) == 2:
        return 2
    else:
        if res[2] != expected[2]:
            my_print(f'''{'*'*50}\n[ERROR]Il precorso ritornato non è corretto! / Incorrect path from min value to max value!\nReturned={root}, expected={expected}''')
            return 2
        else:
            return 8/3

def test_ex1_1(run=True):
    '''
    root:
                              *-7*                           |
                          /           \                      |
                       *1*                2                  |
                   */*    *|*        /    |    \             |
                 *-10*    *-3*     -8    -10    -5           |
                /  *\*     *|*      |      |                 |
               6   *-22*   *9*      7     -9                 |

    expected1: ([-7, 1, -10, -22], [-7, 1, -3, 9])
    expected2: ([-7, 1, -10, -22], [-7, 1, -3, 9], [-22, -10, 1, -3, 9])
    '''
    root = [-7,
                [1, [-10,   [6],
                            [-22]],
                    [-3,    [9]]],
                [2, [-8,    [7]],
                    [-10,   [-9]],
                    [-5]],
            ]
    expected = ([-7, 1, -10, -22], [-7, 1, -3, 9], [-22, -10, 1, -3, 9])
    return do_test_ex1(root, expected)

def test_ex1_2(run=True):
    root = [-18,
                [50, [-25,  [-40],
                            [-54]],
                    [-84,  [-98],
                            [6]],
                    [15, [27]]],
                [49],
                [-87, [ -25, [19, [93],
                                 [67]],
                             [-36]],
                        [21],
                        [83, [-26]]]
            ]
    expected = ([-18, 50, -84, -98], [-18, -87, -25, 19, 93], [-98, -84, 50, -18, -87, -25, 19, 93])
    return do_test_ex1(root, expected)

def test_ex1_3(run=True):
    root = [61, [56, [-51, [-95, [1, [65], [-61], [-20, [63, [52, [-85]]], [-21, [-30]], [-69, [-4], [4], [-63]]]]],
            [0, [-35, [55, [51], [-75], [-50]], [81], [95, [101]]], [-86, [-56], [49]], [-96, [-12, [-9], [19],
            [-95]], [-91], [-50, [-74]]]], [42, [-15, [-44, [98], [46]]], [-30, [-50, [-78]], [-20, [-25]]],
            [83, [54, [11]], [-20, [59], [-58]]]]], [-86, [-49, [85, [100]]]], [-5, [-61, [-84, [-27, [12, [-63], [14],
            [82]], [-50], [100]]], [83, [-38, [-67], [80], [14]], [-42], [-33, [58], [28], [-23]]]], [5], [74, [70, [38],
            [-19, [41]], [-83]]]]], [54, [-34, [3, [-2], [7, [77]]], [22]], [-61, [-18, [63, [3, [16]]], [-8], [-14, [-79,
            [48, [21, [53], [-85], [-72]]]], [68, [-100], [-13, [-87]], [-39]]]], [-69, [-87]]], [-84, [-39, [2, [-76],
            [86, [-29, [9, [95], [-13], [-10]], [4, [-5], [49]], [64, [-63]]], [93, [-45], [22, [51], [62]]]], [-20, [-50, [11]],
            [45, [27, [-74]], [14, [-9], [-49]], [-89, [-96]]]]], [-60]], [-54, [-27, [-5, [-86], [70]], [75, [-25], [-44],
            [-25, [-39], [-44]]], [95]], [94, [-76, [1], [36]], [-20, [-71], [-21], [-75]], [88, [-62, [-98], [-42], [-78]]]]]]]]
    expected = ([61, 54, -61, -18, -14, 68, -100], [61, 56, -51, 0, -35, 95, 101],
                [-100, 68, -14, -18, -61, 54, 61, 56, -51, 0, -35, 95, 101])
    return do_test_ex1(root, expected)



# ----------------------------------- EX.2 ----------------------------------- #
def do_ex2_test(directory, extensions, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(directory, extensions)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(directory, extensions)
    if res is None: return 0
    if res == expected:
        return 2
    my_print(
        f'''{'*' * 50}\n[ERROR]La lista ritornata non è corretta! / The returned list is incorrect!!\nReturned={res}, expected={expected}''')
    return 0

def test_ex2_1(run=True):
    directory  = 'ex2/A'
    extensions = ["txt", "pdf", "png", "gif"]
    expected   = {'ex2/A': [29, 56], 'ex2/A/C': [25, 92], 'ex2/A/B': [25, 28]}
    return do_ex2_test(directory, extensions, expected)


def test_ex2_2(run=True):
    directory  = 'ex2'
    extensions = ["png", "gif"]
    expected   = {'ex2/A/C': [25, 32], 'ex2/C/C/9n5': [20, 37], 'ex2/C/C/9n5/22zi524j': [20, 20], 'ex2/C/C': [20, 36], 'ex2/C/B/p3zt345614/17nt': [40, 40]}
    return do_ex2_test(directory, extensions, expected)

def test_ex2_3(run=True):
    directory  = 'ex2/C'
    extensions = ["pdf", "png"]
    expected   = {'ex2/C/C/9n5': [37, 46], 'ex2/C/C': [36, 41], 'ex2/C/B/p3zt345614/17nt': [40, 57]}
    return do_ex2_test(directory, extensions, expected)

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,   # OK
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,   # OK
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,   # OK
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,   # OK
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,   # OK
    test_ex1_1,    test_ex1_2,   test_ex1_3,                   # OK
    test_ex2_1,    test_ex2_2,  test_ex2_3,                   # OK
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
