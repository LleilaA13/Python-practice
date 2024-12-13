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
# DEBUG = True
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

def do_func1_tests(int_list, m, n, expected):
    res = program.func1(int_list, m, n)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_dict(res, expected)
    return 1


def test_func1_1(run=True):
    '''
    int_list = [4, 4, 10, 4, 2, 1, 2]
    m = 3
    n = 8
    expected = {1: 1, 10: 1, 2: 2}
    '''
    int_list = [4, 4, 10, 4, 2, 1, 2]
    m = 3
    n = 8
    expected = {1: 1, 10: 1, 2: 2}
    return do_func1_tests(int_list, m, n, expected)

def test_func1_2(run=True):
    '''
    int_list = [-5, 4, 5, 10, 3, -1, 2, 12, 10, 11, 10]
    m = 3
    n = 8
    expected = {10: 3, 11: 1, 12: 1, -5: 1, -1: 1}
    '''
    int_list = [-5, 4, 5, 10, 3, -1, 2, 12, 10, 11, 10]
    m = 0
    n = 8
    expected = {10: 3, 11: 1, 12: 1, -5: 1, -1: 1}
    return do_func1_tests(int_list, m, n, expected)

def test_func1_3(run=True):
    '''
    int_list = []
    m = 0
    n = 5
    expected = {}
    '''
    int_list = []
    m = 0
    n = 5
    expected = {}
    return do_func1_tests(int_list, m, n, expected)

def test_func1_4(run=True):
    '''
    int_list = [-78, 10, 76, 82, -27, -39, -65, -19, 74, 18, 20, -25, -38, -71, -52, -49, -69, 21, -27, 58, 20]
    m = -52
    n = 19
    expected = {20: 2, 21: 1, -78: 1, -71: 1, 58: 1, -69: 1, -65: 1, 74: 1, 76: 1, 82: 1}
    '''
    int_list = [-78, 10, 76, 82, -27, -39, -65, -19, 74, 18, 20, -25, -38, -71, -52, -49, -69, 21, -27, 58, 20]
    m = -52
    n = 19
    expected = {20: 2, 21: 1, -78: 1, -71: 1, 58: 1, -69: 1, -65: 1, 74: 1, 76: 1, 82: 1}
    return do_func1_tests(int_list, m, n, expected)


def do_func2_tests(str1, str2, expected):
    res = program.func2(str1, str2)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_val(res, expected)
    return 1


def test_func2_1(run=True):
    '''
    str1 = 'plane'
    str2 = 'react'
    expected = 'PEACE'
    '''
    str1 = 'plane'
    str2 = 'react'
    expected = 'PEACE'
    return do_func2_tests(str1, str2, expected)

def test_func2_2(run=True):
    '''
    str1 = 'staircases'
    str2 = 'granulates'
    expected = 'GRAIRCASES'
    '''
    str1 = 'staircases'
    str2 = 'granulates'
    expected = 'GRAIRCASES'
    return do_func2_tests(str1, str2, expected)

def test_func2_3(run=True):
    '''
    str1 = 'infatuation'
    str2 = 'intangibles'
    expected = 'INFANGABIEN'
    '''
    str1 = 'infatuation'
    str2 = 'intangibles'
    expected = 'INFANGABIEN'
    return do_func2_tests(str1, str2, expected)

def test_func2_4(run=True):
    '''
    str1 = 'deliberately',
    str2 = 'reproductive'
    expected = 'DELIBDRATELE'
    '''
    str1 = 'deliberately'
    str2 = 'reproductive'
    expected = 'DELIBDRATELE'
    return do_func2_tests(str1, str2, expected)


def do_func3_tests(L0, L1, expected):
    res = program.func3(L0, L1)
    testlib.check_val(res, expected)
    return 1

def test_func3_1(run=True):
    '''
    L0 = ['ab', 'o o']
    L1 = [2, 3]
    expected = "ababo oo oo o"
    '''
    L0 = ['ab', 'o o']
    L1 = [2, 3]
    expected = "ababo oo oo o"
    return do_func3_tests(L0, L1, expected)

def test_func3_2(run=True):
    '''
    L0 = ['quick', 'brow', 'fox']
    L1 = [2, 0, 2]
    expected = "quickquickfoxfox"
    '''
    L0 = ['quick', 'brow', 'fox']
    L1 = [2, 0, 2]
    expected = "quickquickfoxfox"
    return do_func3_tests(L0, L1, expected)

def test_func3_3(run=True):
    '''
    L0 = ['h', 'e', 'l', 'o']
    L1 = [1, 1, 2, 1]
    expected = "hello"
    '''
    L0 = ['h', 'e', 'l', 'o']
    L1 = [1, 1, 2, 1]
    expected = "hello"
    return do_func3_tests(L0, L1, expected)

def test_func3_4(run=True):
    '''
    L0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    expected = "bccdddeeeefffffgggggghhhhhhhiiiiiiii"
    '''
    L0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    expected = "bccdddeeeefffffgggggghhhhhhhiiiiiiii"
    return do_func3_tests(L0, L1, expected)

def do_func4_tests(dict_in, expected):
    res = program.func4(dict_in)
    testlib.check_list(res, expected)
    return 1.5

