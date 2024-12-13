# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import tree

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program


def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        col = ''
        if any(err in args[0] for err in ['[OK]', 'Correct']):
            col = COL['BOLD']+COL['GREEN']
        if any(err in args[0] for err in ['error', 'Error', 'ERROR',]):
            col = COL['BOLD']+COL['RED']
        if col:
            return func(f'{col}', *args, f'{COL["RST"]}{COL["ENDC"]}', **kwargs, )
        else:
            return func(*args, **kwargs, )
    return wrapped_func

my_print = my_decorator(print)

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #

# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
#DEBUG = True
DEBUG = False
#############################################################################

COL = {'RED': '\u001b[31m',
       'RST': '\u001b[0m',
       'GREEN': '\u001b[32m',
       'YELLOW' : '\u001b[33m',
       'BOLD' : '\033[1m',
       'ENDC' : '\033[0m'}


def test_personal_data_entry():
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

###############################################################################


def do_func1_tests(int_list, expected):
    res = program.func1(int_list)
    if res == None:
        raise testlib.NotImplemented()
    # testlib.check_dict(res, expected)
    testlib.check_list(int_list, expected[0])
    testlib.check_val(res, expected[1])
    return 0.5


def test_func1_1():
    '''
    int_list = [[1, 2, 3], [-1, 2, 3], [2, 2, -2]]
    expected = ([6, -6, -8], 3)
    '''
    int_list = [[1, 2, 3], [-1, 2, 3], [2, 2, -2]]
    expected = ([6, -6, -8], 3)
    return do_func1_tests(int_list, expected)

def test_func1_2():
    '''
    int_list = [[-1, 0, 1], [999999, -99999], [1], [0], [-9999999]]
    expected = ([0, -99998900001, 1, 0, -9999999], 5)
    '''
    int_list = [[-1, 0, 1], [999999, -99999], [1], [0], [-9999999]]
    expected = ([0, -99998900001, 1, 0, -9999999], 5)
    return do_func1_tests(int_list, expected)

def test_func1_3():
    '''
    int_list = []
    expected = ([], 0)
    '''
    int_list = []
    expected = ([], 0)
    return do_func1_tests(int_list, expected)

def test_func1_4():
    '''
    int_list = [[1, 2, 3, 4, 5, 6, 7, 8], [987, 9876, 9876, 9], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0], [-9, -8, -7, -6, -5]]
    expected = ([40320, 866406745008, 1, 0, -15120], 5)
    '''
    int_list = [[1, 2, 3, 4, 5, 6, 7, 8], [987, 9876, 9876, 9], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0], [-9, -8, -7, -6, -5]]
    expected = ([40320, 866406745008, 1, 0, -15120], 5)
    return do_func1_tests(int_list, expected)

def do_func2_tests(dict1, expected):
    res = program.func2(dict1)
    if res == None:
        raise testlib.NotImplemented()
    testlib.check_val(res, expected)
    return 0.5

def test_func2_1():
    '''
    dict1 = {"a" : [3, 2, 2], "b" : [4, 2, 3], "c" : [-4, 2, 2]}
    expected =  "b"
    '''
    dict1 = {"a" : [3, 2, 2], "b" : [4, 2, 3], "c" : [-4, 2, 2]}
    expected =  "b"
    return do_func2_tests(dict1, expected)

def test_func2_2():
    '''
    dict1 = {"a" : [3, 2, 2, -1, -1], "b" : [4, 2, 3, -4], "c" : [-4, 2, 2]}
    expected =  "a"
    '''
    dict1 = {"a" : [3, 2, 2, -1, -1], "b" : [4, 2, 3, -4], "c" : [-4, 2, 2]}
    expected =  "a"
    return do_func2_tests(dict1, expected)

def test_func2_3():
    '''
    dict1 = {"C" : [1, 1, 1, 1, 1, 1], "b" : [6]}
    expected =  "C"
    '''
    dict1 = {"C" : [1, 1, 1, 1, 1, 1], "b" : [6]}
    expected =  "C"
    return do_func2_tests(dict1, expected)

def test_func2_4():
    '''
    dict1 = {"C" : [0], "B" : [1], "A" : [1, -1, 1, -1, 1, -1, 1, -1, 1], "a" : [-1]}
    expected =  "A"
    '''
    dict1 = {"C" : [0], "B" : [1], "A" : [1, -1, 1, -1, 1, -1, 1, -1, 1], "a" : [-1]}
    expected =  "A"
    return do_func2_tests(dict1, expected)


