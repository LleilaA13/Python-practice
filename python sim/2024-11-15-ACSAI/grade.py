# -*- coding: utf-8 -*-
import testlib
from testlib import my_print, COL, check_expected

import isrecursive 
import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################
# %% ---------------------- DEBUG VARIABLE -------------------
DEBUG = True    # with    stack trace of errors
#DEBUG = False   # without stack trace of errors

#############################################################################
# %% ---------------------- TEST SECTION -------------------
#############################################################################

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


###########################################################################################################################

def do_func1_tests(ID, expected):
    input_filename  = f'txt/in_0{ID}.txt'
    res = program.func1(input_filename)
    testlib.checkList(res, expected)
    return 1

def test_func1_1():
    ID = 1
    expected = ['bat', 'car', 'cat', 'condor', 'rat']
    return do_func1_tests(ID, expected)

def test_func1_2():
    ID = 2
    expected = ['57h9ai49', '5pg3d11t4', '6yvbo', '790qi', '7gbe', '7h3m6c73', '7od842m3m', '8s3bc44j5', 'absurdly', 'actuator', 'anus', 'aqdb8ih1', 'defectors', 'disadvantage', 'doormen', 'expected', 'h4f5b', 'j5c739fit', 'vmn', 'wa39fitb']
    return do_func1_tests(ID, expected)

def test_func1_3():
    ID = 3
    expected = ['adduced', 'analytics', 'crapshooter', 'decreer', 'deprivations', 'develops', 'drastic', 'establishes', 'griding', 'humanistic', 'lubricative', 'noggins', 'noggins😌😌', 'overtire', 'panoramic', 'penthouses', 'percolating', 'supportability', 'tachometer', 'unharvested', 'wintertime']
    return do_func1_tests(ID, expected)

