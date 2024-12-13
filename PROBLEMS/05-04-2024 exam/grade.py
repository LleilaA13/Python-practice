# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import tree
from testlib import my_print, COL, check_expected

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
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

##----------------------------------- Func 1 ----------------------------------- ##

def do_func1_tests(int_list, n, expected):
    res = program.func1(int_list, n)
    testlib.check_dict(res, expected)
    return 1


def test_func1_1(run=True):
    '''
    D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 4}
    D2 = {'bb': 4, 'ee': 4, 'ff': 1, 'ggg': 1}
    expected= {1: 'gggaaccff', 4: 'dddee'}
    '''
    D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 4}
    D2 = {'bb': 4, 'ee': 4, 'ff': 1, 'ggg': 1}
    expected= {1: 'gggaaccff', 4: 'dddee'}
    return do_func1_tests(D1, D2, expected)

def test_func1_2(run=True):
    '''
    D1 = {'paste': 1, 'photodiode': 1, 'lobotomy': 1, 'farming': 2, 'screwdriver': 2, 'napkin': 1, 'extremist': 2, 'siding': 2, 'divine': 1, 'coil': 1, 'jump': 2, 'webinar': 2}
    D2 = {'photodiode': 2, 'farming': 2, 'chop': 2, 'coal': 1, 'tart': 1, 'stonework': 1, 'scenery': 2, 'sport': 2, 'coil': 1, 'napkin': 2, 'paste': 1, 'jump': 2}
    expected = {2: 'screwdriverextremistscenerywebinarsidingsportchop', 1: 'stoneworklobotomydivinecoaltart'}
     '''
    D1 = {'paste': 1, 'photodiode': 1, 'lobotomy': 1, 'farming': 2, 'screwdriver': 2, 'napkin': 1, 'extremist': 2, 'siding': 2, 'divine': 1, 'coil': 1, 'jump': 2, 'webinar': 2}
    D2 = {'photodiode': 2, 'farming': 2, 'chop': 2, 'coal': 1, 'tart': 1, 'stonework': 1, 'scenery': 2, 'sport': 2, 'coil': 1, 'napkin': 2, 'paste': 1, 'jump': 2}
    expected = {2: 'screwdriverextremistscenerywebinarsidingsportchop', 1: 'stoneworklobotomydivinecoaltart'}
    return do_func1_tests(D1, D2, expected)

def test_func1_3(run=True):
    '''
    D1 = {'dolor': 1, 'euphonium': 2, 'towering': 2, 'chive': 3, 'daily': 3, 'controller': 2, 'gunpowder': 3, 'grumpy': 1, 'terracotta': 1, 'hemp': 3, 'navigation': 2, 'composite': 2, 'somber': 2, 'melted': 3, 'fritter': 1, 'venom': 1, 'examine': 1, 'north': 2, 'lady': 1, 'beam': 1}
    D2 = {'chive': 1, 'withdraw': 1, 'sparkling': 3, 'gunpowder': 2, 'yogurt': 3, 'race': 2, 'pigeon': 2, 'beam': 2, 'cinder': 3, 'item': 3, 'ranger': 2, 'lady': 2, 'towering': 1, 'stot': 1, 'hemp': 2, 'north': 3, 'euphonium': 3, 'chord': 2, 'dolor': 1, 'terracotta': 3}
    expected = {3: 'sparklingcindermeltedyogurtdailyitem', 1: 'withdrawexaminefrittergrumpyvenomstot', 2: 'controllernavigationcompositepigeonrangersomberchordrace'}
    '''
    D1 = {'dolor': 1, 'euphonium': 2, 'towering': 2, 'chive': 3, 'daily': 3, 'controller': 2, 'gunpowder': 3, 'grumpy': 1, 'terracotta': 1, 'hemp': 3, 'navigation': 2, 'composite': 2, 'somber': 2, 'melted': 3, 'fritter': 1, 'venom': 1, 'examine': 1, 'north': 2, 'lady': 1, 'beam': 1}
    D2 = {'chive': 1, 'withdraw': 1, 'sparkling': 3, 'gunpowder': 2, 'yogurt': 3, 'race': 2, 'pigeon': 2, 'beam': 2, 'cinder': 3, 'item': 3, 'ranger': 2, 'lady': 2, 'towering': 1, 'stot': 1, 'hemp': 2, 'north': 3, 'euphonium': 3, 'chord': 2, 'dolor': 1, 'terracotta': 3}
    expected = {3: 'sparklingcindermeltedyogurtdailyitem', 1: 'withdrawexaminefrittergrumpyvenomstot', 2: 'controllernavigationcompositepigeonrangersomberchordrace'}
    return do_func1_tests(D1, D2, expected)

def test_func1_4(run=True):
    '''
    D1 = {'hit': 1, 'recipe': 2, 'patrolling': 4, 'resource': 3, 'synergy': 1, 'delight': 6, 'sordid': 5, 'apparatus': 5, 'burial': 1, 'whiskey': 5, 'classification': 1, 'damage': 2, 'jot': 6, 'rebellion': 2, 'snowsuit': 6, 'well-being': 2, 'tale': 2, 'prick': 2, 'census': 3, 'snowman': 3, 'fine': 2, 'deed': 6, 'flung': 4, 'patrimony': 5, 'square': 3, 'sanctuary': 3, 'great-grandmother': 1, 'poet': 2, 'million': 6, 'forbid': 4, 'forehead': 2, 'confidence': 3, 'price': 5, 'fiber': 3, 'polenta': 5, 'caterpillar': 5, 'browsing': 1, 'faded': 3, 'granny': 4, 'officer': 2}
    D2 = {'velodrome': 2, 'patrolling': 1, 'delight': 1, 'gale': 3, 'bore': 3, 'whiskey': 6, 'synergy': 2, 'homogenate': 1, 'resource': 5, 'bunch': 3, 'polenta': 4, 'bin': 3, 'confidence': 2, 'suffer': 4, 'righteous': 1, 'census': 6, 'cost': 4, 'century': 6, 'infancy': 5, 'browsing': 6, 'exceed': 4, 'happiness': 6, 'passive': 4, 'sanctuary': 5, 'square': 4, 'funeral': 6, 'million': 5, 'forbid': 2, 'rebellion': 2, 'patrimony': 2, 'fiber': 4, 'burial': 2, 'gastropod': 1, 'forsake': 2, 'eicosanoid': 4, 'advance': 5, 'apparatus': 5, 'granny': 3, 'socialism': 1, 'forehead': 4}
    expected = {5: 'caterpillaradvanceinfancysordidprice', 6: 'happinesssnowsuitcenturyfuneraldeedjot', 3: 'snowmanbunchfadedboregalebin', 2: 'well-beingvelodromeforsakeofficerdamagerecipeprickfinepoettale', 4: 'eicosanoidpassiveexceedsufferflungcost', 1: 'great-grandmotherclassificationhomogenategastropodrighteoussocialismhit'}
    '''
    D1 = {'hit': 1, 'recipe': 2, 'patrolling': 4, 'resource': 3, 'synergy': 1, 'delight': 6, 'sordid': 5, 'apparatus': 5, 'burial': 1, 'whiskey': 5, 'classification': 1, 'damage': 2, 'jot': 6, 'rebellion': 2, 'snowsuit': 6, 'well-being': 2, 'tale': 2, 'prick': 2, 'census': 3, 'snowman': 3, 'fine': 2, 'deed': 6, 'flung': 4, 'patrimony': 5, 'square': 3, 'sanctuary': 3, 'great-grandmother': 1, 'poet': 2, 'million': 6, 'forbid': 4, 'forehead': 2, 'confidence': 3, 'price': 5, 'fiber': 3, 'polenta': 5, 'caterpillar': 5, 'browsing': 1, 'faded': 3, 'granny': 4, 'officer': 2}
    D2 = {'velodrome': 2, 'patrolling': 1, 'delight': 1, 'gale': 3, 'bore': 3, 'whiskey': 6, 'synergy': 2, 'homogenate': 1, 'resource': 5, 'bunch': 3, 'polenta': 4, 'bin': 3, 'confidence': 2, 'suffer': 4, 'righteous': 1, 'census': 6, 'cost': 4, 'century': 6, 'infancy': 5, 'browsing': 6, 'exceed': 4, 'happiness': 6, 'passive': 4, 'sanctuary': 5, 'square': 4, 'funeral': 6, 'million': 5, 'forbid': 2, 'rebellion': 2, 'patrimony': 2, 'fiber': 4, 'burial': 2, 'gastropod': 1, 'forsake': 2, 'eicosanoid': 4, 'advance': 5, 'apparatus': 5, 'granny': 3, 'socialism': 1, 'forehead': 4}
    expected = {5: 'caterpillaradvanceinfancysordidprice', 6: 'happinesssnowsuitcenturyfuneraldeedjot', 3: 'snowmanbunchfadedboregalebin', 2: 'well-beingvelodromeforsakeofficerdamagerecipeprickfinepoettale', 4: 'eicosanoidpassiveexceedsufferflungcost', 1: 'great-grandmotherclassificationhomogenategastropodrighteoussocialismhit'}
    return do_func1_tests(D1, D2, expected)