def test_func4_1(run=True):
    '''
    dict_in = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
    expected = [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]]
    '''
    dict_in = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
    expected = [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]]
    return do_func4_tests(dict_in, expected)

def test_func4_2(run=True):
    '''
    dict_in = {3: {'name': 'Steve', 'age': 25, 'marks': 60}, 2: {'name': 'Anil', 'age': 23, 'marks': 75}, 1: {'name': 'Asha', 'age': 20, 'marks': 70}}
    expected = [[1, {'name': 'Asha', 'age': 20, 'marks': 70}], [2, {'name': 'Anil', 'age': 23, 'marks': 75}], [3, {'name': 'Steve', 'age': 25, 'marks': 60}]]
    '''
    dict_in = {3: {'name': 'Steve', 'age': 25, 'marks': 60}, 2: {'name': 'Anil', 'age': 23, 'marks': 75}, 1: {'name': 'Asha', 'age': 20, 'marks': 70}}
    expected = [[1, {'name': 'Asha', 'age': 20, 'marks': 70}], [2, {'name': 'Anil', 'age': 23, 'marks': 75}], [3, {'name': 'Steve', 'age': 25, 'marks': 60}]]
    return do_func4_tests(dict_in, expected)


def test_func4_3(run=True):
    '''
    dict_in = {'A': {'Augusta', 'Arvada', 'Aurora', 'Albany', 'Arlington', 'Atlantic City', 'Allentown', 'Asheville', 'Atlanta', 'Akron', 'Alexandria', 'Antioch', 'Abilene', 'Anaheim', 'Ann Arbor', 'Athens', 'Appleton', 'Amarillo', 'Apple Valley', 'Aberdeen', 'Austin', 'Albuquerque', 'Anchorage'}, 'B': {'Baton Rouge', 'Boise City', 'Berkeley', 'Billings', 'Brighton', 'Beaumont', 'Bradenton', 'Burlington', 'Bel Air', 'Burbank', 'Birmingham', 'Bonita Springs', 'Barnstable', 'Baltimore', 'Buffalo', 'Brownsville', 'Boise', 'Boston', 'Bremerton', 'Bakersfield', 'Bethlehem', 'Bloomington', 'Boulder', 'Bridgeport', 'Bellevue', 'Bryan'}, 'C': {'Clearwater', 'Carrollton', 'Corona', 'Cambridge', 'Clarke County', 'Clarksville', 'Champaign', 'Chesapeake', 'Chula Vista', 'Charleston', 'Columbus', 'Corpus Christi', 'Cape Coral', 'Colorado Springs', 'Canton', 'Chandler', 'Chicago', 'Columbia', 'Cathedral City', 'Costa Mesa', 'Cleveland', 'Cincinnati', 'Concord', 'Coral Springs', 'Charlotte', 'Chattanooga', 'Cedar Rapids', 'College Station', 'Cary'}, 'D': {'Downey', 'Davidson County', 'Dayton', 'Dallas', 'Daly City', 'Davenport', 'Durham', 'Des Moines', 'Duluth', 'Detroit', 'Danbury', 'Deltona', 'Daytona Beach', 'Denver', 'Denton'}, 'E': {'Evansville', 'Erie', 'Escondido', 'El Monte', 'Elizabeth', 'El Paso', 'Elk Grove', 'Eugene', 'Elkhart'}, 'F': {'Fargo', 'Fort Wayne', 'Frederick', 'Fairfield', 'Fresno', 'Fontana', 'Fort Collins', 'Fitchburg', 'Fort Walton Beach', 'Fort Worth', 'Flint', 'Fort Smith', 'Fayetteville', 'Fort Lauderdale', 'Fullerton', 'Fremont'}, 'G': {'Green Bay', 'Grayslake', 'Gainesville', 'Garden Grove', 'Glendale', 'Grand Prairie', 'Grand Rapids', 'Gastonia', 'GreenBay', 'Greensboro', 'Greenville', 'Gilbert', 'Gulfport-Biloxi', 'Garland'}, 'H': {'Havre de Grace', 'Henderson', 'Hartford', 'Honolulu', 'Hemet', 'Hollywood', 'Hagerstown', 'Harrisburg', 'Houma', 'Hampton', 'Huntington Beach', 'High Point', 'Hayward', 'Hickory', 'Huntsville', 'Huntington', 'Howell', 'Hesperia', 'Harlingen', 'Houston', 'Hialeah'}, 'I': {'Irvine', 'Irving', 'Indianapolis', 'Independence', 'Inglewood'}, 'J': {'Jersey City', 'Jacksonville', 'Jefferson', 'Johnson City', 'Joliet', 'Jackson'}, 'K': {'Knoxville', 'Killeen', 'Kailua', 'Kalamazoo', 'Kaneohe', 'Kenosha', 'Kansas City', 'Kissimmee', 'Kennewick'}, 'L': {'Lafayette', 'Little Rock', 'Las Vegas', 'Long Beach', 'Laredo', 'Lacey', 'Lincoln', 'Lancaster', 'Lakeland', 'Lansing', 'Lubbock', 'Leominster', 'Lorain', 'Las Cruces', 'Lowell', 'Lakewood', 'Lexington', 'Louisville', 'Los Angeles', 'Lewisville', 'Layton', 'Lake Charles'}, 'M': {'Minneapolis', 'Merced', 'McAllen', 'Myrtle Beach', 'Manchester', 'Murrieta', 'Monroe', 'Macon', 'Miami', 'Medford', 'Madison', 'Mesquite', 'Memphis', 'Muskegon', 'Melbourne', 'Murfreesboro', 'Marina', 'Marysville', 'Montgomery', 'Mesa', 'McHenry', 'Milwaukee', 'Modesto', 'Monterey', 'Mission Viejo', 'Moreno Valley', 'Mobile', 'Miramar'}, 'N': {'New Haven', 'New Orleans', 'New London', 'Norwich', 'Newport News', 'Newburgh', 'North Las Vegas', 'North Charleston', 'New York', 'Naperville', 'Nashua', 'North Port', 'Nashville', 'Naples', 'Norwalk', 'Newark', 'New Bedford', 'New York City', 'Norman', 'Normal', 'Norfolk'}, 'O': {'Olathe', 'Ocala', 'Overland Park', 'Oceanside', 'Olympia', 'Odessa', 'Oxnard', 'Orange', 'Orem', 'Omaha', 'Orlando', 'Ontario', 'Ogden', 'Oakland', 'Oklahoma City'}, 'P': {'Panama City', 'Palm Springs', 'Port Arthur', 'Poughkeepsie', 'Portsmouth', 'Port Orange', 'Peoria', 'Pensacola', 'Palm Bay', 'Providence', 'Philadelphia', 'Plano', 'Pomona', 'Pueblo', 'Pembroke Pines', 'Phoenix', 'Provo', 'Punta Gorda', 'Pompano Beach', 'Pasadena', 'Paterson', 'Palmdale', 'Portland', 'Port Saint Lucie', 'Pittsburgh', 'Port St. Lucie'}, 'R': {'Richmond', 'Rockford', 'Raleigh', 'Richland', 'Redding', 'Reading', 'Reno', 'Riverside', 'Roseville', 'Roanoke', 'Round Lake Beach', 'Rancho Cucamonga', 'Rochester', 'Racine', 'Richmond County'}, 'S': {'Santa Barbara', 'Sterling Heights', 'Saint Petersburg', 'San Jose', 'Sioux Falls', 'Shreveport', 'Springdale', 'Santa Cruz', 'Salem', 'St. Petersburg', 'Seattle', 'St. Paul', 'Santa Maria', 'Simi Valley', 'Syracuse', 'Saginaw', 'Saint Paul', 'Sioux City', 'San Francisco', 'Spokane', 'Santa Rosa', 'San Diego', 'Sebastian', 'Springfield', 'Santa Clara', 'San Buenaventura', 'Stamford', 'Sacramento', 'Stockton', 'Sunnyvale', 'San Bernardino', 'Santa Clarita', 'Saint Louis', 'Spartanburg', 'San Antonio', 'St. Louis', 'Scranton', 'South Lyon', 'Salt Lake City', 'Sarasota', 'Savannah', 'Salinas', 'Santa Ana', 'South Bend', 'Scottsdale', 'Seaside'}, 'T': {'Tuscaloosa', 'Tacoma', 'Thousand Oaks', 'Topeka', 'Tucson', 'Temecula', 'Tampa', 'Thornton', 'Tallahassee', 'Tyler', 'Tulsa', 'Trenton', 'Tempe', 'Toledo', 'Torrance'}, 'U': {'Utica'}, 'V': {'Vallejo', 'Virginia Beach', 'Vero Beach', 'Vancouver', 'Visalia', 'Victorville'}, 'W': {'Waco', 'Waterbury', 'Warren', 'Washington', 'Worcester', 'Winston', 'Westminster', 'West Valley City', 'West Covina', 'Wilmington', 'Waterloo', 'Wichita', 'Winter Haven'}, 'Y': {'York', 'Yakima', 'Yonkers', 'Youngstown'}}
    expected = [['S', {'San Bernardino', 'Santa Ana', 'Springfield', 'Sioux City', 'South Lyon', 'Saginaw', 'Saint Paul', 'Seattle', 'Saint Louis', 'Scottsdale', 'Santa Rosa', 'Salem', 'Sacramento', 'Salinas', 'Shreveport', 'Salt Lake City', 'Sebastian', 'South Bend', 'St. Petersburg', 'San Diego', 'San Buenaventura', 'San Francisco', 'Sioux Falls', 'Santa Barbara', 'Savannah', 'Saint Petersburg', 'Spokane', 'Santa Clarita', 'San Jose', 'Santa Cruz', 'Santa Maria', 'San Antonio', 'Springdale', 'St. Louis', 'Stockton', 'Sunnyvale', 'Sarasota', 'Sterling Heights', 'Syracuse', 'Spartanburg', 'Stamford', 'Simi Valley', 'Scranton', 'St. Paul', 'Santa Clara', 'Seaside'}], ['C', {'Carrollton', 'Clarke County', 'Chandler', 'Cincinnati', 'Cedar Rapids', 'Cary', 'Cleveland', 'Columbia', 'Corpus Christi', 'Charlotte', 'Clearwater', 'Cambridge', 'Chattanooga', 'Clarksville', 'Chicago', 'College Station', 'Charleston', 'Chula Vista', 'Chesapeake', 'Canton', 'Colorado Springs', 'Costa Mesa', 'Cape Coral', 'Champaign', 'Coral Springs', 'Concord', 'Columbus', 'Corona', 'Cathedral City'}], ['M', {'Murfreesboro', 'Manchester', 'Merced', 'Mission Viejo', 'Montgomery', 'Murrieta', 'Miami', 'McAllen', 'Myrtle Beach', 'McHenry', 'Muskegon', 'Madison', 'Miramar', 'Minneapolis', 'Mobile', 'Milwaukee', 'Marina', 'Medford', 'Mesquite', 'Marysville', 'Monroe', 'Memphis', 'Monterey', 'Modesto', 'Melbourne', 'Macon', 'Moreno Valley', 'Mesa'}], ['B', {'Billings', 'Burbank', 'Bryan', 'Boise City', 'Bonita Springs', 'Brownsville', 'Beaumont', 'Baton Rouge', 'Bellevue', 'Burlington', 'Bremerton', 'Bridgeport', 'Brighton', 'Buffalo', 'Bloomington', 'Bakersfield', 'Berkeley', 'Baltimore', 'Boulder', 'Birmingham', 'Bradenton', 'Bethlehem', 'Boise', 'Boston', 'Bel Air', 'Barnstable'}], ['P', {'Port St. Lucie', 'Paterson', 'Pensacola', 'Port Saint Lucie', 'Plano', 'Port Orange', 'Panama City', 'Pueblo', 'Portland', 'Provo', 'Poughkeepsie', 'Palmdale', 'Pittsburgh', 'Peoria', 'Pomona', 'Port Arthur', 'Punta Gorda', 'Providence', 'Pompano Beach', 'Phoenix', 'Palm Bay', 'Philadelphia', 'Portsmouth', 'Palm Springs', 'Pembroke Pines', 'Pasadena'}], ['A', {'Antioch', 'Atlanta', 'Alexandria', 'Aurora', 'Albuquerque', 'Ann Arbor', 'Apple Valley', 'Athens', 'Abilene', 'Arvada', 'Akron', 'Allentown', 'Atlantic City', 'Arlington', 'Asheville', 'Anaheim', 'Austin', 'Aberdeen', 'Anchorage', 'Augusta', 'Appleton', 'Amarillo', 'Albany'}], ['L', {'Leominster', 'Lexington', 'Las Vegas', 'Louisville', 'Lewisville', 'Little Rock', 'Lowell', 'Lincoln', 'Lubbock', 'Laredo', 'Lakeland', 'Lorain', 'Lake Charles', 'Long Beach', 'Las Cruces', 'Lakewood', 'Lacey', 'Layton', 'Los Angeles', 'Lafayette', 'Lansing', 'Lancaster'}], ['H', {'Hickory', 'Harrisburg', 'Harlingen', 'Henderson', 'Hartford', 'Hialeah', 'Havre de Grace', 'Hayward', 'Huntington Beach', 'Honolulu', 'Hagerstown', 'Hampton', 'Hesperia', 'Houma', 'Houston', 'High Point', 'Huntington', 'Huntsville', 'Howell', 'Hemet', 'Hollywood'}], ['N', {'Nashua', 'New Bedford', 'New Haven', 'Nashville', 'Newark', 'North Charleston', 'New York City', 'Newport News', 'New York', 'Norwich', 'Norfolk', 'Norman', 'Naperville', 'New London', 'North Port', 'Norwalk', 'Normal', 'New Orleans', 'North Las Vegas', 'Naples', 'Newburgh'}], ['F', {'Fort Walton Beach', 'Fayetteville', 'Fairfield', 'Fremont', 'Fargo', 'Fort Smith', 'Frederick', 'Fort Collins', 'Flint', 'Fort Worth', 'Fitchburg', 'Fort Lauderdale', 'Fresno', 'Fullerton', 'Fontana', 'Fort Wayne'}], ['D', {'Daly City', 'Durham', 'Davenport', 'Dayton', 'Downey', 'Daytona Beach', 'Denton', 'Denver', 'Davidson County', 'Deltona', 'Danbury', 'Des Moines', 'Dallas', 'Detroit', 'Duluth'}], ['O', {'Oceanside', 'Orem', 'Ocala', 'Overland Park', 'Ogden', 'Omaha', 'Orange', 'Oakland', 'Oklahoma City', 'Oxnard', 'Odessa', 'Orlando', 'Olathe', 'Ontario', 'Olympia'}], ['R', {'Richland', 'Riverside', 'Rancho Cucamonga', 'Redding', 'Rochester', 'Round Lake Beach', 'Richmond County', 'Reading', 'Rockford', 'Roanoke', 'Richmond', 'Raleigh', 'Racine', 'Reno', 'Roseville'}], ['T', {'Tampa', 'Tucson', 'Tallahassee', 'Tyler', 'Trenton', 'Torrance', 'Tuscaloosa', 'Thornton', 'Temecula', 'Tacoma', 'Thousand Oaks', 'Tulsa', 'Toledo', 'Tempe', 'Topeka'}], ['G', {'Grand Prairie', 'Gulfport-Biloxi', 'Green Bay', 'Glendale', 'Gilbert', 'Gastonia', 'Garden Grove', 'GreenBay', 'Gainesville', 'Grayslake', 'Greenville', 'Garland', 'Grand Rapids', 'Greensboro'}], ['W', {'Waterbury', 'Waterloo', 'Waco', 'Warren', 'Worcester', 'Washington', 'Winston', 'Winter Haven', 'Wichita', 'Wilmington', 'Westminster', 'West Valley City', 'West Covina'}], ['E', {'El Paso', 'Escondido', 'Evansville', 'Elk Grove', 'Erie', 'El Monte', 'Elizabeth', 'Elkhart', 'Eugene'}], ['K', {'Knoxville', 'Kenosha', 'Kissimmee', 'Killeen', 'Kansas City', 'Kaneohe', 'Kalamazoo', 'Kailua', 'Kennewick'}], ['J', {'Joliet', 'Jacksonville', 'Jersey City', 'Jefferson', 'Jackson', 'Johnson City'}], ['V', {'Visalia', 'Victorville', 'Vallejo', 'Virginia Beach', 'Vancouver', 'Vero Beach'}], ['I', {'Irving', 'Independence', 'Irvine', 'Indianapolis', 'Inglewood'}], ['Y', {'Youngstown', 'York', 'Yonkers', 'Yakima'}], ['U', {'Utica'}]]
    '''
    cities = ["Aberdeen", "Abilene", "Akron", "Albany", "Albuquerque", "Alexandria", "Allentown", "Amarillo", "Anaheim", "Anchorage", "Ann Arbor", "Antioch", "Apple Valley", "Appleton", "Arlington", "Arvada", "Asheville", "Athens", "Atlanta", "Atlantic City", "Augusta", "Aurora", "Austin", "Bakersfield", "Baltimore", "Barnstable", "Baton Rouge", "Beaumont", "Bel Air", "Bellevue", "Berkeley", "Bethlehem", "Billings", "Birmingham", "Bloomington", "Boise", "Boise City", "Bonita Springs", "Boston", "Boulder", "Bradenton", "Bremerton", "Bridgeport", "Brighton", "Brownsville", "Bryan", "Buffalo", "Burbank", "Burlington", "Cambridge", "Canton", "Cape Coral", "Carrollton", "Cary", "Cathedral City", "Cedar Rapids", "Champaign", "Chandler", "Charleston", "Charlotte", "Chattanooga", "Chesapeake", "Chicago", "Chula Vista", "Cincinnati", "Clarke County", "Clarksville", "Clearwater", "Cleveland", "College Station", "Colorado Springs", "Columbia", "Columbus", "Concord", "Coral Springs", "Corona", "Corpus Christi", "Costa Mesa", "Dallas", "Daly City", "Danbury", "Davenport", "Davidson County", "Dayton", "Daytona Beach", "Deltona", "Denton", "Denver", "Des Moines", "Detroit", "Downey", "Duluth", "Durham", "El Monte", "El Paso", "Elizabeth", "Elk Grove", "Elkhart", "Erie", "Escondido", "Eugene", "Evansville", "Fairfield", "Fargo", "Fayetteville", "Fitchburg", "Flint", "Fontana", "Fort Collins", "Fort Lauderdale", "Fort Smith", "Fort Walton Beach", "Fort Wayne", "Fort Worth", "Frederick", "Fremont", "Fresno", "Fullerton", "Gainesville", "Garden Grove", "Garland", "Gastonia", "Gilbert", "Glendale", "Grand Prairie", "Grand Rapids", "Grayslake", "Green Bay", "GreenBay", "Greensboro", "Greenville", "Gulfport-Biloxi", "Hagerstown", "Hampton", "Harlingen", "Harrisburg", "Hartford", "Havre de Grace", "Hayward", "Hemet", "Henderson", "Hesperia", "Hialeah", "Hickory", "High Point", "Hollywood", "Honolulu", "Houma", "Houston", "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence", "Indianapolis", "Inglewood", "Irvine", "Irving", "Jackson", "Jacksonville", "Jefferson", "Jersey City", "Johnson City", "Joliet", "Kailua", "Kalamazoo", "Kaneohe", "Kansas City", "Kennewick", "Kenosha", "Killeen", "Kissimmee", "Knoxville", "Lacey", "Lafayette", "Lake Charles", "Lakeland", "Lakewood", "Lancaster", "Lansing", "Laredo", "Las Cruces", "Las Vegas", "Layton", "Leominster", "Lewisville", "Lexington", "Lincoln", "Little Rock", "Long Beach", "Lorain", "Los Angeles", "Louisville", "Lowell", "Lubbock", "Macon", "Madison", "Manchester", "Marina", "Marysville", "McAllen", "McHenry", "Medford", "Melbourne", "Memphis", "Merced", "Mesa", "Mesquite", "Miami", "Milwaukee", "Minneapolis", "Miramar", "Mission Viejo", "Mobile", "Modesto", "Monroe", "Monterey", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta", "Muskegon", "Myrtle Beach", "Naperville", "Naples", "Nashua", "Nashville", "New Bedford", "New Haven", "New London", "New Orleans", "New York", "New York City", "Newark", "Newburgh", "Newport News", "Norfolk", "Normal", "Norman", "North Charleston", "North Las Vegas", "North Port", "Norwalk", "Norwich", "Oakland", "Ocala", "Oceanside", "Odessa", "Ogden", "Oklahoma City", "Olathe", "Olympia", "Omaha", "Ontario", "Orange", "Orem", "Orlando", "Overland Park", "Oxnard", "Palm Bay", "Palm Springs", "Palmdale", "Panama City", "Pasadena", "Paterson", "Pembroke Pines", "Pensacola", "Peoria", "Philadelphia", "Phoenix", "Pittsburgh", "Plano", "Pomona", "Pompano Beach", "Port Arthur", "Port Orange", "Port Saint Lucie", "Port St. Lucie", "Portland", "Portsmouth", "Poughkeepsie", "Providence", "Provo", "Pueblo", "Punta Gorda", "Racine", "Raleigh", "Rancho Cucamonga", "Reading", "Redding", "Reno", "Richland", "Richmond", "Richmond County", "Riverside", "Roanoke", "Rochester", "Rockford", "Roseville", "Round Lake Beach", "Sacramento", "Saginaw", "Saint Louis", "Saint Paul", "Saint Petersburg", "Salem", "Salinas", "Salt Lake City", "San Antonio", "San Bernardino", "San Buenaventura", "San Diego", "San Francisco", "San Jose", "Santa Ana", "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Maria", "Santa Rosa", "Sarasota", "Savannah", "Scottsdale", "Scranton", "Seaside", "Seattle", "Sebastian", "Shreveport", "Simi Valley", "Sioux City", "Sioux Falls", "South Bend", "South Lyon", "Spartanburg", "Spokane", "Springdale", "Springfield", "St. Louis", "St. Paul", "St. Petersburg", "Stamford", "Sterling Heights", "Stockton", "Sunnyvale", "Syracuse", "Tacoma", "Tallahassee", "Tampa", "Temecula", "Tempe", "Thornton", "Thousand Oaks", "Toledo", "Topeka", "Torrance", "Trenton", "Tucson", "Tulsa", "Tuscaloosa", "Tyler", "Utica", "Vallejo", "Vancouver", "Vero Beach", "Victorville", "Virginia Beach", "Visalia", "Waco", "Warren", "Washington", "Waterbury", "Waterloo", "West Covina", "West Valley City", "Westminster", "Wichita", "Wilmington", "Winston", "Winter Haven", "Worcester", "Yakima", "Yonkers", "York", "Youngstown"]
    dict_in = {char: {city for city in cities if city.startswith(char)} for char in 'ABCDEFGHIJKLMNOPRSTUVWY'}
    expected = [['S', {'San Bernardino', 'Santa Ana', 'Springfield', 'Sioux City', 'South Lyon', 'Saginaw', 'Saint Paul', 'Seattle', 'Saint Louis', 'Scottsdale', 'Santa Rosa', 'Salem', 'Sacramento', 'Salinas', 'Shreveport', 'Salt Lake City', 'Sebastian', 'South Bend', 'St. Petersburg', 'San Diego', 'San Buenaventura', 'San Francisco', 'Sioux Falls', 'Santa Barbara', 'Savannah', 'Saint Petersburg', 'Spokane', 'Santa Clarita', 'San Jose', 'Santa Cruz', 'Santa Maria', 'San Antonio', 'Springdale', 'St. Louis', 'Stockton', 'Sunnyvale', 'Sarasota', 'Sterling Heights', 'Syracuse', 'Spartanburg', 'Stamford', 'Simi Valley', 'Scranton', 'St. Paul', 'Santa Clara', 'Seaside'}], ['C', {'Carrollton', 'Clarke County', 'Chandler', 'Cincinnati', 'Cedar Rapids', 'Cary', 'Cleveland', 'Columbia', 'Corpus Christi', 'Charlotte', 'Clearwater', 'Cambridge', 'Chattanooga', 'Clarksville', 'Chicago', 'College Station', 'Charleston', 'Chula Vista', 'Chesapeake', 'Canton', 'Colorado Springs', 'Costa Mesa', 'Cape Coral', 'Champaign', 'Coral Springs', 'Concord', 'Columbus', 'Corona', 'Cathedral City'}], ['M', {'Murfreesboro', 'Manchester', 'Merced', 'Mission Viejo', 'Montgomery', 'Murrieta', 'Miami', 'McAllen', 'Myrtle Beach', 'McHenry', 'Muskegon', 'Madison', 'Miramar', 'Minneapolis', 'Mobile', 'Milwaukee', 'Marina', 'Medford', 'Mesquite', 'Marysville', 'Monroe', 'Memphis', 'Monterey', 'Modesto', 'Melbourne', 'Macon', 'Moreno Valley', 'Mesa'}], ['B', {'Billings', 'Burbank', 'Bryan', 'Boise City', 'Bonita Springs', 'Brownsville', 'Beaumont', 'Baton Rouge', 'Bellevue', 'Burlington', 'Bremerton', 'Bridgeport', 'Brighton', 'Buffalo', 'Bloomington', 'Bakersfield', 'Berkeley', 'Baltimore', 'Boulder', 'Birmingham', 'Bradenton', 'Bethlehem', 'Boise', 'Boston', 'Bel Air', 'Barnstable'}], ['P', {'Port St. Lucie', 'Paterson', 'Pensacola', 'Port Saint Lucie', 'Plano', 'Port Orange', 'Panama City', 'Pueblo', 'Portland', 'Provo', 'Poughkeepsie', 'Palmdale', 'Pittsburgh', 'Peoria', 'Pomona', 'Port Arthur', 'Punta Gorda', 'Providence', 'Pompano Beach', 'Phoenix', 'Palm Bay', 'Philadelphia', 'Portsmouth', 'Palm Springs', 'Pembroke Pines', 'Pasadena'}], ['A', {'Antioch', 'Atlanta', 'Alexandria', 'Aurora', 'Albuquerque', 'Ann Arbor', 'Apple Valley', 'Athens', 'Abilene', 'Arvada', 'Akron', 'Allentown', 'Atlantic City', 'Arlington', 'Asheville', 'Anaheim', 'Austin', 'Aberdeen', 'Anchorage', 'Augusta', 'Appleton', 'Amarillo', 'Albany'}], ['L', {'Leominster', 'Lexington', 'Las Vegas', 'Louisville', 'Lewisville', 'Little Rock', 'Lowell', 'Lincoln', 'Lubbock', 'Laredo', 'Lakeland', 'Lorain', 'Lake Charles', 'Long Beach', 'Las Cruces', 'Lakewood', 'Lacey', 'Layton', 'Los Angeles', 'Lafayette', 'Lansing', 'Lancaster'}], ['H', {'Hickory', 'Harrisburg', 'Harlingen', 'Henderson', 'Hartford', 'Hialeah', 'Havre de Grace', 'Hayward', 'Huntington Beach', 'Honolulu', 'Hagerstown', 'Hampton', 'Hesperia', 'Houma', 'Houston', 'High Point', 'Huntington', 'Huntsville', 'Howell', 'Hemet', 'Hollywood'}], ['N', {'Nashua', 'New Bedford', 'New Haven', 'Nashville', 'Newark', 'North Charleston', 'New York City', 'Newport News', 'New York', 'Norwich', 'Norfolk', 'Norman', 'Naperville', 'New London', 'North Port', 'Norwalk', 'Normal', 'New Orleans', 'North Las Vegas', 'Naples', 'Newburgh'}], ['F', {'Fort Walton Beach', 'Fayetteville', 'Fairfield', 'Fremont', 'Fargo', 'Fort Smith', 'Frederick', 'Fort Collins', 'Flint', 'Fort Worth', 'Fitchburg', 'Fort Lauderdale', 'Fresno', 'Fullerton', 'Fontana', 'Fort Wayne'}], ['D', {'Daly City', 'Durham', 'Davenport', 'Dayton', 'Downey', 'Daytona Beach', 'Denton', 'Denver', 'Davidson County', 'Deltona', 'Danbury', 'Des Moines', 'Dallas', 'Detroit', 'Duluth'}], ['O', {'Oceanside', 'Orem', 'Ocala', 'Overland Park', 'Ogden', 'Omaha', 'Orange', 'Oakland', 'Oklahoma City', 'Oxnard', 'Odessa', 'Orlando', 'Olathe', 'Ontario', 'Olympia'}], ['R', {'Richland', 'Riverside', 'Rancho Cucamonga', 'Redding', 'Rochester', 'Round Lake Beach', 'Richmond County', 'Reading', 'Rockford', 'Roanoke', 'Richmond', 'Raleigh', 'Racine', 'Reno', 'Roseville'}], ['T', {'Tampa', 'Tucson', 'Tallahassee', 'Tyler', 'Trenton', 'Torrance', 'Tuscaloosa', 'Thornton', 'Temecula', 'Tacoma', 'Thousand Oaks', 'Tulsa', 'Toledo', 'Tempe', 'Topeka'}], ['G', {'Grand Prairie', 'Gulfport-Biloxi', 'Green Bay', 'Glendale', 'Gilbert', 'Gastonia', 'Garden Grove', 'GreenBay', 'Gainesville', 'Grayslake', 'Greenville', 'Garland', 'Grand Rapids', 'Greensboro'}], ['W', {'Waterbury', 'Waterloo', 'Waco', 'Warren', 'Worcester', 'Washington', 'Winston', 'Winter Haven', 'Wichita', 'Wilmington', 'Westminster', 'West Valley City', 'West Covina'}], ['E', {'El Paso', 'Escondido', 'Evansville', 'Elk Grove', 'Erie', 'El Monte', 'Elizabeth', 'Elkhart', 'Eugene'}], ['K', {'Knoxville', 'Kenosha', 'Kissimmee', 'Killeen', 'Kansas City', 'Kaneohe', 'Kalamazoo', 'Kailua', 'Kennewick'}], ['J', {'Joliet', 'Jacksonville', 'Jersey City', 'Jefferson', 'Jackson', 'Johnson City'}], ['V', {'Visalia', 'Victorville', 'Vallejo', 'Virginia Beach', 'Vancouver', 'Vero Beach'}], ['I', {'Irving', 'Independence', 'Irvine', 'Indianapolis', 'Inglewood'}], ['Y', {'Youngstown', 'York', 'Yonkers', 'Yakima'}], ['U', {'Utica'}]]
    return do_func4_tests(dict_in, expected)

def test_func4_4(run=True):
    '''
    dict_in = {'hp': {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price':30000},
            'lenovo': {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price':40000},
            'dell': {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price':200}}
    expected = [['dell', {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price': 200}], ['hp', {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price': 30000}], ['lenovo', {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price': 40000}]]
    '''
    dict_in = {'hp': {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price':30000},
            'lenovo': {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price':40000},
            'dell': {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price':200}}
    expected = [['dell', {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price': 200}], ['hp', {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price': 30000}], ['lenovo', {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price': 40000}]]
    return do_func4_tests(dict_in, expected)

def do_func5_tests(list_a, list_b, expected):
    res = program.func5(list_a, list_b)
    if res == None:
        raise testlib.NotImplemented()
    testlib.check_val(res, expected)
    return 1.5


def test_func5_1(run=True):
    '''
    list_A = ["flash", "ColA", "USED", "lazer"]
    list_B = ["Rabit", "HELIOS", "trick", "suPER"]
    expected = ['a', 'lo', '', 'er']
    '''
    list_A = ["flash", "ColA", "USED", "lazer"]
    list_B = ["Rabit", "HELIOS", "trick", "suPER"]
    expected = ['a', 'lo', '', 'er']
    return do_func5_tests(list_A, list_B, expected)

def test_func5_2(run=True):
    '''
    list_A = ["RAM", "rom", "JaM", "leAP", "star"]
    list_B = ["", "aBcDeFgH", "aBcDeFgH", "aBcDeFgH", "aBcDeFgH"]
    expected = ['', '', 'a', 'ae', 'a']
    '''
    list_A = ["RAM", "rom", "JaM", "leAP", "star"]
    list_B = ["", "aBcDeFgH", "aBcDeFgH", "aBcDeFgH", "aBcDeFgH"]
    expected = ['', '', 'a', 'ae', 'a']
    return do_func5_tests(list_A, list_B, expected)

def test_func5_3(run=True):
    '''
    list_A = ["abcdefghijklmnopqrstuwxyz", "abcdefghijklmnopqrstuwxyz"]
    list_B = ["ZYXWUTSRQPONMLKJIHGFEDCBA", "zyxwutsrqponmlkjihgfedcba"]
    expected = ['abcdefghijklmnopqrstuwxyz', 'abcdefghijklmnopqrstuwxyz']
    '''
    list_A = ["abcdefghijklmnopqrstuwxyz", "abcdefghijklmnopqrstuwxyz"]
    list_B = ["ZYXWUTSRQPONMLKJIHGFEDCBA", "zyxwutsrqponmlkjihgfedcba"]
    expected = ['abcdefghijklmnopqrstuwxyz', 'abcdefghijklmnopqrstuwxyz']
    return do_func5_tests(list_A, list_B, expected)

def test_func5_4(run=True):
    '''
    list_A = ["catode", "dermatoglyphics", "uncopyrightable"]
    list_B = ["ZYXWUTSRQPONMLKJIHGFEDCBA", "zyxwutsrqponmlkjihgfedcba", "zyxwutsrqponmlkjihgfedcba"]
    expected = ['acdeot', 'acdeghilmoprsty', 'abceghilnoprtuy']
    '''
    list_A = ["catode", "dermatoglyphics", "uncopyrightable"]
    list_B = ["ZYXWUTSRQPONMLKJIHGFEDCBA", "zyxwutsrqponmlkjihgfedcba", "zyxwutsrqponmlkjihgfedcba"]
    expected = ['acdeot', 'acdeghilmoprsty', 'abceghilnoprtuy']
    return do_func5_tests(list_A, list_B, expected)

def do_func6_tests(dict1, expected):
    res = program.func6(dict1)
    if res == None:
        raise testlib.NotImplemented()
    testlib.check_val(res, expected)
    return 1.5

def test_func6_1(run=True):
    '''
    dict1 = {"a" : [3, 2, 2], "b" : [4, 2, 3], "c" : [-4, 2, 2]}
    expected =  "b"
    '''
    dict1 = {"a" : [3, 2, 2], "b" : [4, 2, 3], "c" : [-4, 2, 2]}
    expected =  "b"
    return do_func6_tests(dict1, expected)

def test_func6_2(run=True):
    '''
    dict1 = {"a" : [3, 2, 2, -1, -1], "b" : [4, 2, 3, -4], "c" : [-4, 2, 2]}
    expected =  "a"
    '''
    dict1 = {"a" : [3, 2, 2, -1, -1], "b" : [4, 2, 3, -4], "c" : [-4, 2, 2]}
    expected =  "a"
    return do_func6_tests(dict1, expected)

def test_func6_3(run=True):
    '''
    dict1 = {"C" : [1, 1, 1, 1, 1, 1], "b" : [6]}
    expected =  "C"
    '''
    dict1 = {"C" : [1, 1, 1, 1, 1, 1], "b" : [6]}
    expected =  "C"
    return do_func6_tests(dict1, expected)

def test_func6_4(run=True):
    '''
    dict1 = {"C" : [0], "B" : [1], "A" : [1, -1, 1, -1, 1, -1, 1, -1, 1], "a" : [-1]}
    expected =  "A"
    '''
    dict1 = {"C" : [0], "B" : [1], "A" : [1, -1, 1, -1, 1, -1, 1, -1, 1], "a" : [-1]}
    expected =  "A"
    return do_func6_tests(dict1, expected)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_func6_1, test_func6_2, test_func6_3, test_func6_4,
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