def test_func1_4():
    ID = 4
    expected = ['"', '",', '"a', '"non', '"o', '"or', '"poeta,', '"qual', '"se', "'l", "'mpedisce", "'mpediva", "'n", "'ncontro,", "'nferno,", "'nvidia", ',', 'a', 'abbandonai.', 'acciò', 'acquista,', 'affannata', 'ahi', 'aiutami', 'al', 'alighieri', 'allor', 'alto,', 'altri', 'altro', 'altrui', 'amara', 'ambedui.', 'amore', 'ancor', 'ancora,', 'anima', 'animali', 'antichi', 'anzi', 'aspra', 'augusto', 'autore;', 'basso', 'basso.', 'beate', 'belle;', 'bello', 'ben', 'bene', 'bestia', 'bestia,', 'brame', 'bramosa', 'bugiardi.', 'buono', 'caccerà', 'cagion', 'cagione', 'calle.', 'cammilla,', 'cammin', 'cammino,', 'campar', 'cantai', 'canto', 'carca', 'cercar', 'certo!".', "ch'a", "ch'ancor", "ch'ella", "ch'eran", "ch'i'", "ch'io", "ch'uscia", "ch'è", "ch'èi", 'che', 'che,', 'chi', 'ché', 'ciascun', 'ciberà', 'città', 'ciò', 'colle', 'color', 'colui', "com'i'", 'combusto.', 'come', 'cominciar', 'commedia', 'compunto,', 'con', 'conoscesti,', 'contenti', 'contra', 'convien', 'cor', 'corpo', 'cosa', 'cose', 'costui', 'così', 'cotanto', 'coverta;', "cu'", 'cui', "d'anchise", "d'esto", "d'un", 'da', 'dal', 'dante', 'de', "de'", 'degna:', 'del', 'desse', 'di', 'dicesti,', 'dietro.', 'dilettoso', 'dinanzi', 'dio', 'dipartilla.', 'dir', 'diritta', 'dirò', 'discerno', 'diserta,', 'diserto,', 'disperate', 'divina', 'divino', 'doglia.', 'dolce', 'dolenti,', 'dopo', "dov'or", 'dove', 'dritto', 'dura', 'durata', 'dèi', 'e', 'ecco,', 'ed', 'elegge!".', 'empie', 'era', 'esta', 'etterno,', 'eurialo', 'fa', 'face,', 'fai', 'falsi', 'fame', 'fame,', 'famoso', 'farà', 'fatto', 'fece', 'felice', 'feltro', 'feltro.', 'fermo', 'ferute.', 'fia', 'fiera', 'figliuol', 'fin', 'fioco.', 'fiume?",', 'foco,', 'fonte', 'forte', 'fosse', 'fronte.', 'fu', "fu'", 'fugga', 'fuggiva,', 'fui', 'fui,', 'fuor', 'furon', 'fé', 'gaetta', 'genti', 'genti.', 'gioia?".', 'giugne', 'giunto,', 'giusto', 'già', 'grame,', 'gran', 'grande', 'gravezza', 'grida;', 'gridai', 'gride,', 'guardai', 'guata,', 'guida,', 'ha', 'i', 'il', 'ilión', 'impera', 'imperador', 'in', 'inferno', 'inferno:', 'infin', 'io', 'italia', 'iulio', 'ivi', "l'acqua", "l'aere", "l'altezza.", "l'alto", "l'altre", "l'amor", "l'animo", "l'avrà", "l'erta,", "l'ora", "l'uccide;", 'la', 'lago', 'lagrimar', 'largo', 'lascerò', 'lascia', 'lasciò', 'lasso,', 'le', 'legge,', 'leggera', 'lei', 'lei,', 'lena', 'leone.', 'li', 'lo', 'loco', 'loco,', 'lombardi,', 'lonza', 'lui', 'lui,', 'lui:', 'lume', 'lungo', 'lupa,', 'là', "m'apparve", "m'avea", "m'era", "m'ha", 'ma', 'macolato', 'maestro', 'magrezza,', 'mai', 'male', 'malvagia', 'mantoani', 'mattino,', 'me', "me'", 'mena', 'meni', 'mentre', 'mesti".', 'mezzo', 'mi', 'miei', 'mio', 'mio,', 'miserere', 'molte', 'molti', 'molto,', 'montava', 'monte', 'morir', 'morte', 'morte;', 'morì', 'mosse', 'mosse,', 'nacqui', 'natura', 'nazion', 'ne', 'nel', 'niso', 'noia?', 'non', 'nostra', 'notte', 'né', 'occhi', 'od', 'offerto', 'ogne', 'oh', 'ombra', 'omo', 'omo,', "ond'io", 'onde', 'onore', 'onore.', 'oscura', 'ove', 'pace,', 'parea', 'parenti', 'parlar', 'parti', 'partia', 'partire;', 'passai', 'passar', 'passo', 'pasto', 'patria', 'paura', 'paura!', 'peggio,', 'pel', 'pelago', 'pelle', 'peltro,', 'pensier', 'penso', 'per', "perch'i'", 'perché', 'perdei', 'perder', 'perigliosa', 'persona', 'piaggia', 'pianeta', 'piange', 'pien', 'pieta.', 'pietro', 'piè', 'più', 'poco', 'poeta', 'poeti', 'poi', 'polsi".', 'porse', 'porta', 'posato', 'presta', 'pria.', 'prima', 'principio', 'punto', 'quai', 'qual', 'quando', 'quanto', 'quasi', 'quei', 'quel', 'quella', 'quelle', 'quello', 'questa', 'questi', 'questo', 'queta', 'qui', 'quivi', 'rabbiosa', 'raggi', 'regge;', 'regna,', 'retro', 'ria,', 'ribellante', 'richeggio', 'ridir', 'rimessa', 'rimirar', 'rinova', 'ripigneva', 'ripresi', "rispuos'io", 'rispuose', 'rispuosemi:', 'ritornar', 'ritorni', 'ritrovai', 'riva', 'roma', 'rovinava', "s'ammoglia,", "s'attrista;", 'saggio,', 'sali', 'salire,', 'salute', 'san', 'sanza', 'sapienza,', 'saranno', 'sarà', 'sarò', 'scorte.', 'se', "se'", 'seconda', 'seggio:', 'segui,', 'selva', 'selvaggia', 'selvaggio:', 'sembiava', 'sempre', 'si', 'sia', 'sii,', 'silenzio', 'smarrita.', 'so', 'sol', 'solo', 'son', 'sonno', 'sotto', 'spalle', 'spandi', 'speran', 'speranza', 'sperar', 'spiriti', 'stagione;', 'stelle', 'stilo', 'strida,', 'studio', 'sua', 'sub', 'sue', 'suoi', 'superbo', 'sì', 'sù', 'tace.', 'tal', "tant'era", "tant'è", 'tanta', 'tanto', 'tardi,', 'te', "temp'era", 'tempo', 'tenere', 'tenni', 'terminava', 'terra', "test'alta", 'ti', 'tolsi', 'tra', 'trarrotti', 'trattar', 'tremar', 'tremesse.', 'troia,', 'trovai,', 'tu', 'tua', 'tuo', 'turno', "tutt'i", 'tutta', 'tutte', 'udirai', 'umile', 'un', 'una', 'uscito', "v'ho", "v'intrai,", 'vagliami', 'valle', 'vederai', 'vedi', 'vedrai', 'veggia', 'vegna.', 'veltro', 'vene', 'venendomi', 'venire', 'venisse', 'venne', 'verace', 'vergine', 'vergognosa', 'verrà,', 'vestite', 'vi', 'via', 'via,', 'viaggio",', 'vide,', 'vidi', 'villa,', 'virgilio', 'virtute,', 'vissi', 'vista', 'vista,', 'vita', 'viva.', 'viver', 'voglia,', 'volge', 'volontieri', 'volse', 'volsi:', 'volte', 'volto,', 'volume.', 'vorrai', "vuo'", 'vuol', 'vòlto.', 'è']
    return do_func1_tests(ID, expected)