##----------------------------------- Func 2 ----------------------------------- ##
def do_func2_tests(testo, n, expected):
    res = program.func2(testo, n)
    testlib.check_list(res, expected)
    return 0.5

def test_func2_1(run=True):
    '''
    testo = 'la rana in Spagna gracida in campagna'
    n = 3
    expected = ['campagna', 'gracida', 'Spagna', 'rana']
    '''
    testo = 'la rana in Spagna gracida in campagna'
    n = 3
    expected = ['campagna', 'gracida', 'Spagna', 'rana']
    return do_func2_tests(testo, n, expected)

def test_func2_2(run=True):
    '''
    testo = """
   lifetime
  conductor     sword    	bull-fighter     foolish    	antennae     sock
 flap     radiate     demon 	   """
    n = 4
    expected = ['demon', 'radiate', 'flap', 'sock', 'antennae', 'foolish', 'bull-fighter', 'sword', 'conductor', 'lifetime']
    '''
    testo = """ 
      lifetime  
     conductor     sword    	bull-fighter     foolish    	antennae     sock 	 
    flap     radiate     demon 	   """
    n = 4
    expected = ['demon', 'radiate', 'flap', 'sock', 'antennae', 'foolish', 'bull-fighter', 'sword', 'conductor',
                'lifetime']
    return do_func2_tests(testo, n, expected)

def test_func2_3(run=True):
    '''
    testo = """  	 party
  combat   	armament    carrot    river
   indicator	   bonus    half-sister
	 wee    tinkle    collision
malice    horn    mundane   	edger    abbey    phenotype
capacity
	 dislike    royal
 """
    n = 9
    expected = ['phenotype', 'collision', 'half-sister', 'indicator']
    '''
    testo = """  	 party 
      combat   	armament    carrot    river
       indicator	   bonus    half-sister 
    	 wee    tinkle    collision   
    malice    horn    mundane   	edger    abbey    phenotype   
    capacity 
    	 dislike    royal  
     """
    n = 9
    expected = ['phenotype', 'collision', 'half-sister', 'indicator']
    return do_func2_tests(testo, n, expected)

def test_func2_4(run=True):
    '''
    testo = """    	 personality
  medium  	   blade

   cloudburst 	    incandescence
     gray


ecumenist 	 	  topsail
dapper      physical      crook
  		garrulous
 stall    	 yam

pretend      constant
immigrant      spree  	   train 	  	 standoff

energy
   venue   	  vol
     melody      c-clamp
    fixture      cohort

 weary
   	 wise

  champagne	   	 """
    n = 6
    expected = ['champagne', 'cohort', 'fixture', 'c-clamp', 'melody', 'energy', 'standoff', 'immigrant', 'constant', 'pretend', 'garrulous', 'physical', 'dapper', 'topsail', 'ecumenist', 'incandescence', 'cloudburst', 'medium', 'personality']
    '''
    testo = """    	 personality 	 
      medium  	   blade

       cloudburst 	    incandescence
         gray


    ecumenist 	 	  topsail     
    dapper      physical      crook 
      		garrulous    
     stall    	 yam   

    pretend      constant     
    immigrant      spree  	   train 	  	 standoff 

    energy	 
       venue   	  vol
         melody      c-clamp	
        fixture      cohort 

     weary
       	 wise

      champagne	   	 """
    n = 6
    expected = ['champagne', 'cohort', 'fixture', 'c-clamp', 'melody', 'energy', 'standoff', 'immigrant', 'constant',
                'pretend', 'garrulous', 'physical', 'dapper', 'topsail', 'ecumenist', 'incandescence', 'cloudburst',
                'medium', 'personality']
    return do_func2_tests(testo, n, expected)

##----------------------------------- Func 3 ----------------------------------- ##

def do_func3_tests(str1, str2, expected):
    res = program.func3(str1, str2)
    testlib.check_val(res, expected)
    return 0.5


def test_func3_1(run=True):
    '''
    S1 = {'a', 'b', 'c'}
    S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
    expected = {'a': ['abc', 'aa', 'ab'], 'c': ['cc', 'cd'], 'b': ['bb', 'bc']}
    '''
    S1 = {'a', 'b', 'c'}
    S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
    expected = {'a': ['abc', 'aa', 'ab'], 'c': ['cc', 'cd'], 'b': ['bb', 'bc']}
    return do_func3_tests(S1, S2, expected)

def test_func3_2(run=True):
    '''
    S1 = {'pros', 'jum', 'r', 'on', 'p', 'i', 'ove', 'te', 'ex', 're'}
    S2 = {'temple', 'webinar', 'atelier', 'rid', 'beast', 'prosecution', 'eponym', 'cenotaph', 'reservation', 'onset'}
    expected = {'pros': ['prosecution'], 'r': ['reservation', 'rid'], 'on': ['onset'], 'p': ['prosecution'], 'te': ['temple'], 're': ['reservation']}
    '''
    S1 = {'pros', 'jum', 'r', 'on', 'p', 'i', 'ove', 'te', 'ex', 're'}
    S2 = {'temple', 'webinar', 'atelier', 'rid', 'beast', 'prosecution', 'eponym', 'cenotaph', 'reservation', 'onset'}
    expected = {'pros': ['prosecution'], 'r': ['reservation', 'rid'], 'on': ['onset'], 'p': ['prosecution'], 'te': ['temple'], 're': ['reservation']}
    return do_func3_tests(S1, S2, expected)

def test_func3_3(run=True):
    '''
    S1 = {'ma', 't', 's', 'st', 'rec', 'm', 'cro', 'T', 'w', 'ch', 'ou', 'cra', 'ow', 'fur', 'wis', 'han', 'sno', 'c', 'rid', 'te'}
    S2 = {'hand-holding', 'messy', 'commander', 'earring', 'effect', 'chem', 'stitch', 'madam', 'motel', 'snowman', 'charter', 'walnut', 'crotch', 'furnace', 'handover', 'gloom', 'cloudy', 'territory', 'moldy', 'collector'}
    expected = {'ma': ['madam'], 't': ['territory'], 's': ['snowman', 'stitch'], 'st': ['stitch'], 'm': ['madam', 'messy', 'moldy', 'motel'], 'cro': ['crotch'], 'w': ['walnut'], 'ch': ['charter', 'chem'], 'fur': ['furnace'], 'han': ['hand-holding', 'handover'], 'sno': ['snowman'], 'c': ['collector', 'commander', 'charter', 'cloudy', 'crotch', 'chem'], 'te': ['territory']}
    '''
    S1 = {'ma', 't', 's', 'st', 'rec', 'm', 'cro', 'T', 'w', 'ch', 'ou', 'cra', 'ow', 'fur', 'wis', 'han', 'sno', 'c', 'rid', 'te'}
    S2 = {'hand-holding', 'messy', 'commander', 'earring', 'effect', 'chem', 'stitch', 'madam', 'motel', 'snowman', 'charter', 'walnut', 'crotch', 'furnace', 'handover', 'gloom', 'cloudy', 'territory', 'moldy', 'collector'}
    expected = {'ma': ['madam'], 't': ['territory'], 's': ['snowman', 'stitch'], 'st': ['stitch'], 'm': ['madam', 'messy', 'moldy', 'motel'], 'cro': ['crotch'], 'w': ['walnut'], 'ch': ['charter', 'chem'], 'fur': ['furnace'], 'han': ['hand-holding', 'handover'], 'sno': ['snowman'], 'c': ['collector', 'commander', 'charter', 'cloudy', 'crotch', 'chem'], 'te': ['territory']}
    return do_func3_tests(S1, S2, expected)