def do_func3_tests(list_a, list_b, expected):
    res = program.func3(list_a, list_b)
    if res == None:
        raise testlib.NotImplemented()
    testlib.check_val(res, expected)
    return 0.5


def test_func3_1():
    '''
    list_A = ["flash", "ColA", "USED", "lazer"]
    list_B = ["Rabit", "HELIOS", "trick", "suPER"]
    expected = ['a', 'lo', '', 'er']
    '''
    list_A = ["flash", "ColA", "USED", "lazer"]
    list_B = ["Rabit", "HELIOS", "trick", "suPER"]
    expected = ['a', 'lo', '', 'er']
    return do_func3_tests(list_A, list_B, expected)

def test_func3_2():
    '''
    list_A = ["RAM", "rom", "JaM", "leAP", "star"]
    list_B = ["", "aBcDeFgH", "aBcDeFgH", "aBcDeFgH", "aBcDeFgH"]
    expected = ['', '', 'a', 'ae', 'a']
    '''
    list_A = ["RAM", "rom", "JaM", "leAP", "star"]
    list_B = ["", "aBcDeFgH", "aBcDeFgH", "aBcDeFgH", "aBcDeFgH"]
    expected = ['', '', 'a', 'ae', 'a']
    return do_func3_tests(list_A, list_B, expected)

def test_func3_3():
    '''
    list_A = ["abcdefghijklmnopqrstuwxyz", "abcdefghijklmnopqrstuwxyz"]
    list_B = ["ZYXWUTSRQPONMLKJIHGFEDCBA", "zyxwutsrqponmlkjihgfedcba"]
    expected = ['abcdefghijklmnopqrstuwxyz', 'abcdefghijklmnopqrstuwxyz']
    '''
    list_A = ["abcdefghijklmnopqrstuwxyz", "abcdefghijklmnopqrstuwxyz"]
    list_B = ["ZYXWUTSRQPONMLKJIHGFEDCBA", "zyxwutsrqponmlkjihgfedcba"]
    expected = ['abcdefghijklmnopqrstuwxyz', 'abcdefghijklmnopqrstuwxyz']
    return do_func3_tests(list_A, list_B, expected)

def test_func3_4():
    '''
    list_A = ["catode", "dermatoglyphics", "uncopyrightable"]
    list_B = ["ZYXWUTSRQPONMLKJIHGFEDCBA", "zyxwutsrqponmlkjihgfedcba", "zyxwutsrqponmlkjihgfedcba"]
    expected = ['acdeot', 'acdeghilmoprsty', 'abceghilnoprtuy']
    '''
    list_A = ["catode", "dermatoglyphics", "uncopyrightable"]
    list_B = ["ZYXWUTSRQPONMLKJIHGFEDCBA", "zyxwutsrqponmlkjihgfedcba", "zyxwutsrqponmlkjihgfedcba"]
    expected = ['acdeot', 'acdeghilmoprsty', 'abceghilnoprtuy']
    return do_func3_tests(list_A, list_B, expected)


# ----------------------------------- EX.1 ----------------------------------- #

def do_func4_tests(ID, expected):
    input_filename  = f'func4/in_example{ID}.txt'
    output_filename = f'func4/out_example{ID}.txt'
    expected_filename = f'func4/exp_example{ID}.txt'
    res = program.func4(input_filename, output_filename)
    if res == None:
        raise testlib.NotImplemented()
    testlib.check_val(res, expected)
    testlib.check_text_file(output_filename, expected_filename)
    return 1.5


def test_func4_1():
    '''
    input_filename = 'func4/in_example1.txt'
    ouput_filename = 'func4/out_example1.txt'
    expected_filename = 'func4/exp_example1.txt'
    expected = 5
    '''
    ID = 1
    expected = 5
    return do_func4_tests(ID, expected)

def test_func4_2():
    '''
    input_filename = 'func4/in_example2.txt'
    ouput_filename = 'func4/out_example2.txt'
    expected_filename = 'func4/exp_example2.txt'
    expected = 26
    '''
    ID = 2
    expected = 26
    return do_func4_tests(ID, expected)


def test_func4_3():
    '''
    input_filename = 'func4/in_example3.txt'
    ouput_filename = 'func4/out_example3.txt'
    expected_filename = 'func4/exp_example3.txt'
    expected = 7
    '''
    ID = 3
    expected = 7
    return do_func4_tests(ID, expected)

