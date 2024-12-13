# -*- coding: utf-8 -*-
import testlib
from testlib import my_print, COL
import isrecursive
import os
import sys
import glob
import hashlib

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program


def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        col = ''
        if any(err in args[0] for err in ['[OK]', 'Correct']):
            col = COL['GREEN']
        if any(err in args[0] for err in ['error', 'Error', 'ERROR', ]):
            col = COL['RED']
        return func(f'{COL["BOLD"]}{col}', *args, f'{COL["RST"]}{COL["ENDC"]}',
                    **kwargs, )

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
# %% ---------------------- DEBUG VARIABLE -------------------
DEBUG = True
# DEBUG = False

COL = {'RED': '\u001b[31m',
       'RST': '\u001b[0m',
       'GREEN': '\u001b[32m',
       'YELLOW': '\u001b[33m',
       'BOLD': '\033[1m',
       'ENDC': '\033[0m'}


def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'MATRICULATION NUMBER', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py{COL['RST']}"
    else:
        assert program.nome != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    return 1e-9


#############################################################################
# %% ---------------------- TEST SECTION -------------------
#############################################################################

# Test per func1
def test_func1_1():
    board = {(0, 0): "S", (1, 1): "X", (2, 9): "O"}
    expected = ('|S| | | | | | | | | |\n'
                '| |X| | | | | | | | |\n'
                '| | | | | | | | | |O|\n'
                '| | | | | | | | | | |\n'
                '| | | | | | | | | | |\n'
                '| | | | | | | | | | |\n'
                '| | | | | | | | | | |\n'
                '| | | | | | | | | | |\n'
                '| | | | | | | | | | |\n'
                '| | | | | | | | | | |')
    result = program.func1(board, 10)
    testlib.check_expected()
    assert result == expected, f"Errore in func1: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func1_2():
    board = {}
    expected = ""
    result = program.func1(board, 0)
    assert result == expected, f"Errore in func1: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func1_3():
    board = {(5, 5): "X", (5, 6): "X", (5, 7): "O"}
    expected = ('| | | | | | | | |\n'
                '| | | | | | | | |\n'
                '| | | | | | | | |\n'
                '| | | | | | | | |\n'
                '| | | | | | | | |\n'
                '| | | | | |X|X|O|\n'
                '| | | | | | | | |\n'
                '| | | | | | | | |')
    result = program.func1(board, 8)
    assert result == expected, f"Errore in func1: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func1_4():
    board = {
        (0, 0): "X", (0, 9): "X", (9, 0): "X", (9, 9): "X",
        # angoli della board
        (5, 5): "X", (3, 4): "X", (6, 7): "X"  # posizioni centrali sparse
    }
    expected = ('|X| | | | | | | | |X|\n'
                '| | | | | | | | | | |\n'
                '| | | | | | | | | | |\n'
                '| | | | |X| | | | | |\n'
                '| | | | | | | | | | |\n'
                '| | | | | |X| | | | |\n'
                '| | | | | | | |X| | |\n'
                '| | | | | | | | | | |\n'
                '| | | | | | | | | | |\n'
                '|X| | | | | | | | |X|')
    result = program.func1(board, 10)
    assert result == expected, f"Errore in func1: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func1_5():
    board = {(0, 0): "O"}
    expected = '|O|'
    result = program.func1(board, 1)
    assert result == expected, f"Errore in func1: atteso {expected}, ottenuto {result}"
    return 1.5