def test_func3_4(run=True):
    '''
    S1 = {'gh', 'pla', 'eco', 'c', 'n', 'st', 'loa', 'ga', 'ad', 'con', 'alt', 'imi', 'w', 'bi', 'agg', 'r', 'f', 'em', 'wet', 't', 'of', 'gl', 'ho', 'h', 'p', 'suc', 'iso'}
    S2 = {'cooking', 'offering', 'wooden', 'void', 'disclosure', 'home', 'knit', 'altitude', 'wick', 'policeman', 'patty', 'stack', 'catch', 'living', 'cleavage', 'achievement', 'buck', 'drill', 'hygienic', 'storey', 'tab', 'planet', 'soul', 'bind', 'pail', 'success', 'devastation', 'behest', 'contention', 'fantastic'}
    expected = {'pla': ['planet'], 'c': ['contention', 'cleavage', 'cooking', 'catch'], 'st': ['storey', 'stack'], 'con': ['contention'], 'alt': ['altitude'], 'w': ['wooden', 'wick'], 'bi': ['bind'], 'f': ['fantastic'], 't': ['tab'], 'of': ['offering'], 'ho': ['home'], 'h': ['hygienic', 'home'], 'p': ['policeman', 'planet', 'patty', 'pail'], 'suc': ['success']}
    '''
    S1 = {'gh', 'pla', 'eco', 'c', 'n', 'st', 'loa', 'ga', 'ad', 'con', 'alt', 'imi', 'w', 'bi', 'agg', 'r', 'f', 'em', 'wet', 't', 'of', 'gl', 'ho', 'h', 'p', 'suc', 'iso'}
    S2 = {'cooking', 'offering', 'wooden', 'void', 'disclosure', 'home', 'knit', 'altitude', 'wick', 'policeman', 'patty', 'stack', 'catch', 'living', 'cleavage', 'achievement', 'buck', 'drill', 'hygienic', 'storey', 'tab', 'planet', 'soul', 'bind', 'pail', 'success', 'devastation', 'behest', 'contention', 'fantastic'}
    expected = {'pla': ['planet'], 'c': ['contention', 'cleavage', 'cooking', 'catch'], 'st': ['storey', 'stack'], 'con': ['contention'], 'alt': ['altitude'], 'w': ['wooden', 'wick'], 'bi': ['bind'], 'f': ['fantastic'], 't': ['tab'], 'of': ['offering'], 'ho': ['home'], 'h': ['hygienic', 'home'], 'p': ['policeman', 'planet', 'patty', 'pail'], 'suc': ['success']}
    return do_func3_tests(S1, S2, expected)


# ----------------------------------- Func. 4 ----------------------------------- #

def do_func4_tests(ID, size, expected):
    input_filename  = f'func4/{ID}.png'
    res = program.func4(input_filename, size)
    testlib.check_dict(res, expected)
    return 2

def test_func4_1(run=True):
    '''
    input_filename = 'func4/1.png'
    size = 5
    expected = {(125, 190, 250): 1, (184, 100, 249): 2, (115, 186, 199): 1, (139, 150, 176): 1, (250, 240, 236): 1, (125, 157, 232): 1}
    '''
    ID = 1
    size = 5
    expected = {(125, 190, 250): 1, (184, 100, 249): 2, (115, 186, 199): 1, (139, 150, 176): 1, (250, 240, 236): 1, (125, 157, 232): 1}
    return do_func4_tests(ID, size, expected)

def test_func4_2(run=True):
    '''
    input_filename = 'func4/2.png'
    size = 7
    expected = {(107, 219, 135): 2, (137, 148, 124): 4, (171, 209, 165): 1, (211, 255, 181): 1}
    '''
    ID = 2
    size = 7
    expected = {(107, 219, 135): 2, (137, 148, 124): 4, (171, 209, 165): 1, (211, 255, 181): 1}
    return do_func4_tests(ID, size, expected)

def test_func4_3(run=True):
    '''
    input_filename = 'func4/3.png'
    size = 9
    expected = {(142, 151, 152): 7, (165, 175, 131): 11, (226, 156, 224): 9, (223, 158, 255): 3, (188, 169, 223): 6, (199, 191, 225): 3, (196, 146, 223): 6, (138, 100, 155): 2, (230, 187, 144): 1, (240, 234, 171): 4}
    '''
    ID = 3
    size = 8
    expected = {(213, 132, 162): 2, (244, 228, 106): 1, (228, 210, 146): 1}
    return do_func4_tests(ID, size, expected)

def test_func4_4(run=True):
    '''
    input_filename = 'func4/4.png'
    size = 9
    expected = {(142, 151, 152): 7, (165, 175, 131): 11, (226, 156, 224): 9, (223, 158, 255): 3, (188, 169, 223): 6, (199, 191, 225): 3, (196, 146, 223): 6, (138, 100, 155): 2, (230, 187, 144): 1, (240, 234, 171): 4}
    '''
    ID = 4
    size = 9
    expected = {(142, 151, 152): 7, (165, 175, 131): 11, (226, 156, 224): 9, (223, 158, 255): 3, (188, 169, 223): 6, (199, 191, 225): 3, (196, 146, 223): 6, (138, 100, 155): 2, (230, 187, 144): 1, (240, 234, 171): 4}
    return do_func4_tests(ID, size, expected)

##----------------------------------- Func 5 ----------------------------------- ##

def do_test_func5(ID, K, M,  expected):
    file_in = f'func5/{ID}.txt'
    res = program.func5(file_in, K, M)
    testlib.check_val(res, expected)
    return 1

def test_func5_1(run=True):
    '''
    file_txt = 'func5/1.txt'
    K = 3
    M = 10
    expected = [[1, 2, 30],
                [4, 5, 60],
                [7, 8, 90],
                [10, 11, 120]
    '''
    ID = 1
    K = 3
    M = 10
    expected = [[1, 2, 30],
                [4, 5, 60],
                [7, 8, 90],
                [10, 11, 120]]
    return do_test_func5(ID, K, M, expected)


def test_func5_2(run=True):
    '''
    file_txt = 'func5/2.txt'
    K = 8
    P = 8
    expected = [[2688, 894, 521, 283, 849, 174],
                [591, 91, 5760, 7872, 826, 4032],
                [354, 593, 953, 711, 892, 889],
                [476, 279, 159, 420, 358, 9],
                [713, 258, 571, 954, 17, 159]]
    '''
    ID = 2
    K = 8
    P = 8
    expected = [[2688, 894, 521, 283, 849, 174],
                [591, 91, 5760, 7872, 826, 4032],
                [354, 593, 953, 711, 892, 889],
                [476, 279, 159, 420, 358, 9],
                [713, 258, 571, 954, 17, 159]]
    return do_test_func5(ID, K, P, expected)


