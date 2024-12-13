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


def do_func1_tests(int_list, n, expected):
    res = program.func1(int_list, n)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_dict(res, expected)
    return 0.5


def test_func1_1():
    '''
    int_list = [4, 4, 10, 4, 2, 1, 2]
    n = 2
    expected = {4: 3, 2: 2}
    '''
    int_list = [4, 4, 10, 4, 2, 1, 2]
    n = 2
    expected = {4: 3, 2: 2}
    return do_func1_tests(int_list, n, expected)

def test_func1_2():
    '''
    int_list = [-5, 4, 5, 10, 3, -1, 2, 12]
    n = 1
    expected = {-5: 1, 4: 1, 5: 1, 10: 1, 3: 1, -1: 1, 2: 1, 12: 1}
    '''
    int_list = [-5, 4, 5, 10, 3, -1, 2, 12]
    n = 1
    expected = {-5: 1, 4: 1, 5: 1, 10: 1, 3: 1, -1: 1, 2: 1, 12: 1}
    return do_func1_tests(int_list, n, expected)

def test_func1_3():
    '''
    int_list = []
    n = 5
    expected = {}
    '''
    int_list = []
    n = 5
    expected = {}
    return do_func1_tests(int_list, n, expected)

def test_func1_4():
    '''
    int_list = [-78, 10, 76, 82, -27, -39, -65, -19, 74, 18, 20, -25, -38, -71, -52, -49, -69, 21, -27, 58, 20]
    n = 2
    expected = {-27: 2, 20: 2}
    '''
    int_list = [-78, 10, 76, 82, -27, -39, -65, -19, 74, 18, 20, -25, -38, -71, -52, -49, -69, 21, -27, 58, 20]
    n = 2
    expected = {-27: 2, 20: 2}
    return do_func1_tests(int_list, n, expected)

def do_func2_tests(dict1, a, b, expected):
    res = program.func2(dict1, a, b)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_list(res, expected)
    return 0.5

def test_func2_1():
    '''
    dict1 = {'Car':'GoOd', 'floor':'bAd', 'Wild':'EXCELLENT', 'air':'Bad', 'cocoon':'greaT'}
    a = 'c'
    b = 'G'
    expected =  ['greaT', 'GoOd', 'bAd']
    '''
    dict1 = {'Car':'GoOd', 'floor':'bAd', 'Wild':'EXCELLENT', 'air':'Bad', 'cocoon':'greaT'}
    a = 'c'
    b = 'G'
    expected =  ['greaT', 'GoOd', 'bAd']
    return do_func2_tests(dict1, a, b, expected)

def test_func2_2():
    '''
    dict1 = {'gkvmhswher': 'jpmiixfse', 'vgnClc': 'pvherjaAi', 'Dffqild': 'eiqkBukno', 'gpjhpbmhuc': 'dlje', 'ijeAts': 'Bmknpf', 'lkqpygg': 'czqEBku'}
    a = 'A'
    b = 'Z'
    expected = ['eiqkBukno', 'jpmiixfse', 'pvherjaAi', 'czqEBku', 'Bmknpf', 'dlje']
    '''
    dict1 = {'gkvmhswher': 'jpmiixfse', 'vgnClc': 'pvherjaAi', 'Dffqild': 'eiqkBukno', 'gpjhpbmhuc': 'dlje', 'ijeAts': 'Bmknpf', 'lkqpygg': 'czqEBku'}
    a = 'A'
    b = 'Z'
    expected = ['eiqkBukno', 'jpmiixfse', 'pvherjaAi', 'czqEBku', 'Bmknpf', 'dlje']
    return do_func2_tests(dict1, a, b, expected)

