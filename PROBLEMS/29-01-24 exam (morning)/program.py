#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER

To pass the exam you must:
    - solve at least 3 exercises of type func AND;
    - solve at least 1 exercise of type ex (recursive problem) AND;
    - obtain a score greater than or equal to 18

The final grade is the sum of the scores of the solved problems.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""

name = "Leila"
surname = "Zanoni"
student_id = "2033176"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 points
Define the function func1(int_list, n) that takes as its
input a list of integers int_list and an integer n. The
function returns a dictionary in which the values are the
integers of the int_list that have a number of repetitions
greater than or equal to n and the corresponding keys are
the integers of the int_list.

Example:
    func1([4, 4, 10, 4, 2, 1, 2], 2) should return the dictionary
    {4: 3, 2: 2}
'''
def func1(int_list, n):
    ## Scrivi qui il tuo codice
    d = {v : int_list.count(v) for v in int_list if int_list.count(v) >= n}
    return d


l1 = [4, 4, 10, 4, 2, 1, 2]
#print(func1(l1, 2))


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points

Si definisca una funzione func2(dict1, a, b) che prende in ingresso
un dizionario che ha chiavi e valori di tipo stringa e due stringhe di
lunghezza uno. La funzione deve restituire una lista composta dalle
sole stringhe del dizionario corrispondenti a una chiave che inizia
con un carattere compreso fra i caratteri a e b, ignorando sempre
la distinzione fra maiuscole e minuscole.
La lista ritornata deve essere ordinata per numero di caratteri decrescente
e, in caso di parità, in ordine alfabetico.
Esempio:
    func2({'Car':'GoOd', 'floor':'bAd', 'Wild':'EXCELLENT', 'air':'Bad', 'cocoon':'greaT'}, 'c', 'G')
    deve restituire la lista ['greaT', 'GoOd', 'bAd']
'''

def func2(dict1, a, b):
    ## Write your code here
    lista = []
    for k, v in dict1.items():
        if k[0].lower() >= a.lower() and k[0].lower() <= b.lower():
            lista.append(dict1[k])
    return sorted(lista, key = lambda x : (-len(x), x))

    
    
        
    

#print(func2({'Car':'GoOd', 'floor':'bAd', 'Wild':'EXCELLENT', 'air':'Bad', 'cocoon':'greaT'}, 'c', 'G'))

# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 2 points

Define a function func3(str1, str2) that takes as input two strings of
the same length and constructs a new string str3 obtained by
alternating the characters of str1 with those of inverted str2.  In
addition, the characters of str1 must change from uppercase to
lowercase, and vice versa.  The function returns the string thus
constructed.

Example:
    func3('gLIde', 'yoWLS')) must return the string 'GSlLiWDoEy'
'''

def func3(str1, str2):
    ## Write your code here
    l = []
    for word in str1:
        for char in word:
            if char.islower():
                char = char.upper()
                l.append(char)
            else:
                char = char.lower()
                l.append(char)
    str1_new = ''.join(l)
    res = []
    for s1, s2 in zip(str1_new, str2[::-1]):
        res.append(s1 + s2)
    
    return "".join(res)
        

#print(func3('gLIde', 'yoWLS'))#GSlLiWDoEy
# print(func3('StaIrcAses', 'granulates'))#ssTeAtiaRlCuanSaErSg
#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Define a function func4(input_filename, output_filename, expr) that
takes as input two strings representing two filenames and a
third string expr.
The file given by input_filename contains a series of words separated by spaces, tabs, or carriage returns.
The function must locate within the contents of input_filename all lines that contain a word equal to 'expr', ignoring the distinction between upper and lower case and return them in the same order within a new file named 'output_filename'.
Finally, the function must return a dictionary in which:
    - the keys are the numbers of the rows in the identified input_filename file
    - the values are triples containing respectively:
        - the number of total characters in the row
        - the number of words in the row
        - the total number of spaces, tabs, and carriage return characters of the row

Note: rows begin with the number 1.
Example
If there are the following three lines in the file 'func4_test1.txt'
cat bat    rat
Condor baT
Cat cAr CAR
the function func4('func4_test1.txt', 'func4_out1.txt', 'CAt') should write
in the file 'func4_out1.txt' the following 2 lines:
cat bat    rat
Cat cAr CAR

and return the dictionary {1: (15, 3, 6), 3: (11, 3, 2)}.
"""

def func4(input_filename, output_filename, expr):
    ## Write your code here

    D = {}
    
    with open(input_filename) as fin:
        with open(output_filename, 'w') as fout:
            for i, riga in enumerate(fin, 1):
                parole = riga.split()
                if any(parola.lower() == expr.lower() for parola in parole):
                    D[i] = len(riga), len(parole), len(riga) - len("".join(parole))
                    fout.write(riga)
                    
    return D



print(func4('func4/func4_test1.txt', 'func4/func4_out1.txt', 'CAt'))

# %% ----------------------------------- FUNC5 ------------------------- #
''' func5: 8 points