def test_func5_3(run=True):
    '''
    file_txt = 'func5/3.txt'
    K = 5
    P = 14
    expected = [[238, 9100, 11970, 3360, 469, 747, 622, 877, 978, 5110, 299], [7770, 969, 350, 751, 801, 13230, 511, 996, 512, 10150, 141], [9240, 962, 964, 446, 279, 838, 13090, 772, 487, 819, 507], [8960, 504, 49, 917, 524, 202, 92, 806, 111, 817, 382], [809, 667, 977, 654, 818, 828, 834, 406, 233, 392, 748], [392, 412, 840, 369, 226, 173, 738, 13580, 3010, 538, 618], [599, 3, 854, 6230, 787, 27, 324, 683, 558, 416, 851], [8, 116, 756, 156, 959, 544, 11900, 33, 682, 624, 742], [3570, 779, 11900, 598, 351, 938, 142, 8400, 233, 699, 13160], [341, 578, 524, 197, 388, 58, 368, 121, 983, 10850, 88]]
    '''
    ID = 3
    K = 5
    P = 14
    expected = [[238, 9100, 11970, 3360, 469, 747, 622, 877, 978, 5110, 299], [7770, 969, 350, 751, 801, 13230, 511, 996, 512, 10150, 141], [9240, 962, 964, 446, 279, 838, 13090, 772, 487, 819, 507], [8960, 504, 49, 917, 524, 202, 92, 806, 111, 817, 382], [809, 667, 977, 654, 818, 828, 834, 406, 233, 392, 748], [392, 412, 840, 369, 226, 173, 738, 13580, 3010, 538, 618], [599, 3, 854, 6230, 787, 27, 324, 683, 558, 416, 851], [8, 116, 756, 156, 959, 544, 11900, 33, 682, 624, 742], [3570, 779, 11900, 598, 351, 938, 142, 8400, 233, 699, 13160], [341, 578, 524, 197, 388, 58, 368, 121, 983, 10850, 88]]
    return do_test_func5(ID, K, P, expected)


def test_func5_4(run=True):
    '''
    file_txt = 'func5/4.txt'
    K = 7
    P = 16
    expected = [[324, 715, 50, 852, 331, 205, 187, 316, 16, 696, 387, 849, 349], [293, 7728, 337, 314, 741, 342, 530, 801, 848, 15904, 117, 152, 879], [445, 974, 661, 438, 719, 68, 515, 9184, 845, 607, 780, 1568, 822], [883, 723, 265, 99, 711, 622, 425, 11648, 1456, 12432, 864, 12320, 184], [348, 4144, 6608, 947, 545, 367, 550, 814, 451, 974, 594, 887, 15680], [503, 429, 460, 9, 369, 946, 591, 65, 200, 663, 484, 274, 621], [284, 11760, 44, 908, 12656, 45, 249, 912, 8960, 290, 883, 9296, 934], [19, 415, 606, 523, 929, 9408, 3472, 608, 267, 128, 395, 687, 485], [285, 292, 9, 6944, 930, 460, 121, 612, 430, 7952, 193, 295, 837], [802, 7168, 2240, 591, 556, 759, 219, 216, 439, 83, 888, 536, 393], [41, 808, 412, 786, 744, 648, 72, 171, 219, 643, 888, 302, 839], [578, 74, 559, 650, 797, 452, 685, 509, 237, 652, 549, 814, 549], [485, 1456, 14336, 142, 956, 14560, 199, 764, 877, 342, 998, 408, 491], [671, 7728, 373, 3136, 4816, 642, 295, 503, 690, 429, 369, 712, 681], [933, 874, 513, 851, 275, 11200, 576, 386, 11424, 573, 75, 435, 820]]
    '''
    ID = 4
    K = 7
    P = 16
    expected = [[324, 715, 50, 852, 331, 205, 187, 316, 16, 696, 387, 849, 349], [293, 7728, 337, 314, 741, 342, 530, 801, 848, 15904, 117, 152, 879], [445, 974, 661, 438, 719, 68, 515, 9184, 845, 607, 780, 1568, 822], [883, 723, 265, 99, 711, 622, 425, 11648, 1456, 12432, 864, 12320, 184], [348, 4144, 6608, 947, 545, 367, 550, 814, 451, 974, 594, 887, 15680], [503, 429, 460, 9, 369, 946, 591, 65, 200, 663, 484, 274, 621], [284, 11760, 44, 908, 12656, 45, 249, 912, 8960, 290, 883, 9296, 934], [19, 415, 606, 523, 929, 9408, 3472, 608, 267, 128, 395, 687, 485], [285, 292, 9, 6944, 930, 460, 121, 612, 430, 7952, 193, 295, 837], [802, 7168, 2240, 591, 556, 759, 219, 216, 439, 83, 888, 536, 393], [41, 808, 412, 786, 744, 648, 72, 171, 219, 643, 888, 302, 839], [578, 74, 559, 650, 797, 452, 685, 509, 237, 652, 549, 814, 549], [485, 1456, 14336, 142, 956, 14560, 199, 764, 877, 342, 998, 408, 491], [671, 7728, 373, 3136, 4816, 642, 295, 503, 690, 429, 369, 712, 681], [933, 874, 513, 851, 275, 11200, 576, 386, 11424, 573, 75, 435, 820]]
    return do_test_func5(ID, K, P, expected)

# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(dirin, necessary, forbidden, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(dirin, necessary, forbidden)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(dirin, necessary, forbidden)
    testlib.check_list(res, expected)
    return 2

def test_ex1_1(run=True):
    '''
    dirname = 'ex1/AAA'
    necessary: ['ciao', 'mamma']
    forbidden: ['papa', 'nonno']
    expected = ['ex1/AAA/share/recollection/lamentable/dogsled.txt', 'ex1/AAA/heavy/tomorrow/flare/cellar.txt',
            'ex1/AAA/heavy/spoon/cranberry.txt', 'ex1/AAA/heavy/roster/prosecutor.txt', 'ex1/AAA/gifted/systemize/due.txt',
            'ex1/AAA/gifted/systemize/distinction.txt', 'ex1/AAA/share/help.txt', 'ex1/AAA/regime.txt', 'ex1/AAA/mayonnaise.txt']
    '''
    dirname   = 'ex1/AAA'
    necessary = ['ciao', 'mamma']
    forbidden = ['papa', 'nonno']
    expected  = ['ex1/AAA/share/recollection/lamentable/dogsled.txt', 'ex1/AAA/heavy/tomorrow/flare/cellar.txt',
            'ex1/AAA/heavy/spoon/cranberry.txt', 'ex1/AAA/heavy/roster/prosecutor.txt', 'ex1/AAA/gifted/systemize/due.txt',
            'ex1/AAA/gifted/systemize/distinction.txt', 'ex1/AAA/share/help.txt', 'ex1/AAA/regime.txt', 'ex1/AAA/mayonnaise.txt']
    return do_test_ex1(dirname, necessary, forbidden, expected)