###########################################################################################################################

def do_func2_tests(ID1, expected):
    input_filename  = f'txt/in_0{ID1}.txt'
    res = program.func2(input_filename)
    assert res in expected
    return 1

def test_func2_1():
    IDa = 1
    expected = (4,)
    return do_func2_tests(IDa, expected)


def test_func2_2():
    IDa = 2
    expected = (10, 17)
    return do_func2_tests(IDa, expected)


def test_func2_3():
    IDa = 3
    expected = (8, 4)
    return do_func2_tests(IDa, expected)


def test_func2_4():
    IDa = 4
    expected = (42, 7)
    return do_func2_tests(IDa, expected)



###########################################################################################################################

def do_func3_tests(ID, a_list, listi, expected):
    output_filename = f'txt/out_0{ID}.txt'
    expected_filename = f'txt/exp_0{ID}.txt'
    expected_filename2 = f'txt/exp_0{ID}_alt.txt'
    res = program.func3(a_list, listi, output_filename)
    try:  # si prova con il primo file
        testlib.check_text_file(output_filename, expected_filename)
    except AssertionError: # se da errore si prova col secondo
        testlib.check_text_file(output_filename, expected_filename2)
    # se arriva qui vuol dire che almeno uno dei 2 file e' giusto
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}\nexpected={expected}.\n{'*'*50}''')
        return 0
    return 1.5


def test_func3_1():
    ID = 0
    lists = [["monkey", "cat",], ["panda", "alligator"], ["zoo", 'zuu', 'zotero']]
    listi= [[1, 0], [0, 1], [2, 1, 0]]
    expected = 7
    return do_func3_tests(ID, lists, listi, expected)


def test_func3_2():
    ID = 1
    lists = [
        ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"],
        ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "brown", "black"],
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    ]
    listi = [
        [9, 0, 1, 4, 3, 7, 2, 5, 8, 6],
        [3, 2, 6, 4, 9, 5, 1, 0, 8, 7],
        [1, 3, 0, 7, 9, 5, 4, 6, 2, 8]
    ]
    expected = 30
    return do_func3_tests(ID, lists, listi, expected)


def test_func3_3():
    ID = 2
    lists = [
        ["car", "bus", "bike", "train", "plane", "boat"],  # 6 elements
        ["apple", "banana", "cherry", "date"],             # 4 elements
        ["red", "blue", "green", "yellow", "purple"],      # 5 elements
        ["one", "two", "three", "four", "five", "six", "seven"]  # 7 elements
    ]
    listi = [
        [5, 2, 0, 3, 1, 4],  # Permutation for the 6-element list
        [1, 3, 2, 0],        # Permutation for the 4-element list
        [4, 0, 3, 1, 2],     # Permutation for the 5-element list
        [6, 5, 3, 1, 4, 0, 2]  # Permutation for the 7-element list
    ]
    expected = 22
    return do_func3_tests(ID, lists, listi, expected)


def test_func3_4():
    ID = 3
    lists = [
        ["jazz", "rock", "pop", "blues", "classical", "hip-hop", "metal"],  # 7 elements
        ["paris", "london", "rome", "berlin", "madrid"],                   # 5 elements
        ["jupiter", "saturn", "neptune"],                                  # 3 elements
        ["north", "south", "east", "west"]                                 # 4 elements
    ]
    listi = [
        [6, 4, 3, 1, 0, 5, 2],  # Permutation for the 7-element music genre list
        [1, 3, 4, 0, 2],        # Permutation for the 5-element cities list
        [2, 0, 1],              # Permutation for the 3-element planets list
        [3, 1, 2, 0]            # Permutation for the 4-element directions list
    ]
    expected = 19
    return do_func3_tests(ID, lists, listi, expected)


def do_func4_tests(list_A, expected):
    result = program.func4(list_A)
    testlib.checkDict(result, expected)
    return 1.5

###########################################################################################################################

def test_func4_1():
    list_A = [("cat", [7, 3]), ("dog", [1, 4]), ("cat", [2, 7])]
    expected = {'cat': [2, 3, 7], 'dog': [1, 4]}
    return do_func4_tests(list_A, expected)

def test_func4_2():
    list_A = [("cat", [1, 7, 3]), ("dog", [1, 4, 5, 7]), ("cat", [2, 7]), ("bat", [7, 6, 5, 4, 2])]
    expected1 = {'cat': [1, 2, 3, 7], 'dog': [1, 4, 5, 7], 'bat': [7, 6, 5, 4, 2]}
    expected2 = {'cat': [1, 2, 3, 7], 'dog': [1, 4, 5, 7], 'bat': [2, 4, 5, 6, 7]}
    result = program.func4(list_A)
    assert result == expected1 or result == expected2
    return 1.5
    

def test_func4_3():
    list_A = [("cat", [1, 7, 3]), ("dog", [1, 4, 5, 7]), ("cat", [2, 7]), ("bat", [7, 6, 5, 4, 2]),
             ("dog", [1, 5, 4, 7]), ("velociraptor", [0])]
    expected1 = {'cat': [1, 2, 3, 7], 'dog': [1, 4, 5, 7], 'bat': [7, 6, 5, 4, 2], 'velociraptor': [0]}
    expected2 = {'cat': [1, 2, 3, 7], 'dog': [1, 4, 5, 7], 'bat': [2, 4, 5, 6, 7], 'velociraptor': [0]}
    result = program.func4(list_A)
    assert result == expected1 or result == expected2
    return 1.5

def test_func4_4():
    list_A = [("cat", [1]), ("dog", [1]), ("cat", [1]), ("bat", [1]),
             ("dog", [1]), ("velociraptor", [0])]
    expected = {'cat': [1], 'dog': [1], 'bat': [1], 'velociraptor': [0]}
    return do_func4_tests(list_A, expected)


###########################################################################################################################

def do_func5_tests(ID, expected):
    input_filename = f'txt/in_0{ID}.txt'
    output_filename = f'txt/out_f5_0{ID}.txt'
    expected_filename = f'txt/exp_f5_0{ID}.txt'
    res = program.func5(input_filename, output_filename)
    testlib.check_text_file(output_filename, expected_filename)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR]The returned value is incorrect!''')
        my_print(f'''Returned={res}\nexpected={expected}.\n{'*'*50}''')
        return 0
    return 1.5