def test_func2_3():
    '''
    dict1 = {'gkvmhswher': 'jpmiixfse', 'vgnClc': 'pvherjaAi', 'Dffqild': 'eiqkBukno', 'gpjhpbmhuc': 'dlje', 'ijeAts': 'Bmknpf', 'lkqpygg': 'czqEBku'}
    a = 'A'
    b = 'B'
    expected = []
    '''
    dict1 = {'gkvmhswher': 'jpmiixfse', 'vgnClc': 'pvherjaAi', 'Dffqild': 'eiqkBukno', 'gpjhpbmhuc': 'dlje', 'ijeAts': 'Bmknpf', 'lkqpygg': 'czqEBku'}
    a = 'A'
    b = 'B'
    expected = []
    return do_func2_tests(dict1, a, b, expected)

def test_func2_4():
    '''
    dict1 = {'juo': 'eoiCi', 'helepu': 'ombhc', 'rijKmhiv': 'rkhQi', 'pfqjqoku': 'zine', 'sjDgwprj': 'xJmKDux', 'Jjjoseghdy': 'jmmnhm', 'jFv': 'frlpn', 'Icjcpgom': 'efmghlwAt', 'lgrldmkab': 'llpegktnqc', 'esqgL': 'fktogGs'}
    a = 'j'
    b = 'j'
    expected = ['jmmnhm',  'eoiCi', 'frlpn']
    '''
    dict1 = {'juo': 'eoiCi', 'helepu': 'ombhc', 'rijKmhiv': 'rkhQi', 'pfqjqoku': 'zine', 'sjDgwprj': 'xJmKDux', 'Jjjoseghdy': 'jmmnhm', 'jFv': 'frlpn', 'Icjcpgom': 'efmghlwAt', 'lgrldmkab': 'llpegktnqc', 'esqgL': 'fktogGs'}
    a = 'j'
    b = 'j'
    expected = ['jmmnhm',  'eoiCi', 'frlpn']
    return do_func2_tests(dict1, a, b, expected)


def do_func3_tests(str1, str2, expected):
    res = program.func3(str1, str2)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_val(res, expected)
    return 0.5


def test_func3_1():
    '''
    str1 = 'gLIde'
    str2 = 'yoWLS'
    expected = 'GSlLiWDoEy'
    '''
    str1 = 'gLIde'
    str2 = 'yoWLS'
    expected = 'GSlLiWDoEy'
    return do_func3_tests(str1, str2, expected)

def test_func3_2():
    '''
    str1 = 'StaIrcAses'
    str2 = 'granulates'
    expected = 'ssTeAtiaRlCuanSaErSg'
    '''
    str1 = 'StaIrcAses'
    str2 = 'granulates'
    expected = 'ssTeAtiaRlCuanSaErSg'
    return do_func3_tests(str1, str2, expected)

def test_func3_3():
    '''
    str1 = 'infaTuAtION'
    str2 = 'IntANGIbLenESS'
    expected = 'ISNSFEAnteULabTIiGoNnA'
    '''
    str1 = 'infaTuAtION'
    str2 = 'IntANGIbLenESS'
    expected = 'ISNSFEAnteULabTIiGoNnA'
    return do_func3_tests(str1, str2, expected)

def test_func3_4():
    '''
    str1 = 'delIberAtIVelY',
    str2 = 'ReproductIvE'
    expected = 'DEEvLIitBcEuRdaoTripveER'
    '''
    str1 = 'delIberAtIVelY'
    str2 = 'ReproductIvE'
    expected = 'DEEvLIitBcEuRdaoTripveER'
    return do_func3_tests(str1, str2, expected)


# ----------------------------------- EX.1 ----------------------------------- #

def do_func4_tests(ID, length, expected):
    input_filename  = f'func4/func4_test{ID}.txt'
    output_filename = f'func4/func4_out{ID}.txt'
    expected_filename = f'func4/func4_exp{ID}.txt'
    res = program.func4(input_filename, output_filename, length)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_dict(res, expected)
    testlib.check_text_file(output_filename, expected_filename)
    return 2