def test_func4_4():
    '''
    input_filename = 'func4/in_example4.txt'
    ouput_filename = 'func4/out_example4.txt'
    expected_filename = 'func4/exp_example4.txt'
    expected = 4
    '''
    ID = 4
    expected = 4
    return do_func4_tests(ID, expected)

def do_test_func5(ID, expected):
    img_in = f'func5/func5_test{ID}.png'
    img_out = f'func5/func5_out{ID}.png'
    img_exp = f'func5/func5_exp{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(img_in, img_out)
    if res == None:
        raise testlib.NotImplemented()
    testlib.check_val(res, expected, f'''{'*'*50}\n[ERROR] Il numero di segmenti colorati è sbagliato! / The number of colored segments is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1():
    '''
    imagefile = func5/func5_test1.png
    output_imagefile = func5/func5_out1.png
    '''
    ID = 1
    expected = 12
    return do_test_func5(ID, expected)


def test_func5_2():
    '''
    imagefile = func5/func5_test2.png
    output_imagefile = func5/func5_out2.png
    color = (255,0,0)
    '''
    ID = 2
    expected = 11
    return do_test_func5(ID, expected)


def test_func5_3():
    '''
    imagefile = func5/func5_test3.png
    output_imagefile = func5/func5_out3.png
    '''
    ID = 3
    expected = 73
    return do_test_func5(ID, expected)


def test_func5_4():
    '''
    imagefile = func5/func5_test4.png
    output_imagefile = func5/func5_out4.png
    '''
    ID = 4
    expected = 143
    return do_test_func5(ID, expected)
# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(dirin, expected):
    res = program.ex1(dirin)
    if res == None:
        raise testlib.NotImplemented()
    testlib.check_list(res, expected)
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(dirin)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    return 2

def test_ex1_1():
    '''
    dirin = 'ex1/A'
    expected = [('ex1/A', 3), ('ex1/A/B', 2), ('ex1/A/B/C', 2), ('ex1/A/D', 2), ('ex1/A/E', 1)]
    '''
    dirin = 'ex1/A'
    expected = [('ex1/A', 3), ('ex1/A/B', 2), ('ex1/A/B/C', 2), ('ex1/A/D', 2), ('ex1/A/E', 1)]
    return do_test_ex1(dirin, expected)

def test_ex1_2():
    '''
    dirin = 'ex1/abracadabra'
    expected = [('ex1/abracadabra/prog2', 3), ('ex1/abracadabra/prog2/CCC/eeee', 3), ('ex1/abracadabra', 2), ('ex1/abracadabra/prog2/CCC/ttttttt/help', 2), ('ex1/abracadabra/prog2/EEE/x', 1), ('ex1/abracadabra/prog3/c', 1), ('ex1/abracadabra/prog3/d', 1), ('ex1/abracadabra/prog3/e', 1), ('ex1/abracadabra/prog1', 0), ('ex1/abracadabra/prog2/AAA', 0), ('ex1/abracadabra/prog2/BBB', 0), ('ex1/abracadabra/prog2/CCC', 0), ('ex1/abracadabra/prog2/CCC/fffffff', 0), ('ex1/abracadabra/prog2/CCC/ttttttt', 0), ('ex1/abracadabra/prog2/DDD', 0), ('ex1/abracadabra/prog2/EEE', 0), ('ex1/abracadabra/prog3', 0), ('ex1/abracadabra/prog3/a', 0), ('ex1/abracadabra/prog3/b', 0)]
    '''
    dirin = 'ex1/abracadabra'
    expected = [('ex1/abracadabra/prog2', 3), ('ex1/abracadabra/prog2/CCC/eeee', 3), ('ex1/abracadabra', 2), ('ex1/abracadabra/prog2/CCC/ttttttt/help', 2), ('ex1/abracadabra/prog2/EEE/x', 1), ('ex1/abracadabra/prog3/c', 1), ('ex1/abracadabra/prog3/d', 1), ('ex1/abracadabra/prog3/e', 1), ('ex1/abracadabra/prog1', 0), ('ex1/abracadabra/prog2/AAA', 0), ('ex1/abracadabra/prog2/BBB', 0), ('ex1/abracadabra/prog2/CCC', 0), ('ex1/abracadabra/prog2/CCC/fffffff', 0), ('ex1/abracadabra/prog2/CCC/ttttttt', 0), ('ex1/abracadabra/prog2/DDD', 0), ('ex1/abracadabra/prog2/EEE', 0), ('ex1/abracadabra/prog3', 0), ('ex1/abracadabra/prog3/a', 0), ('ex1/abracadabra/prog3/b', 0)]
    return do_test_ex1(dirin, expected)


def test_ex1_3():
    '''
    dirin = 'ex1/1'
    expected = [('ex1/1/2/1', 2), ('ex1/1/3', 2), ('ex1/1', 0), ('ex1/1/2', 0), ('ex1/1/2/2', 0), ('ex1/1/3/q', 0), ('ex1/1/4', 0)]
    '''
    dirin = 'ex1/1'
    expected = [('ex1/1/2/1', 2), ('ex1/1/3', 2), ('ex1/1', 0), ('ex1/1/2', 0), ('ex1/1/2/2', 0), ('ex1/1/3/q', 0), ('ex1/1/4', 0)]
    return do_test_ex1(dirin, expected)



# ----------------------------------- EX. 2----------------------------------- #


def do_ex2_test(root, expected):
    res = program.ex2(root)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR]Il valore ritornato non è corretto! / The returned value is incorrect!!\nReturned={res}, expected={expected}''')
        return 0
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(root)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)
    return 2