def test_ex1_2(run=True):
    '''
    dirin = 'ex1/CCC'
    expected = ['ex1/C/bhk49r49.txt', 'ex1/C/A/a9fa5r54ol/inr6.txt', 'ex1/C/2o48dgq.txt', 'ex1/C/A/iahvg9mD9f.txt', 'ex1/C/A/r5g/74p52jhs.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/5lo3sa.txt', 'ex1/C/C/9n5/22zi524j/98469.txt', 'ex1/C/A/r5g/d501/tew8/l6j933qj.txt', 'ex1/C/a7u6kcehcm.txt', 'ex1/C/4q5ni/q5251as862.txt', 'ex1/C/A/lwc4z40fq.txt', 'ex1/C/B/Ch9d4f9.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/4lok.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/yoh.txt', 'ex1/C/A/r5g/d501/tew8/4tA4ca3g81k.txt', 'ex1/C/C/9n5/22zi524j/u2g/k2se7oh.txt', 'ex1/C/C/9n5/22zi524j/u2g/my1fc.txt', 'ex1/C/A/d6031a.txt', 'ex1/C/A/so8j7j3m.txt', 'ex1/C/B/p3zt345614/7j30i/f59a2l.txt', 'ex1/C/C/9n5/22zi524j/1iha5/nk7460q.txt', 'ex1/C/B/85bafd.txt', 'ex1/C/A/a9fa5r54ol/jfn.txt', 'ex1/C/B/p3zt345614/17nt/r0p8p5oe.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/p2q8/3gjbyrib.txt', 'ex1/C/C/9n5/22zi524j/u2g/m068.txt', 'ex1/C/B/33h294F.txt', 'ex1/C/439/53d23yd/092l53.txt', 'ex1/C/B/p3zt345614/7j30i/6hmre.txt', 'ex1/C/iuh5.txt', 'ex1/C/p1u34x59.txt', 'ex1/C/4q5ni/5bh9l253bc.txt', 'ex1/C/A/6f8554w.txt', 'ex1/C/C/4nd3c32.txt', 'ex1/C/A/a9fa5r54ol/9dlnpni/1bqeb8/m685c.txt', 'ex1/C/A/r5g/d501/w6i37c.txt', 'ex1/C/C/9n5/22zi524j/cj44.txt', 'ex1/C/B/p3zt345614/ei9ej73p/523hn6.txt', 'ex1/C/B/ape.txt']
    '''
    dirname = 'ex1/CCC'
    necessary = ['admission', 'anime', 'moonscape', 'reminder', 'orangutan']
    forbidden = ['riding', 'popsicle', 'laugh', 'meat', 'brainy']
    expected = ['ex1/CCC/steeple/splendid/tonight/aboard/crepe.txt',
                'ex1/CCC/steeple/splendid/photodiode/scent/applied.txt',
                'ex1/CCC/steeple/splendid/photodiode/mutton/divalent.txt',
                'ex1/CCC/steeple/nation/glut/revascularisation/standard.txt',
                'ex1/CCC/pride/olive/macro/xylophone/harpsichord.txt', 'ex1/CCC/pride/olive/lewd/ginseng/ruthless.txt',
                'ex1/CCC/pride/olive/lewd/dame/subsection.txt', 'ex1/CCC/pride/olive/lewd/dame/motor.txt',
                'ex1/CCC/pride/cytoplasm/semester/freight/recommendation.txt',
                'ex1/CCC/longboat/writer/cabinet/functional/judicious.txt',
                'ex1/CCC/longboat/spit/population/intentionality/nervous.txt',
                'ex1/CCC/longboat/manicure/lettuce/row/counter-force.txt',
                'ex1/CCC/longboat/manicure/lettuce/doggie/awful.txt',
                'ex1/CCC/longboat/blast/mainstream/bowler/summer.txt',
                'ex1/CCC/longboat/blast/classmate/brush/density.txt',
                'ex1/CCC/councilman/right/luxuriant/empowerment/gingerbread.txt',
                'ex1/CCC/councilman/right/luxuriant/district/taste.txt',
                'ex1/CCC/councilman/handle/girdle/armchair/chalice.txt',
                'ex1/CCC/contrail/conviction/quinoa/bunkhouse/subprime.txt',
                'ex1/CCC/contrail/conviction/monster/stormy/brown.txt',
                'ex1/CCC/steeple/splendid/commuter/elephant.txt', 'ex1/CCC/steeple/newsstand/makeshift/cell.txt',
                'ex1/CCC/steeple/newsstand/makeshift/anterior.txt',
                'ex1/CCC/steeple/nation/manifestation/regulator.txt', 'ex1/CCC/steeple/nation/glut/swamp.txt',
                'ex1/CCC/steeple/nation/glut/anesthesiology.txt', 'ex1/CCC/pride/polenta/abbey/pendulum.txt',
                'ex1/CCC/pride/olive/pollution/fibrosis.txt', 'ex1/CCC/pride/olive/macro/orangutan.txt',
                'ex1/CCC/pride/friendship/flow/crackers.txt', 'ex1/CCC/pride/cytoplasm/class/psychedelic.txt',
                'ex1/CCC/pride/cytoplasm/class/fanny-pack.txt', 'ex1/CCC/pride/cytoplasm/changeable/deputy.txt',
                'ex1/CCC/longboat/wardrobe/waiter/aggression.txt', 'ex1/CCC/longboat/blast/penny/triad.txt',
                'ex1/CCC/longboat/blast/penny/colt.txt', 'ex1/CCC/longboat/blast/penny/bean.txt',
                'ex1/CCC/longboat/blast/mainstream/tile.txt', 'ex1/CCC/longboat/blast/fade/valley.txt',
                'ex1/CCC/longboat/blast/classmate/nightingale.txt', 'ex1/CCC/councilman/right/prosecution/nothing.txt',
                'ex1/CCC/councilman/right/prosecution/lack.txt', 'ex1/CCC/councilman/handle/recliner/opera.txt',
                'ex1/CCC/councilman/handle/girdle/tension.txt', 'ex1/CCC/councilman/booking/thug/reporter.txt',
                'ex1/CCC/councilman/booking/thug/administration.txt', 'ex1/CCC/councilman/booking/personnel/low.txt',
                'ex1/CCC/contrail/worried/marketing/coil.txt', 'ex1/CCC/contrail/worried/co-producer/happening.txt',
                'ex1/CCC/contrail/kick-off/ruddy/celebrity.txt', 'ex1/CCC/contrail/conviction/vest/pronunciation.txt',
                'ex1/CCC/contrail/conviction/ark/smelting.txt', 'ex1/CCC/pride/friendship/sailing.txt',
                'ex1/CCC/longboat/wardrobe/reading.txt', 'ex1/CCC/longboat/wardrobe/eraser.txt',
                'ex1/CCC/longboat/manicure/bifocals.txt', 'ex1/CCC/longboat/industrious/homosexual.txt',
                'ex1/CCC/councilman/handle/inhibitor.txt', 'ex1/CCC/councilman/handle/ignorant.txt',
                'ex1/CCC/councilman/castanet/cold.txt', 'ex1/CCC/pride/feng.txt', 'ex1/CCC/inheritance/fame.txt',
                'ex1/CCC/can.txt']
    return do_test_ex1(dirname, necessary, forbidden, expected)