Write a function func5 that takes as input an RGB image.  The function
counts and returns the number of non-black "isolated" pixels, that is,
pixels preceeded and followed by black pixels (i.e., given a pixel P,
there is a black pixel preceeding and following P).  If a pixel P is
on the left or right border of the image (i.e., it is on the first or
last column), then we consider it "isolated" only if the following or
preceeding pixel is black.  Additionally, the function saves an RGB
image with the same width and height of the input image and in which
only the isolated pixels are copied.

For example, if B is a black pixel and * is a non-black pixel, given
the image:

BB*BBBB*
*BBB*BBB
B*BB**B*
BBBBBB*B
*BBB**BB

The function returns 8 and saves the image:

BB*BBBB*
*BBB*BBB
B*BBBBB*
BBBBBB*B
*BBBBBBB



'''
import images


def func5(input_file_name, output_file_name):
    # your code goes here
    img = images.load(input_file_name)
    b = (0, 0, 0)
    W = len(img[0])
    H = len(img)
    res = [[(0, 0, 0)] * W for _ in range(H)]
    count = 0
    for y, riga in enumerate(img):
        for x, pixel in enumerate(riga):
            if pixel != b and ((x == 0) or (riga[x-1] == b)) and ((x == W - 1) or (riga[x +1] == b)):
                count += 1
                res[y][x] = pixel

                
    images.save(res, output_file_name)
    return count


imagefile = 'func5/img1_in.png'
output_imagefile = 'func5/img1_out.png'
print(func5(imagefile, output_imagefile))
                

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points

Define the function ex1(dirin), recursive or using recursive functions
or methods, having as an argument a string indicating the path to an
existing directory.  The function will examine dirin and all its
subdirectories (at any level), and count the number of numeric
characters found in files with the extension '.txt' found in any
directory.

The function returns a list of strings representing the relative paths
to the dirin directory of the files in which the numeric characters
were found. The list of file paths is sorted in descending order
according to the number of numeric characters found in the various
files. If two or more files have the same number of numeric
characters, the ascending order of file depth within the dirin
directory should be used. In case of a tie, alphabetical order should
be used.

A '.txt' file that does not contain numeric characters is not included
in the returned list.

NOTICE 1: We recommend using the os.listdir, os.path.isfile and
  os.path.isdir functions and NOT the os.join function in Windows. Use
  concatenation between strings with the '/' character.

NOTICE 2: It is forbidden to use the os.walk function.

For example, the function ex1('ex1/A') must return the list
  ['ex1/A/B/3odd74B.txt', 'ex1/A/C/e3dd7Ag22.txt',
  'ex1/A/3cmi4G3ev.txt', 'ex1/A/gkfep28.txt', 'ex1/A/C/n3ks22.txt']
"""

import os

def ex1(dirin):
    # your code goes here
    fnames = _ex1(dirin)
    return sorted(fnames.keys(), key = lambda x :(-fnames[x], x.count('/'), x))

def _ex1(dirin):
    fnames = {}
    for f in os.listdir(dirin):
        full = dirin + '/' + f
        #print(full)
        if os.path.isfile(full) and f.endswith('.txt'):
            with open(full) as fin:
                count = sum([1 for c in fin.read() if c.isdigit()])
                if count:
                    fnames[full] = count
        elif os.path.isdir(full):
              fnames.update(_ex1(full))
                
    return fnames


print(ex1('ex1/A'))
# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 points

Define the function ex2(root), recursive or using a recursive method,
which takes as input the root node that is the root of a binary tree
consisting of nodes of type BinaryTree, as defined in the tree.py
module.  The function must return the number of nodes in the tree that
have a value greater than the sum of the nodes in its subtrees.

Example:

        root      
    ______25______ 
   |             |  
   8__        ___2___ 
      |      |       |  
      3      9       1  

      expected = 2, namely the nodes 25 and 8


Other example:

              root       
          ______2______  
         |             | 
      __ 7__        ___15___  
     |      |      |       | 
    _4_     3_    _0_     _5_  
   |   |      |  |   |   |   | 
   2   -1     1  8   3   2  -9 

       expected = 4, namely nodes 4, 3, 15 and 5


"""
import tree

def ex2(root):
    ## Scrivi qui il tuo codice
    pass
    return conta(root)

def conta(radice):
    if radice is None:
        return 0
    if (radice.left or radice.right) and radice.value > somma(radice.left) + somma(radice.right):
        return 1 + conta(radice.left)+conta(radice.right)
    return conta(radice.left)+conta(radice.right)

def somma(radice):
    if radice is None:
        return 0
    return radice.value + somma(radice.left) + somma(radice.right)



root = tree.BinaryTree.fromList([25, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
print(ex2(root))
# root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [15, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [-9, None, None]]]])
# print(ex2(root))
# root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
# print(ex2(root))

###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenii puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