def test_func5_1():
    IDa = 1
    expected = 8
    return do_func5_tests(IDa, expected)


def test_func5_2():
    IDa = 2
    expected = 31
    return do_func5_tests(IDa, expected)


def test_func5_3():
    IDa = 3
    expected = 63
    return do_func5_tests(IDa, expected)


def test_func5_4():
    IDa = 4
    expected = 955
    return do_func5_tests(IDa, expected)

###############################################################################
def do_func6_tests(folderpath, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            res = program.func6(folderpath)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion")
            print('NO RECURSION!!')
        finally:
            isrecursive.undecorate_module(program)
    res = program.func6(folderpath)
    testlib.checkDict(res, expected)
    return 2


def test_func6_1():
    folderpath = "func6/A"
    expected = {'file_paths': ['func6/A/a.txt', 'func6/A/B/b.txt', 'func6/A/C/b.txt', 'func6/A/C/c.txt', 'func6/A/gkfep28.txt', 'func6/A/C/n3ks22.txt', 'func6/A/C/vAe866.png', 'func6/A/3cmi4G3ev.txt', 'func6/A/B/3odd74B.txt', 'func6/A/C/oeaa01c4.bak', 'func6/A/C/e3dd7Ag22.txt'], 'subfolder_paths': ['func6/A/B', 'func6/A/C']}
    return do_func6_tests(folderpath, expected)

def test_func6_2():
    folderpath = "func6/B"
    expected = {'file_paths': ['func6/B/gn9.txt', 'func6/B/gem4.txt', 'func6/B/k5B3.txt', 'func6/B/vjv28.txt', 'func6/B/2kdt437mi.txt', 'func6/B/Ap81l6Cch.txt', 'func6/B/hfc44ba/fm45.txt', 'func6/B/hfc44ba/qm21e714', 'func6/B/DBvt2h4/v1ahd.txt', 'func6/B/hfc44ba/e7md39.txt', 'func6/B/DBvt2h4/yr3ao93533.txt', 'func6/B/DBvt2h4/8q2i3cb/33q.txt', 'func6/B/DBvt2h4/8q2i3cb/qjc.txt', 'func6/B/hfc44ba/4i9bfe1lq32.fde', 'func6/B/hfc44ba/Crfjcl0an56.tqq', 'func6/B/hfc44ba/B7n33lv/65h7.P5f', 'func6/B/DBvt2h4/55i4q73/i5233.txt', 'func6/B/DBvt2h4/5nfhb6adjd/1fe.txt', 'func6/B/DBvt2h4/8q2i3cb/37d4og.txt', 'func6/B/DBvt2h4/8q2i3cb/y4fcG6.txt', 'func6/B/hfc44ba/ummc6eb93/nr3e.awk', 'func6/B/DBvt2h4/55i4q73/5f4oxdfk.txt', 'func6/B/hfc44ba/ummc6eb93/844d9i.txt', 'func6/B/DBvt2h4/8q2i3cb/pebd42g5B.txt', 'func6/B/hfc44ba/ummc6eb93/unjlfaz.2fd', 'func6/B/hfc44ba/B7n33lv/4A6c45gvs4.A3a', 'func6/B/hfc44ba/ummc6eb93/slfiq56hi.a52', 'func6/B/hfc44ba/ummc6eb93/4hcAa25tn4.no2', 'func6/B/DBvt2h4/5nfhb6adjd/55Qbbc5t8m.txt', 'func6/B/hfc44ba/B7n33lv/gl88e642/3f8g.txt', 'func6/B/hfc44ba/B7n33lv/gl88e642/n31gy3n.ter'], 'subfolder_paths': ['func6/B/DBvt2h4', 'func6/B/hfc44ba', 'func6/B/DBvt2h4/55i4q73', 'func6/B/DBvt2h4/8q2i3cb', 'func6/B/hfc44ba/B7n33lv', 'func6/B/hfc44ba/ummc6eb93', 'func6/B/DBvt2h4/5nfhb6adjd', 'func6/B/hfc44ba/B7n33lv/gl88e642']}
    return do_func6_tests(folderpath, expected)


def test_func6_3():
    folderpath = "func6/C"
    expected = {'file_paths': ['func6/C/iuh5.txt', 'func6/C/B/ape.txt', 'func6/C/52e/w642ch', 'func6/C/2o48dgq.txt', 'func6/C/A/d6031a.txt', 'func6/C/B/85bafd.txt', 'func6/C/bhk49r49.txt', 'func6/C/p1u34x59.txt', 'func6/C/A/6f8554w.txt', 'func6/C/B/33h294F.txt', 'func6/C/B/Ch9d4f9.txt', 'func6/C/C/4nd3c32.txt', 'func6/C/439/16c193iw1c', 'func6/C/439/gr7126dt72', 'func6/C/A/r5g/cl9f.ne3', 'func6/C/A/so8j7j3m.txt', 'func6/C/a7u6kcehcm.txt', 'func6/C/A/lwc4z40fq.txt', 'func6/C/A/r5g/Adf3e.2i7', 'func6/C/52e/7ij/5Eskv49e', 'func6/C/52e/8ee7r85x45ef', 'func6/C/A/iahvg9mD9f.txt', 'func6/C/52e/7ij/gB2g30j3y', 'func6/C/A/r5g/14kn9hm.fd4', 'func6/C/C/9n5/7dlxd5r.png', 'func6/C/A/r5g/74p52jhs.txt', 'func6/C/4q5ni/4l2bcb85s.25c', 'func6/C/52e/7ij/cbh1513m823', 'func6/C/4q5ni/5bh9l253bc.txt', 'func6/C/4q5ni/q5251as862.txt', 'func6/C/52e/7ij/5B5dc57wl410', 'func6/C/A/a9fa5r54ol/jfn.txt', 'func6/C/A/a9fa5r54ol/inr6.txt', 'func6/C/A/r5g/d501/w6i37c.txt', 'func6/C/A/v9gdti5xl/gb47e8xei', 'func6/C/439/53d23yd/092l53.txt', 'func6/C/A/r5g/d501/39e446o.s90', 'func6/C/C/9n5/22zi524j/cj44.txt', 'func6/C/439/53d23yd/fcni3lmddeab', 'func6/C/B/p3zt345614/d4544k3.3dd', 'func6/C/C/9n5/22zi524j/98469.txt', 'func6/C/A/r5g/d501/14rek36of8.6e7', 'func6/C/A/r5g/d501/tew8/6e1353.er3', 'func6/C/C/9n5/22zi524j/mns3257.hhi', 'func6/C/C/9n5/22zi524j/j3y9nlh7.e2m', 'func6/C/C/9n5/22zi524j/u2g/m068.txt', 'func6/C/A/a9fa5r54ol/9dlnpni/yoh.txt', 'func6/C/A/r5g/d501/tew8/l6j933qj.txt', 'func6/C/B/p3zt345614/7j30i/6hmre.txt', 'func6/C/C/9n5/22zi524j/u2g/my1fc.txt', 'func6/C/A/a9fa5r54ol/9dlnpni/4lok.txt', 'func6/C/A/r5g/d501/tew8/55gf44mmh.vlq', 'func6/C/A/r5g/d501/tew8/m5o3obg77.56j', 'func6/C/B/p3zt345614/7j30i/f59a2l.txt', 'func6/C/C/9n5/22zi524j/Ejclmg3v24.Mok', 'func6/C/C/9n5/22zi524j/u2g/a3h29s.ke5', 'func6/C/B/p3zt345614/17nt/r0p8p5oe.txt', 'func6/C/C/9n5/22zi524j/u2g/k2se7oh.txt', 'func6/C/A/a9fa5r54ol/9dlnpni/5lo3sa.txt', 'func6/C/A/r5g/d501/tew8/4tA4ca3g81k.txt', 'func6/C/C/9n5/22zi524j/1iha5/t9975l.3fd', 'func6/C/B/p3zt345614/17nt/b2hKgkbrqn.png', 'func6/C/B/p3zt345614/ei9ej73p/523hn6.txt', 'func6/C/C/9n5/22zi524j/1iha5/nk7460q.txt', 'func6/C/A/a9fa5r54ol/9dlnpni/1bqeb8/m685c.txt', 'func6/C/A/a9fa5r54ol/9dlnpni/p2q8/3gjbyrib.txt'], 'subfolder_paths': ['func6/C/A', 'func6/C/B', 'func6/C/C', 'func6/C/439', 'func6/C/52e', 'func6/C/4q5ni', 'func6/C/A/r5g', 'func6/C/C/9n5', 'func6/C/52e/7ij', 'func6/C/A/r5g/d501', 'func6/C/439/53d23yd', 'func6/C/A/v9gdti5xl', 'func6/C/A/a9fa5r54ol', 'func6/C/B/p3zt345614', 'func6/C/C/9n5/22zi524j', 'func6/C/A/r5g/d501/tew8', 'func6/C/B/p3zt345614/17nt', 'func6/C/B/p3zt345614/7j30i', 'func6/C/C/9n5/22zi524j/u2g', 'func6/C/A/a9fa5r54ol/9dlnpni', 'func6/C/C/9n5/22zi524j/1iha5', 'func6/C/B/p3zt345614/ei9ej73p', 'func6/C/A/a9fa5r54ol/9dlnpni/p2q8', 'func6/C/A/a9fa5r54ol/9dlnpni/1bqeb8']}
    return do_func6_tests(folderpath, expected)

def test_func6_4():
    folderpath = "func6"
    expected = {'file_paths': ['func6/A/a.txt', 'func6/A/B/b.txt', 'func6/A/C/b.txt', 'func6/A/C/c.txt', 'func6/B/gn9.txt', 'func6/B/gem4.txt', 'func6/B/k5B3.txt', 'func6/C/iuh5.txt', 'func6/B/vjv28.txt', 'func6/C/B/ape.txt', 'func6/C/52e/w642ch', 'func6/A/gkfep28.txt', 'func6/C/2o48dgq.txt', 'func6/A/C/n3ks22.txt', 'func6/A/C/vAe866.png', 'func6/C/A/d6031a.txt', 'func6/C/B/85bafd.txt', 'func6/C/bhk49r49.txt', 'func6/C/p1u34x59.txt', 'func6/A/3cmi4G3ev.txt', 'func6/A/B/3odd74B.txt', 'func6/B/2kdt437mi.txt', 'func6/B/Ap81l6Cch.txt', 'func6/C/A/6f8554w.txt', 'func6/C/B/33h294F.txt', 'func6/C/B/Ch9d4f9.txt', 'func6/C/C/4nd3c32.txt', 'func6/A/C/oeaa01c4.bak', 'func6/C/439/16c193iw1c', 'func6/C/439/gr7126dt72', 'func6/C/A/r5g/cl9f.ne3', 'func6/C/A/so8j7j3m.txt', 'func6/C/a7u6kcehcm.txt', 'func6/A/C/e3dd7Ag22.txt', 'func6/C/A/lwc4z40fq.txt', 'func6/C/A/r5g/Adf3e.2i7', 'func6/B/hfc44ba/fm45.txt', 'func6/B/hfc44ba/qm21e714', 'func6/C/52e/7ij/5Eskv49e', 'func6/C/52e/8ee7r85x45ef', 'func6/C/A/iahvg9mD9f.txt', 'func6/B/DBvt2h4/v1ahd.txt', 'func6/C/52e/7ij/gB2g30j3y', 'func6/C/A/r5g/14kn9hm.fd4', 'func6/C/C/9n5/7dlxd5r.png', 'func6/B/hfc44ba/e7md39.txt', 'func6/C/A/r5g/74p52jhs.txt', 'func6/C/4q5ni/4l2bcb85s.25c', 'func6/C/52e/7ij/cbh1513m823', 'func6/C/4q5ni/5bh9l253bc.txt', 'func6/C/4q5ni/q5251as862.txt', 'func6/C/52e/7ij/5B5dc57wl410', 'func6/C/A/a9fa5r54ol/jfn.txt', 'func6/C/A/a9fa5r54ol/inr6.txt', 'func6/C/A/r5g/d501/w6i37c.txt', 'func6/C/A/v9gdti5xl/gb47e8xei', 'func6/B/DBvt2h4/yr3ao93533.txt', 'func6/C/439/53d23yd/092l53.txt', 'func6/C/A/r5g/d501/39e446o.s90', 'func6/B/DBvt2h4/8q2i3cb/33q.txt', 'func6/B/DBvt2h4/8q2i3cb/qjc.txt', 'func6/B/hfc44ba/4i9bfe1lq32.fde', 'func6/B/hfc44ba/Crfjcl0an56.tqq', 'func6/C/C/9n5/22zi524j/cj44.txt', 'func6/B/hfc44ba/B7n33lv/65h7.P5f', 'func6/C/439/53d23yd/fcni3lmddeab', 'func6/C/B/p3zt345614/d4544k3.3dd', 'func6/C/C/9n5/22zi524j/98469.txt', 'func6/B/DBvt2h4/55i4q73/i5233.txt', 'func6/C/A/r5g/d501/14rek36of8.6e7', 'func6/B/DBvt2h4/5nfhb6adjd/1fe.txt', 'func6/B/DBvt2h4/8q2i3cb/37d4og.txt', 'func6/B/DBvt2h4/8q2i3cb/y4fcG6.txt', 'func6/B/hfc44ba/ummc6eb93/nr3e.awk', 'func6/C/A/r5g/d501/tew8/6e1353.er3', 'func6/C/C/9n5/22zi524j/mns3257.hhi', 'func6/C/C/9n5/22zi524j/j3y9nlh7.e2m', 'func6/C/C/9n5/22zi524j/u2g/m068.txt', 'func6/B/DBvt2h4/55i4q73/5f4oxdfk.txt', 'func6/B/hfc44ba/ummc6eb93/844d9i.txt', 'func6/C/A/a9fa5r54ol/9dlnpni/yoh.txt', 'func6/C/A/r5g/d501/tew8/l6j933qj.txt', 'func6/C/B/p3zt345614/7j30i/6hmre.txt', 'func6/C/C/9n5/22zi524j/u2g/my1fc.txt', 'func6/B/DBvt2h4/8q2i3cb/pebd42g5B.txt', 'func6/B/hfc44ba/ummc6eb93/unjlfaz.2fd', 'func6/C/A/a9fa5r54ol/9dlnpni/4lok.txt', 'func6/C/A/r5g/d501/tew8/55gf44mmh.vlq', 'func6/C/A/r5g/d501/tew8/m5o3obg77.56j', 'func6/C/B/p3zt345614/7j30i/f59a2l.txt', 'func6/C/C/9n5/22zi524j/Ejclmg3v24.Mok', 'func6/C/C/9n5/22zi524j/u2g/a3h29s.ke5', 'func6/B/hfc44ba/B7n33lv/4A6c45gvs4.A3a', 'func6/C/B/p3zt345614/17nt/r0p8p5oe.txt', 'func6/C/C/9n5/22zi524j/u2g/k2se7oh.txt', 'func6/B/hfc44ba/ummc6eb93/slfiq56hi.a52', 'func6/C/A/a9fa5r54ol/9dlnpni/5lo3sa.txt', 'func6/C/A/r5g/d501/tew8/4tA4ca3g81k.txt', 'func6/C/C/9n5/22zi524j/1iha5/t9975l.3fd', 'func6/B/hfc44ba/ummc6eb93/4hcAa25tn4.no2', 'func6/C/B/p3zt345614/17nt/b2hKgkbrqn.png', 'func6/C/B/p3zt345614/ei9ej73p/523hn6.txt', 'func6/C/C/9n5/22zi524j/1iha5/nk7460q.txt', 'func6/B/DBvt2h4/5nfhb6adjd/55Qbbc5t8m.txt', 'func6/B/hfc44ba/B7n33lv/gl88e642/3f8g.txt', 'func6/B/hfc44ba/B7n33lv/gl88e642/n31gy3n.ter', 'func6/C/A/a9fa5r54ol/9dlnpni/1bqeb8/m685c.txt', 'func6/C/A/a9fa5r54ol/9dlnpni/p2q8/3gjbyrib.txt'], 'subfolder_paths': ['func6/A', 'func6/B', 'func6/C', 'func6/A/B', 'func6/A/C', 'func6/C/A', 'func6/C/B', 'func6/C/C', 'func6/C/439', 'func6/C/52e', 'func6/C/4q5ni', 'func6/C/A/r5g', 'func6/C/C/9n5', 'func6/B/DBvt2h4', 'func6/B/hfc44ba', 'func6/C/52e/7ij', 'func6/C/A/r5g/d501', 'func6/C/439/53d23yd', 'func6/C/A/v9gdti5xl', 'func6/C/A/a9fa5r54ol', 'func6/C/B/p3zt345614', 'func6/C/C/9n5/22zi524j', 'func6/B/DBvt2h4/55i4q73', 'func6/B/DBvt2h4/8q2i3cb', 'func6/B/hfc44ba/B7n33lv', 'func6/C/A/r5g/d501/tew8', 'func6/B/hfc44ba/ummc6eb93', 'func6/C/B/p3zt345614/17nt', 'func6/B/DBvt2h4/5nfhb6adjd', 'func6/C/B/p3zt345614/7j30i', 'func6/C/C/9n5/22zi524j/u2g', 'func6/C/A/a9fa5r54ol/9dlnpni', 'func6/C/C/9n5/22zi524j/1iha5', 'func6/C/B/p3zt345614/ei9ej73p', 'func6/B/hfc44ba/B7n33lv/gl88e642', 'func6/C/A/a9fa5r54ol/9dlnpni/p2q8', 'func6/C/A/a9fa5r54ol/9dlnpni/1bqeb8']}
    return do_func6_tests(folderpath, expected)


tests = [
    # TO DISABLE SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1 ,  test_func1_2, test_func1_3, test_func1_4, # OK 6
    test_func2_1,  test_func2_2, test_func2_3, test_func2_4, # OK 6
    test_func3_1,  test_func3_2, test_func3_3, test_func3_4, # OK 6
    test_func4_1, test_func4_2, test_func4_3,  test_func4_4,# OK 6
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_func6_1, test_func6_2, test_func6_3, test_func6_4,
    test_personal_data_entry,
]

if __name__ == '__main__':
    import sys
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
    if 'matricola' in program.__dict__:
        print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')
################################################################################