def test_ex1_3(run=True):
    '''
    dirin = 'ex1/B'
    expected = ['ex1/B/k5B3.txt', 'ex1/B/gn9.txt', 'ex1/B/2kdt437mi.txt', 'ex1/B/gem4.txt', 'ex1/B/DBvt2h4/8q2i3cb/37d4og.txt', 'ex1/B/hfc44ba/B7n33lv/gl88e642/3f8g.txt', 'ex1/B/DBvt2h4/8q2i3cb/qjc.txt', 'ex1/B/DBvt2h4/8q2i3cb/y4fcG6.txt', 'ex1/B/DBvt2h4/yr3ao93533.txt', 'ex1/B/hfc44ba/e7md39.txt', 'ex1/B/Ap81l6Cch.txt', 'ex1/B/vjv28.txt', 'ex1/B/hfc44ba/fm45.txt', 'ex1/B/DBvt2h4/55i4q73/5f4oxdfk.txt', 'ex1/B/DBvt2h4/5nfhb6adjd/1fe.txt', 'ex1/B/DBvt2h4/5nfhb6adjd/55Qbbc5t8m.txt', 'ex1/B/DBvt2h4/55i4q73/i5233.txt', 'ex1/B/DBvt2h4/8q2i3cb/33q.txt', 'ex1/B/DBvt2h4/8q2i3cb/pebd42g5B.txt', 'ex1/B/DBvt2h4/v1ahd.txt', 'ex1/B/hfc44ba/ummc6eb93/844d9i.txt']
    '''
    dirname = 'ex1/BBB'
    necessary = ['plastic', 'yak', 'still', 'sensitive', 'idea', 'woman']
    forbidden = ['gambling', 'cheek', 'topsail', 'opossum', 'elm', 'sponge']
    expected  = ['ex1/BBB/suffer/vegetation/writer/heir/omniscient/supply.txt',
     'ex1/BBB/suffer/prostanoid/weasel/world/collagen/improvement.txt',
     'ex1/BBB/suffer/prostanoid/amber/bafflement/autoimmunity/spank.txt',
     'ex1/BBB/suffer/prostanoid/amber/bafflement/autoimmunity/pain.txt',
     'ex1/BBB/suffer/lemon/condominium/homosexuality/lollipop/shopping.txt',
     'ex1/BBB/suffer/forecast/valuable/toothbrush/digit/subway.txt',
     'ex1/BBB/suffer/forecast/valuable/realm/cooperative/recovery.txt',
     'ex1/BBB/suffer/forecast/valuable/quiver/kiwi/industrialisation.txt',
     'ex1/BBB/suffer/forecast/laparoscope/chew/pawnshop/spider.txt',
     'ex1/BBB/suffer/forecast/commitment/stall/exposition/glove.txt',
     'ex1/BBB/suffer/catalog/hood/onerous/underpants/ant.txt',
     'ex1/BBB/percentage/wreck/transcribe/mix/math/canopy.txt',
     'ex1/BBB/percentage/wreck/transcribe/mix/diligent/communion.txt',
     'ex1/BBB/percentage/wreck/boolean/export/table/fighter.txt',
     'ex1/BBB/percentage/wreck/boolean/description/progression/habit.txt',
     'ex1/BBB/percentage/wreck/billion/police/confusion/caramel.txt',
     'ex1/BBB/percentage/wreck/billion/erection/snowmobiling/paperback.txt',
     'ex1/BBB/percentage/wreck/billion/erection/month/excite.txt',
     'ex1/BBB/percentage/wreck/billion/erection/living/diaphragm.txt',
     'ex1/BBB/percentage/rush/colorlessness/storm/ceaseless/tart.txt',
     'ex1/BBB/percentage/rush/colorlessness/leprosy/lend/encounter.txt',
     'ex1/BBB/percentage/rush/accommodation/message/quit/system.txt',
     'ex1/BBB/percentage/pigpen/stalk/trowel/summit/keep.txt', 'ex1/BBB/percentage/pigpen/stalk/trowel/ounce/haste.txt',
     'ex1/BBB/percentage/pigpen/intelligence/trait/hill/observe.txt',
     'ex1/BBB/percentage/pigpen/intelligence/minor/extinction/goal.txt',
     'ex1/BBB/percentage/club/octave/fingerling/pantsuit/cloudy.txt',
     'ex1/BBB/percentage/club/festive/tennis/seagull/nickname.txt',
     'ex1/BBB/percentage/club/festive/shallows/decorate/mileage.txt',
     'ex1/BBB/percentage/club/festive/shallows/creek/mathematics.txt',
     'ex1/BBB/bookcase/heater/maddening/thumb/birthday/doll.txt',
     'ex1/BBB/bookcase/heater/maddening/livestock/efficiency/chestnut.txt',
     'ex1/BBB/bookcase/developmental/aunt/camper/dangerous/divide.txt',
     'ex1/BBB/bookcase/developmental/aunt/apricot/breath/victory.txt',
     'ex1/BBB/bookcase/brave/cultivator/equal/secure/direct.txt',
     'ex1/BBB/bookcase/brave/cultivator/abbey/vitality/spank.txt',
     'ex1/BBB/app/motive/profess/chafe/pavilion/eleventh.txt', 'ex1/BBB/app/motive/kitty/chateau/shark/plight.txt',
     'ex1/BBB/app/motive/kitty/chateau/shark/dot.txt', 'ex1/BBB/app/motive/diagnosis/mailbox/seabass/serum.txt',
     'ex1/BBB/app/filly/trance/trunk/consignment/girl.txt', 'ex1/BBB/app/filly/trance/trunk/boost/jealousy.txt',
     'ex1/BBB/app/filly/rocker/initiate/cartoon/composer.txt', 'ex1/BBB/app/filly/infusion/warlord/trashy/judgment.txt',
     'ex1/BBB/app/filly/infusion/warlord/trashy/acquaintance.txt',
     'ex1/BBB/app/filly/infusion/warlord/outrigger/littleneck.txt',
     'ex1/BBB/app/fertilizer/journalism/speak/cougar/ex-husband.txt',
     'ex1/BBB/app/fertilizer/human/periodical/likeable/serve.txt',
     'ex1/BBB/app/fertilizer/human/assorted/media/membership.txt',
     'ex1/BBB/app/fertilizer/controller/ligand/cluster/doorpost.txt',
     'ex1/BBB/app/entrance/slavery/shootdown/marxism/quit.txt',
     'ex1/BBB/app/entrance/cribbage/pastoralist/wing/drip.txt', 'ex1/BBB/suffer/vegetation/writer/transition/twins.txt',
     'ex1/BBB/suffer/vegetation/news/pursuit/bibliography.txt', 'ex1/BBB/suffer/vegetation/gasket/threshold/cheat.txt',
     'ex1/BBB/suffer/vegetation/gasket/neuropathologist/aglet.txt',
     'ex1/BBB/suffer/lemon/woodchuck/insight/heart-throb.txt', 'ex1/BBB/suffer/lemon/helium/founder/composer.txt',
     'ex1/BBB/suffer/lemon/fall/happiness/flair.txt', 'ex1/BBB/suffer/lemon/condominium/vitro/trolley.txt',
     'ex1/BBB/suffer/forecast/valuable/adapter/setting.txt', 'ex1/BBB/suffer/forecast/crabby/crest/supernatural.txt',
     'ex1/BBB/suffer/forecast/commitment/spokeswoman/cube.txt',
     'ex1/BBB/suffer/forecast/commitment/repository/abandoned.txt',
     'ex1/BBB/suffer/forecast/commitment/chapel/amenity.txt', 'ex1/BBB/suffer/catalog/hood/processor/knuckle.txt',
     'ex1/BBB/suffer/catalog/hood/headline/doll.txt', 'ex1/BBB/percentage/wreck/cornmeal/advocacy/dollar.txt',
     'ex1/BBB/percentage/wreck/boolean/plastic/spin.txt', 'ex1/BBB/percentage/wreck/boolean/headphones/male.txt',
     'ex1/BBB/percentage/wreck/boolean/headphones/concentration.txt',
     'ex1/BBB/percentage/rush/cooking/muscatel/miscommunication.txt',
     'ex1/BBB/percentage/rush/cooking/awful/speech.txt', 'ex1/BBB/percentage/rush/cooking/awful/relationship.txt',
     'ex1/BBB/percentage/rush/cooking/ambiguous/shear.txt', 'ex1/BBB/percentage/rush/colorlessness/storm/fish.txt',
     'ex1/BBB/percentage/rush/colorlessness/leprosy/means.txt',
     'ex1/BBB/percentage/rush/colorlessness/leprosy/better.txt',
     'ex1/BBB/percentage/rush/accommodation/stereotyped/sort.txt',
     'ex1/BBB/percentage/pigpen/stalk/overview/miscommunication.txt',
     'ex1/BBB/percentage/pigpen/someplace/come/lever.txt', 'ex1/BBB/percentage/pigpen/intelligence/trait/tour.txt',
     'ex1/BBB/percentage/pigpen/intelligence/trait/quiver.txt',
     'ex1/BBB/percentage/pigpen/intelligence/minor/volatility.txt',
     'ex1/BBB/percentage/pigpen/intelligence/census/humdrum.txt', 'ex1/BBB/percentage/club/kill/champion/way.txt',
     'ex1/BBB/percentage/club/immense/sand/vibration.txt', 'ex1/BBB/percentage/club/festive/tennis/flatboat.txt',
     'ex1/BBB/percentage/club/festive/shallows/anticodon.txt', 'ex1/BBB/percentage/club/festive/mineral/mincemeat.txt',
     'ex1/BBB/bookcase/heater/maddening/thumb/versed.txt', 'ex1/BBB/bookcase/heater/maddening/thumb/commonsense.txt',
     'ex1/BBB/bookcase/heater/maddening/mourn/memorial.txt',
     'ex1/BBB/bookcase/developmental/plight/sherry/dynamite.txt',
     'ex1/BBB/bookcase/developmental/aunt/carotene/lute.txt', 'ex1/BBB/bookcase/developmental/aunt/camper/laughter.txt',
     'ex1/BBB/bookcase/developmental/afoul/astrolabe/happiness.txt',
     'ex1/BBB/bookcase/brave/war/priesthood/washtub.txt', 'ex1/BBB/bookcase/brave/war/chapel/song.txt',
     'ex1/BBB/bookcase/brave/war/chapel/pipe.txt', 'ex1/BBB/app/sunglasses/tow-truck/nifty/appeal.txt',
     'ex1/BBB/app/sunglasses/tow-truck/assistance/shootdown.txt', 'ex1/BBB/app/sunglasses/Early/rescue/scallops.txt',
     'ex1/BBB/app/motive/syndicate/statin/exposition.txt', 'ex1/BBB/app/motive/profess/washtub/topsail.txt',
     'ex1/BBB/app/motive/kitty/jewel/temptress.txt', 'ex1/BBB/app/motive/kitty/chateau/troubled.txt',
     'ex1/BBB/app/filly/yam/junk/tune.txt', 'ex1/BBB/app/filly/rocker/emitter/quota.txt',
     'ex1/BBB/app/filly/rocker/emitter/polo.txt', 'ex1/BBB/app/filly/corps/slimy/prostanoid.txt',
     'ex1/BBB/app/filly/corps/inspiration/wasting.txt', 'ex1/BBB/app/fertilizer/overcome/gloom/daughter.txt',
     'ex1/BBB/app/fertilizer/dragonfly/transaction/overhead.txt', 'ex1/BBB/app/fertilizer/dragonfly/cable/exit.txt',
     'ex1/BBB/suffer/vegetation/writer/keeper.txt', 'ex1/BBB/suffer/vegetation/list/dialect.txt',
     'ex1/BBB/suffer/prostanoid/weasel/soldier.txt', 'ex1/BBB/suffer/prostanoid/amber/walkway.txt',
     'ex1/BBB/suffer/forecast/laparoscope/resemblance.txt', 'ex1/BBB/suffer/forecast/crabby/say.txt',
     'ex1/BBB/suffer/catalog/durian/element.txt', 'ex1/BBB/percentage/wreck/transcribe/authenticity.txt',
     'ex1/BBB/percentage/wreck/billion/tread.txt', 'ex1/BBB/percentage/club/octave/nougat.txt',
     'ex1/BBB/bookcase/heater/maddening/ragged.txt', 'ex1/BBB/bookcase/heater/maddening/lay.txt',
     'ex1/BBB/bookcase/heater/insure/slapstick.txt', 'ex1/BBB/bookcase/developmental/plight/shackle.txt',
     'ex1/BBB/bookcase/developmental/cute/residue.txt', 'ex1/BBB/bookcase/developmental/aunt/irrigation.txt',
     'ex1/BBB/bookcase/brave/obsidian/mailing.txt', 'ex1/BBB/bookcase/brave/cultivator/emanate.txt',
     'ex1/BBB/app/filly/trance/inquiry.txt', 'ex1/BBB/app/filly/rocker/commotion.txt',
     'ex1/BBB/app/filly/corps/annual.txt', 'ex1/BBB/app/fertilizer/overcome/crocodile.txt',
     'ex1/BBB/app/fertilizer/overcome/cluster.txt', 'ex1/BBB/app/fertilizer/controller/hyacinth.txt',
     'ex1/BBB/app/entrance/knock/road.txt', 'ex1/BBB/suffer/vegetation/belief.txt', 'ex1/BBB/suffer/lemon/mutt.txt',
     'ex1/BBB/suffer/catalog/sky.txt', 'ex1/BBB/percentage/wreck/soliloquy.txt',
     'ex1/BBB/percentage/wreck/eyestrain.txt', 'ex1/BBB/percentage/rush/raven.txt', 'ex1/BBB/percentage/rush/manor.txt',
     'ex1/BBB/bookcase/heater/flicker.txt', 'ex1/BBB/bookcase/brave/packaging.txt', 'ex1/BBB/bookcase/brave/deer.txt',
     'ex1/BBB/app/sunglasses/yourself.txt', 'ex1/BBB/app/motive/drag.txt', 'ex1/BBB/percentage/chaplain.txt',
     'ex1/BBB/bookcase/endoderm.txt', 'ex1/BBB/envious.txt']
    return do_test_ex1(dirname, necessary, forbidden, expected)