# Test per func2
def test_func2_1():
    input_string = "Fregata:2,3:H:4;Fregata:3,3:H:4"
    expected = [{'lunghezza': '4', 'nome': 'Fregata', 'orientamento': 'H',
                 'posizione': '2,3'},
                {'lunghezza': '4', 'nome': 'Fregata', 'orientamento': 'H',
                 'posizione': '3,3'}]
    result = program.func2(input_string)
    assert result == expected, f"Errore in func2: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func2_2():
    input_string = ""
    expected = []
    result = program.func2(input_string)
    assert result == expected, f"Errore in func2: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func2_3():
    input_string = "Fregata:2,2:V:3"
    expected = [{'lunghezza': '3', 'nome': 'Fregata', 'orientamento': 'V',
                 'posizione': '2,2'}]
    result = program.func2(input_string)
    assert result == expected, f"Errore in func2: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func2_4():
    input_string = "Destroyer:0,0:H:5;Frigate:0,0:V:10"  # sovrapposizione
    expected = [{'lunghezza': '5',
                 'nome': 'Destroyer',
                 'orientamento': 'H',
                 'posizione': '0,0'},
                {'lunghezza': '10',
                 'nome': 'Frigate',
                 'orientamento': 'V',
                 'posizione': '0,0'}]
    result = program.func2(input_string)
    assert result == expected, f"Errore in func2: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func2_5():
    input_string = ""
    expected = []
    result = program.func2(input_string)
    assert result == expected, f"Errore in func2: atteso {expected}, ottenuto {result}"
    return 1.5


# Test per func3
def test_func3_1():
    lista_navi = [
        {'nome': 'Fregata', 'posizione': (2, 3), 'orientamento': 'H',
         'lunghezza': 2},
        {'nome': 'Sottomarino', 'posizione': (4, 4), 'orientamento': 'V',
         'lunghezza': 3},
        {'nome': 'Sottomarino', 'posizione': (7, 4), 'orientamento': 'V',
         'lunghezza': 3},
        {'nome': 'Torpediniere', 'posizione': (3, 6), 'orientamento': 'H',
         'lunghezza': 3},
        {'nome': 'Torpediniere', 'posizione': (5, 8), 'orientamento': 'V',
         'lunghezza': 3},
        {'nome': 'Cacciatorpediniere', 'posizione': (0, 0), 'orientamento': 'H',
         'lunghezza': 4},
        {'nome': 'Portaerei', 'posizione': (6, 1), 'orientamento': 'V',
         'lunghezza': 5}
    ]
    result = program.func3(lista_navi)
    assert result is True, "Errore in func3: atteso True, ottenuto False"
    return 1.5


def test_func3_2():
    lista_navi = [
        {'nome': 'Sopramarino', 'posizione': (0, 0), 'orientamento': 'V',
         'lunghezza': 10}]
    result = program.func3(lista_navi)
    assert result is False, "Errore in func3: atteso False, ottenuto True"
    return 1.5


def test_func3_3():
    lista_navi = []
    result = program.func3(lista_navi)
    assert result is False, "Errore in func3: atteso False, ottenuto False"
    return 1.5


def test_func3_4():
    lista_navi = [
        {'nome': 'Fregata', 'posizione': (2, 3), 'orientamento': 'H',
         'lunghezza': 2},
        {'nome': 'Submarine', 'posizione': (4, 4), 'orientamento': 'V',
         'lunghezza': 3},
        {'nome': 'Sottomarino', 'posizione': (7, 4), 'orientamento': 'V',
         'lunghezza': 3},
        {'nome': 'Torpediniere', 'posizione': (3, 6), 'orientamento': 'H',
         'lunghezza': 3},
        {'nome': 'Torpediniere', 'posizione': (5, 8), 'orientamento': 'V',
         'lunghezza': 3},
        {'nome': 'Cacciatorpediniere', 'posizione': (0, 0), 'orientamento': 'H',
         'lunghezza': 4},
        {'nome': 'Portaerei', 'posizione': (6, 1), 'orientamento': 'V',
         'lunghezza': 5}
    ]
    result = program.func3(lista_navi)
    assert result is False, "Errore in func3: atteso False, ottenuto True"
    return 1.5