def test_ex2_1():
    '''
        root      
    ______25______ 
   |             |  
   8__        ___2___ 
      |      |       |  
      3      9       1  

      expected = (3, 1, 2)
    '''
    root = tree.BinaryTree.fromList([25, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
    expected = (3, 1, 2)
    return do_ex2_test(root, expected)

def test_ex2_2():
    '''
              root       
          ______2______  
         |             | 
      __ 7__        ___15___  
     |      |      |       | 
    _4_     3_    _0_     _5_  
   |   |      |  |   |   |   | 
   2   -1     1  8   3   2  -9 

       expected = (7, 1, 6)
    '''
    root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [15, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [-9, None, None]]]])
    expected =  (7, 1, 6)
    return do_ex2_test(root, expected)


def test_ex2_3():
    '''
    A big tree
    expected = (137, 80, 136)
    '''
    root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    expected = (137, 80, 136)
    return do_ex2_test(root, expected)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,  test_ex1_2, test_ex1_3,
    test_ex2_1,    test_ex2_2, test_ex2_3,
    test_personal_data_entry,
]


if __name__ == '__main__':
    try:
        test_personal_data_entry()
    except AssertionError as e:
        print(e)
        my_print(f'\n{COL["RED"]}{COL["BOLD"]}Dati personali mancanti: test non eseguiti! / Personal data missing: test not executed!{COL["RST"]}')
        exit(0)
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
    grades = {}
    total  = 0

    with open('grade.csv') as F:
        for line in F:
            test, points = line.split(',')
            _, name, *_ = test.split('_')
            if name == 'personal': continue
            total += float(points)
            grades[name] = grades.get(name, 0) + float(points)
    #%% Constraint for the exam
    constraint1 = len([name for name,grade in grades.items() if grade>0 and name.startswith('func')]) >= 3
    constraint2 = len([name for name,grade in grades.items() if grade>0 and name.startswith('ex')]) >= 1
    constraint3 = total >= 18
    constraint4 = all((constraint1, constraint2, constraint3))
    if not constraint1:
        print(f'YOU HAVE NOT PASSED AT LEAST 3 FUNC EXERCISES: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint2:
        print(f'YOU HAVE NOT PASSED AT LEAST 1 RECURSIVE EXERCISE: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint3:
        print(f'THE FINAL GRADE IS LESS THAN 18: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    else:
        print(f"YOU HAVE {COL['GREEN']}PASSED{COL['RST']} THE EXAM WITH {COL['BOLD']+COL['GREEN']}{total}{COL['RST']} POINTS")
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    print(f"Three func problems solved:  {COL['BOLD']} {COL['GREEN'] if constraint1 else COL['RED']} {constraint1}{COL['RST']}{COL['ENDC']}")
    print(f"One ex problem solved:       {COL['BOLD']} {COL['GREEN'] if constraint2 else COL['RED']} {constraint2}{COL['RST']}{COL['ENDC']} ")
    print(f"Total >= 18:                 {COL['BOLD']} {COL['GREEN'] if constraint3 else COL['RED']} {constraint3}{COL['RST']}{COL['ENDC']}")
    print(f"Exam passed:                 {COL['BOLD']} {COL['GREEN'] if constraint4 else COL['RED']} {constraint4}{COL['RST']}{COL['ENDC']}")
################################################################################