# ----------------------------------- EX. 2----------------------------------- #


def do_ex2_test(root_as_list, expected_as_list, expected):
    if not DEBUG:
        try:
            root = tree.BinaryTree.fromList(root_as_list)
            isrecursive.decorate_module(program)
            program.ex2(root)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    root  = tree.BinaryTree.fromList(root_as_list)
    root2 = tree.BinaryTree.fromList(root_as_list)
    toor  = tree.BinaryTree.fromList(expected_as_list)
    res = program.ex2(root)
    if root == root2:
        raise Exception("The tree has not been modified at all / L'albero non è stato modificato per nulla")
    if root != toor:
        raise Exception("The tree has not been modified correctly / L'albero non è stato modificato correttamente")
    if res != expected:
        raise Exception("The function does not return the correct value / La funzione non restituisce il valore corretto")
    return 2


def test_ex2_1(run=True):
    '''
        root      
                    | profondità
         1          |  0
        / \         |
       2   3        |  1
      / \ / \       |
     4  5 6  7      |  2
    / \    \        |
   8   9   10       |  3
Diventerà:
                    | profondità
         1          |  0
        / \         |
       3   2        |  1    2 spostati
      / \ / \       |
     6  7 4  5      |  2
    /    / \        |
   10   9   8       |  3    3 spostati
      expected = 5
    '''
    root_as_list = [1,  [2, [4, [8, None, None],
                                [9, None, None]],
                            [5, None, None]],
                        [3, [6, None,
                                [10, None, None]],
                            [7, None, None]]]
    expected_as_list = [1,  [3, [6, [10, None, None],
                                    None],
                                [7, None, None]],
                            [2, [4, [9, None, None],
                                    [8, None, None]],
                                [5, None, None]]]
    expected = 5
    return do_ex2_test(root_as_list, expected_as_list, expected)

def test_ex2_2(run=True):
    '''
              root       
          ______2______  
         |             | 
      __27__        ___-3
     |      |      |
    _-5_    9_    _20
   |    |     |  |
   2   -1     1  8

       expected = 5
    '''
    root_as_list     = [2,  [27, [-5, None,
                                      [10, None, None]],
                                 [9,  None,
                                      [24, None, None]]],
                            [-3, [20, [-1, None, None],
                                      None],
                                 None]]
    expected_as_list = [2, [-3, [20, None, [-1, None, None]], None], [27, [-5, [10, None, None], None], [9, [24, None, None], None]]]
    expected = 5
    return do_ex2_test(root_as_list, expected_as_list, expected)