def test_func3_5():
    lista_navi = [
        {'nome': 'Fregata', 'posizione': (2, 3), 'orientamento': 'H',
         'lunghezza': 2},
        {'nome': 'Sottomarino', 'posizione': (4, 4), 'orientamento': 'V',
         'lunghezza': 3},
        {'nome': 'Sottomarino', 'posizione': (7, 4), 'orientamento': 'V',
         'lunghezza': 3},
        {'nome': 'Torpediniere', 'posizione': (3, 6), 'orientamento': 'H',
         'lunghezza': 3},
        {'nome': 'Torpediniere', 'posizione': (5, 8), 'orientamento': 'V',
         'lunghezza': 3},
        {'nome': 'Cacciatorpediniere', 'posizione': (0, 0), 'orientamento': 'H',
         'lunghezza': 4},
        {'nome': 'Portaerei', 'posizione': (6, 1), 'orientamento': 'V',
         'lunghezza': 1},
        {'nome': 'Portaerei', 'posizione': (6, 1), 'orientamento': 'V',
         'lunghezza': 1}
    ]
    result = program.func3(lista_navi)
    assert result is False, "Errore in func3: atteso False, ottenuto True"
    return 1.5


# Test per func4
def test_func4_1():
    lista_navi = [
        {"nome": "Sottomarino", "posizione": (1, 1), "orientamento": "V",
         "lunghezza": 3},
        {"nome": "Fregata", "posizione": (0, 1), "orientamento": "V",
         "lunghezza": 3}
    ]
    expected = {(1, 1), (2, 1)}
    result = program.func4(lista_navi)
    assert result == expected, f"Errore in func4: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func4_2():
    lista_navi = []
    expected = set()
    result = program.func4(lista_navi)
    assert result == expected, f"Errore in func4: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func4_3():
    lista_navi = [
        {"nome": "Destroyer", "posizione": (5, 5), "orientamento": "H",
         "lunghezza": 2}]
    expected = set()
    result = program.func4(lista_navi)
    assert result == expected, f"Errore in func4: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func4_4():
    lista_navi = [
        {"nome": "Submarine", "posizione": (0, 0), "orientamento": "V",
         "lunghezza": 2},
        {"nome": "Destroyer", "posizione": (2, 0), "orientamento": "H",
         "lunghezza": 3},
        {"nome": "Frigate", "posizione": (1, 2), "orientamento": "H",
         "lunghezza": 4}
    ]  # navi adiacenti ma non sovrapposte
    expected = set()
    result = program.func4(lista_navi)
    assert result == expected, f"Errore in func4: atteso {expected}, ottenuto {result}"
    return 1.5


def test_func4_5():
    lista_navi = [
        {"nome": "Submarine", "posizione": (0, 0), "orientamento": "V",
         "lunghezza": 5},  # nave che si estende fino al limite
        {"nome": "Destroyer", "posizione": (2, 0), "orientamento": "H",
         "lunghezza": 3},
    ]
    expected = {(2, 0)}
    result = program.func4(lista_navi)
    assert result == expected, f"Errore in func4: atteso {expected}, ottenuto {result}"
    return 1.5


################################################################################
# %% --------------------- TESTS ---------------------
tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti

    test_personal_data_entry,
    test_func1_1, test_func1_2, test_func1_3, test_func1_4, test_func1_5, # 7.5 punti
    test_func2_1, test_func2_2, test_func2_3, test_func2_4, test_func2_5, # 7.5 punti
    test_func3_1, test_func3_2, test_func3_3, test_func3_4, test_func3_5, # 7.5 punti
    test_func4_1, test_func4_2, test_func4_3, test_func4_4, test_func4_5, # 7.5 punti
]


def check_expected():
    files = glob.glob('backup/**', recursive=True)
    # print(*files, sep='\n')
    for file_b in files:
        if os.path.isfile(file_b):
            file_e = '/'.join(file_b.split('/')[1:])
            with open(file_b, mode='rb') as frb, open(file_e, mode='rb') as fre:
                assert hashlib.md5(frb.read()).hexdigest() == hashlib.md5(
                    fre.read()).hexdigest(), \
                    (
                        f"{COL['BOLD']} {COL['RED']}\nWARNING: an expected or input file has been overwritten by mistake!\n"
                        f"expected/input file: {file_e}\ndiffers from:        {file_b}\nWe cannot evaluate your exam,"
                        f"please call the lecturer to fix the issue!{COL['RST']}{COL['ENDC']}")


# %% --------------------- MAIN ---------------------
if __name__ == '__main__':
    test_personal_data_entry()
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