def test_func4_1():
    '''
    input_filename = 'func4/func4_test1.txt'
    ouput_filename = 'func4/func4_out1.txt'
    expr = 'CAt'
    expected_filename = 'func4/func4_exp1.txt'
    expected = {1: (15, 3, 6), 3: (11, 3, 2)}
    '''
    ID = 1
    expr = 'CAt'
    expected = {1: (15, 3, 6), 3: (11, 3, 2)}
    return do_func4_tests(ID, expr, expected)

def test_func4_2():
    '''
    input_filename = 'func4/func4_test2.txt'
    ouput_filename = 'func4/func4_out2.txt'
    expr = 'expECTED'
    expected_filename = 'func4/func4_exp2.txt'
    expected = {1: (42, 4, 9), 5: (41, 5, 9), 9: (20, 2, 3), 18: (29, 3, 8)}
    '''
    ID = 2
    expr = 'expECTED'
    expected = {1: (42, 4, 9), 5: (41, 5, 9), 9: (20, 2, 3), 18: (29, 3, 8)}
    return do_func4_tests(ID, expr, expected)


def test_func4_3():
    '''
    input_filename = 'func4/func4_test3.txt'
    ouput_filename = 'func4/func4_out3.txt'
    expr = 'noGgINS'
    expected_filename = 'func4/func4_exp3.txt'
    expected = {2: (8, 1, 1), 3: (134, 12, 12), 4: (30, 3, 5), 11: (8, 1, 1), 14: (76, 7, 11), 18: (49, 5, 6), 19: (21, 2, 3)}
    '''
    ID = 3
    expr = 'noGgINS'
    expected = {2: (8, 1, 1), 3: (134, 12, 12), 4: (30, 3, 5), 11: (8, 1, 1), 14: (76, 7, 11), 18: (49, 5, 6), 19: (21, 2, 3)}
    return do_func4_tests(ID, expr, expected)

def do_test_func5(ID, expected):
    img_in = f'func5/img{ID}_in.png'
    img_out = f'func5/img{ID}_out.png'
    img_exp = f'func5/img{ID}_exp.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(img_in, img_out)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_val(res, expected)
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1():
    '''
    imagefile = func5/img1_in.png
    output_imagefile = func5/img1_out.png
    '''
    ID = 1
    expected = 13
    return do_test_func5(ID, expected)


def test_func5_2():
    '''
    imagefile = func5/img2_in.png
    output_imagefile = func5/img2_out.png
    '''
    ID = 2
    expected = 2
    return do_test_func5(ID, expected)


def test_func5_3():
    '''
    imagefile = func5/img3_in.png
    output_imagefile = func5/img3_out.png
    '''
    ID = 3
    expected = 0
    return do_test_func5(ID, expected)


def test_func5_4():
    '''
    imagefile = func5/img4_in.png
    output_imagefile = func5/img4_out.png
    '''
    ID = 4
    expected = 15686
    return do_test_func5(ID, expected)



# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(dirin, expected):
    res = program.ex1(dirin)
    if res == None:
        raise testlib.NotImplemented
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
    expected = ['ex1/A/B/3odd74B.txt', 'ex1/A/C/e3dd7Ag22.txt', 'ex1/A/3cmi4G3ev.txt', 'ex1/A/gkfep28.txt', 'ex1/A/C/n3ks22.txt']
    '''
    dirin = 'ex1/A'
    expected = ['ex1/A/B/3odd74B.txt', 'ex1/A/C/e3dd7Ag22.txt', 'ex1/A/3cmi4G3ev.txt', 'ex1/A/gkfep28.txt', 'ex1/A/C/n3ks22.txt']
    return do_test_ex1(dirin, expected)

def test_ex1_2():
    '''
    dirin = 'ex1/B'
    expected = ['ex1/B/k5B3.txt', 'ex1/B/gn9.txt', 'ex1/B/2kdt437mi.txt', 'ex1/B/gem4.txt', 'ex1/B/DBvt2h4/8q2i3cb/37d4og.txt', 'ex1/B/hfc44ba/B7n33lv/gl88e642/3f8g.txt', 'ex1/B/DBvt2h4/8q2i3cb/qjc.txt', 'ex1/B/DBvt2h4/8q2i3cb/y4fcG6.txt', 'ex1/B/DBvt2h4/yr3ao93533.txt', 'ex1/B/hfc44ba/e7md39.txt', 'ex1/B/Ap81l6Cch.txt', 'ex1/B/vjv28.txt', 'ex1/B/hfc44ba/fm45.txt', 'ex1/B/DBvt2h4/55i4q73/5f4oxdfk.txt', 'ex1/B/DBvt2h4/5nfhb6adjd/1fe.txt', 'ex1/B/DBvt2h4/5nfhb6adjd/55Qbbc5t8m.txt', 'ex1/B/DBvt2h4/55i4q73/i5233.txt', 'ex1/B/DBvt2h4/8q2i3cb/33q.txt', 'ex1/B/DBvt2h4/8q2i3cb/pebd42g5B.txt', 'ex1/B/DBvt2h4/v1ahd.txt', 'ex1/B/hfc44ba/ummc6eb93/844d9i.txt']
    '''
    dirin = 'ex1/B'
    expected = ['ex1/B/k5B3.txt', 'ex1/B/gn9.txt', 'ex1/B/2kdt437mi.txt', 'ex1/B/gem4.txt', 'ex1/B/DBvt2h4/8q2i3cb/37d4og.txt', 'ex1/B/hfc44ba/B7n33lv/gl88e642/3f8g.txt', 'ex1/B/DBvt2h4/8q2i3cb/qjc.txt', 'ex1/B/DBvt2h4/8q2i3cb/y4fcG6.txt', 'ex1/B/DBvt2h4/yr3ao93533.txt', 'ex1/B/hfc44ba/e7md39.txt', 'ex1/B/Ap81l6Cch.txt', 'ex1/B/vjv28.txt', 'ex1/B/hfc44ba/fm45.txt', 'ex1/B/DBvt2h4/55i4q73/5f4oxdfk.txt', 'ex1/B/DBvt2h4/5nfhb6adjd/1fe.txt', 'ex1/B/DBvt2h4/5nfhb6adjd/55Qbbc5t8m.txt', 'ex1/B/DBvt2h4/55i4q73/i5233.txt', 'ex1/B/DBvt2h4/8q2i3cb/33q.txt', 'ex1/B/DBvt2h4/8q2i3cb/pebd42g5B.txt', 'ex1/B/DBvt2h4/v1ahd.txt', 'ex1/B/hfc44ba/ummc6eb93/844d9i.txt']
    return do_test_ex1(dirin, expected)


def test_ex1_3():
    '''
    dirin = 'ex1/C'
    expected = ['ex1/C/bhk49r49.txt', 'ex1/C/A/a9fa5r54ol/inr6.txt', 'ex1/C/2o48dgq.txt', 'ex1/C/A/iahvg9mD9f.txt', 'ex1/C/A/r5g/74p52jhs.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/5lo3sa.txt', 'ex1/C/C/9n5/22zi524j/98469.txt', 'ex1/C/A/r5g/d501/tew8/l6j933qj.txt', 'ex1/C/a7u6kcehcm.txt', 'ex1/C/4q5ni/q5251as862.txt', 'ex1/C/A/lwc4z40fq.txt', 'ex1/C/B/Ch9d4f9.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/4lok.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/yoh.txt', 'ex1/C/A/r5g/d501/tew8/4tA4ca3g81k.txt', 'ex1/C/C/9n5/22zi524j/u2g/k2se7oh.txt', 'ex1/C/C/9n5/22zi524j/u2g/my1fc.txt', 'ex1/C/A/d6031a.txt', 'ex1/C/A/so8j7j3m.txt', 'ex1/C/B/p3zt345614/7j30i/f59a2l.txt', 'ex1/C/C/9n5/22zi524j/1iha5/nk7460q.txt', 'ex1/C/B/85bafd.txt', 'ex1/C/A/a9fa5r54ol/jfn.txt', 'ex1/C/B/p3zt345614/17nt/r0p8p5oe.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/p2q8/3gjbyrib.txt', 'ex1/C/C/9n5/22zi524j/u2g/m068.txt', 'ex1/C/B/33h294F.txt', 'ex1/C/439/53d23yd/092l53.txt', 'ex1/C/B/p3zt345614/7j30i/6hmre.txt', 'ex1/C/iuh5.txt', 'ex1/C/p1u34x59.txt', 'ex1/C/4q5ni/5bh9l253bc.txt', 'ex1/C/A/6f8554w.txt', 'ex1/C/C/4nd3c32.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/1bqeb8/m685c.txt', 'ex1/C/A/r5g/d501/w6i37c.txt', 'ex1/C/C/9n5/22zi524j/cj44.txt', 'ex1/C/B/p3zt345614/ei9ej73p/523hn6.txt', 'ex1/C/B/ape.txt']
    '''
    dirin = 'ex1/C'
    expected = ['ex1/C/bhk49r49.txt', 'ex1/C/A/a9fa5r54ol/inr6.txt', 'ex1/C/2o48dgq.txt', 'ex1/C/A/iahvg9mD9f.txt', 'ex1/C/A/r5g/74p52jhs.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/5lo3sa.txt', 'ex1/C/C/9n5/22zi524j/98469.txt', 'ex1/C/A/r5g/d501/tew8/l6j933qj.txt', 'ex1/C/a7u6kcehcm.txt', 'ex1/C/4q5ni/q5251as862.txt', 'ex1/C/A/lwc4z40fq.txt', 'ex1/C/B/Ch9d4f9.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/4lok.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/yoh.txt', 'ex1/C/A/r5g/d501/tew8/4tA4ca3g81k.txt', 'ex1/C/C/9n5/22zi524j/u2g/k2se7oh.txt', 'ex1/C/C/9n5/22zi524j/u2g/my1fc.txt', 'ex1/C/A/d6031a.txt', 'ex1/C/A/so8j7j3m.txt', 'ex1/C/B/p3zt345614/7j30i/f59a2l.txt', 'ex1/C/C/9n5/22zi524j/1iha5/nk7460q.txt', 'ex1/C/B/85bafd.txt', 'ex1/C/A/a9fa5r54ol/jfn.txt', 'ex1/C/B/p3zt345614/17nt/r0p8p5oe.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/p2q8/3gjbyrib.txt', 'ex1/C/C/9n5/22zi524j/u2g/m068.txt', 'ex1/C/B/33h294F.txt', 'ex1/C/439/53d23yd/092l53.txt', 'ex1/C/B/p3zt345614/7j30i/6hmre.txt', 'ex1/C/iuh5.txt', 'ex1/C/p1u34x59.txt', 'ex1/C/4q5ni/5bh9l253bc.txt', 'ex1/C/A/6f8554w.txt', 'ex1/C/C/4nd3c32.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/1bqeb8/m685c.txt', 'ex1/C/A/r5g/d501/w6i37c.txt', 'ex1/C/C/9n5/22zi524j/cj44.txt', 'ex1/C/B/p3zt345614/ei9ej73p/523hn6.txt', 'ex1/C/B/ape.txt']
    return do_test_ex1(dirin, expected)

# ----------------------------------- EX. 2----------------------------------- #


def do_ex2_test(root, expected):
    res = program.ex2(root)
    if res == None:
        raise testlib.NotImplemented
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

      expected = 2
    '''
    root = tree.BinaryTree.fromList([25, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
    expected = 2
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

       expected = 4
    '''
    root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [15, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [-9, None, None]]]])
    expected =  4
    return do_ex2_test(root, expected)


def test_ex2_3():
    '''
    A big tree
    expected = 44
    '''
    root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    expected = 44
    return do_ex2_test(root, expected)


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