def test_ex2_3(run=True):
    '''
    A big tree
    expected = 151
    '''
    root_as_list     = [2, [11, [19, [10, [20, [17, [-6, [-9, [22, None, [19, None, None]], None], [10, None, None]], [-3, [17, None, None], [-2, None, None]]], [25, [-9, [21, None, None], None], [27, [25, [22, None, [-5, None, None]], [24, None, None]], [4, None, None]]]], [30, None, [3, None, [2, [20, None, None], None]]]], [-10, [6, [-5, None, None], [10, [4, None, None], [13, None, None]]], [21, None, [-6, [18, None, [26, None, None]], [-4, None, None]]]]], [13, [2, [29, [30, [23, [8, None, [9, [14, None, None], [6, [13, None, None], None]]], None], [-6, [14, [18, [15, None, None], None], [2, None, None]], [30, [3, None, None], [10, None, None]]]], [2, [-5, None, [-4, [10, None, [23, None, None]], [16, [20, None, None], None]]], [26, [27, [-8, None, [-10, [28, None, None], [7, None, None]]], [-8, None, None]], [17, [-10, None, None], [19, None, None]]]]], [11, [9, [7, [26, [27, None, None], [-10, [17, None, None], None]], [30, [27, None, None], None]], [-1, [27, [12, None, None], [-1, [25, None, None], None]], [-4, [-6, [-9, None, None], [-1, None, None]], [4, None, None]]]], [23, [8, [27, [22, [1, [-9, None, [-2, None, None]], [23, [1, None, None], None]], [-4, [-1, None, None], [8, None, [22, None, None]]]], [16, [4, [10, None, None], [26, None, None]], [0, [1, None, None], [-2, [27, [-3, None, None], [21, None, None]], None]]]], None], [30, None, [20, [26, [1, None, None], None], [21, [12, [-1, None, None], None], [14, None, None]]]]]]], [6, [17, [24, [4, None, [18, None, None]], [-9, [29, None, None], None]], [1, [20, [4, None, None], None], [10, None, [19, None, None]]]], [7, [12, [3, None, None], None], [1, [23, [24, None, None], None], [17, None, None]]]]]], [12, [-5, [13, [2, [22, [8, [21, None, None], [7, None, None]], [18, None, None]], [17, [-7, None, None], [-6, None, [4, None, None]]]], None], [4, [15, None, [-6, [25, [2, [-5, None, [-8, None, None]], [18, [8, None, None], None]], [-1, [16, None, None], [30, None, None]]], [12, [12, [-3, [17, None, None], None], [-2, None, [9, None, None]]], None]]], [1, [13, [-3, [2, [0, None, None], [11, None, None]], [-1, None, [19, [20, None, [18, None, None]], None]]], [20, [15, [30, [29, None, None], None], [18, [20, None, [14, None, None]], [27, [17, None, None], None]]], [3, [8, [14, None, None], [-4, None, None]], [20, [29, None, None], [19, None, [-5, None, None]]]]]], [20, [-10, [-9, [14, None, [-7, None, None]], [2, [19, None, None], [9, None, None]]], [16, None, [14, None, None]]], [0, [28, [11, None, [-1, [25, None, None], [14, None, None]]], [-9, None, None]], [29, None, [1, None, None]]]]]]], [4, [6, [29, [22, [1, [27, None, [12, None, None]], None], None], None], [5, [6, [15, [8, [21, [20, None, None], [2, None, [-1, [19, None, None], [23, None, None]]]], [-4, [24, None, None], None]], [28, [13, [19, None, None], None], None]], [22, None, [23, [-7, [-8, None, None], [10, None, None]], [26, None, [22, None, [-2, None, None]]]]]], [8, [14, [15, [24, None, None], None], [6, None, None]], [30, [11, None, [0, [-4, None, None], [-4, [-1, None, None], None]]], [-4, [-4, None, [9, None, None]], None]]]]], [9, [-5, [-1, [29, [-8, None, None], [21, [26, None, None], None]], None], None], [23, [-2, [-8, [-6, [-5, [3, None, None], None], [-9, [24, None, None], [-5, None, None]]], [3, [6, None, [16, None, [20, None, None]]], None]], [21, [22, [25, None, [17, None, None]], None], [-10, [1, None, [14, None, None]], None]]], [-4, [7, [28, [15, None, None], [-4, None, [10, None, None]]], [-5, [-10, [24, None, None], [0, None, [27, None, None]]], [-8, None, None]]], [-10, None, None]]]]]]]
    expected_as_list = [2, [12, [-5, [4, [15, [-6, [25, [-1, [16, None, None], [30, None, None]], [2, [-5, [-8, None, None], None], [18, None, [8, None, None]]]], [12, None, [12, [-3, None, [17, None, None]], [-2, [9, None, None], None]]]], None], [1, [20, [-10, [16, None, [14, None, None]], [-9, [14, [-7, None, None], None], [2, [9, None, None], [19, None, None]]]], [0, [29, None, [1, None, None]], [28, [11, [-1, [25, None, None], [14, None, None]], None], [-9, None, None]]]], [13, [-3, [-1, None, [19, None, [20, None, [18, None, None]]]], [2, [0, None, None], [11, None, None]]], [20, [3, [8, [-4, None, None], [14, None, None]], [20, [19, None, [-5, None, None]], [29, None, None]]], [15, [30, None, [29, None, None]], [18, [27, [17, None, None], None], [20, None, [14, None, None]]]]]]]], [13, [2, [17, [-7, None, None], [-6, [4, None, None], None]], [22, [8, [7, None, None], [21, None, None]], [18, None, None]]], None]], [4, [9, [-5, None, [-1, [29, [21, [26, None, None], None], [-8, None, None]], None]], [23, [-4, [7, [-5, [-10, [0, None, [27, None, None]], [24, None, None]], [-8, None, None]], [28, [15, None, None], [-4, [10, None, None], None]]], [-10, None, None]], [-2, [-8, [3, [6, [16, None, [20, None, None]], None], None], [-6, [-5, None, [3, None, None]], [-9, [-5, None, None], [24, None, None]]]], [21, [-10, [1, [14, None, None], None], None], [22, [25, [17, None, None], None], None]]]]], [6, [29, None, [22, [1, None, [27, None, [12, None, None]]], None]], [5, [8, [14, [6, None, None], [15, [24, None, None], None]], [30, [-4, [-4, [9, None, None], None], None], [11, None, [0, [-4, [-1, None, None], None], [-4, None, None]]]]], [6, [15, [28, [13, None, [19, None, None]], None], [8, [21, [2, None, [-1, [23, None, None], [19, None, None]]], [20, None, None]], [-4, None, [24, None, None]]]], [22, [23, [-7, [10, None, None], [-8, None, None]], [26, [22, None, [-2, None, None]], None]], None]]]]]], [11, [19, [-10, [6, [10, [4, None, None], [13, None, None]], [-5, None, None]], [21, [-6, [18, [26, None, None], None], [-4, None, None]], None]], [10, [20, [25, [-9, None, [21, None, None]], [27, [4, None, None], [25, [22, [-5, None, None], None], [24, None, None]]]], [17, [-6, [10, None, None], [-9, [22, [19, None, None], None], None]], [-3, [-2, None, None], [17, None, None]]]], [30, [3, None, [2, None, [20, None, None]]], None]]], [13, [6, [17, [1, [20, None, [4, None, None]], [10, [19, None, None], None]], [24, [4, [18, None, None], None], [-9, None, [29, None, None]]]], [7, [1, [23, None, [24, None, None]], [17, None, None]], [12, [3, None, None], None]]], [2, [29, [2, [-5, [-4, [10, [23, None, None], None], [16, None, [20, None, None]]], None], [26, [17, [-10, None, None], [19, None, None]], [27, [-8, [-10, [28, None, None], [7, None, None]], None], [-8, None, None]]]], [30, [23, None, [8, None, [9, [6, [13, None, None], None], [14, None, None]]]], [-6, [30, [3, None, None], [10, None, None]], [14, [18, None, [15, None, None]], [2, None, None]]]]], [11, [23, [8, None, [27, [22, [-4, [-1, None, None], [8, [22, None, None], None]], [1, [-9, [-2, None, None], None], [23, None, [1, None, None]]]], [16, [0, [1, None, None], [-2, None, [27, [-3, None, None], [21, None, None]]]], [4, [10, None, None], [26, None, None]]]]], [30, [20, [26, None, [1, None, None]], [21, [14, None, None], [12, [-1, None, None], None]]], None]], [9, [7, [30, [27, None, None], None], [26, [27, None, None], [-10, None, [17, None, None]]]], [-1, [-4, [-6, [-1, None, None], [-9, None, None]], [4, None, None]], [27, [12, None, None], [-1, None, [25, None, None]]]]]]]]]]
    expected = 151
    return do_ex2_test(root_as_list, expected_as_list, expected)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1,  test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,  test_ex1_2, test_ex1_3,
    test_ex2_1,    test_ex2_2, test_ex2_3,
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
