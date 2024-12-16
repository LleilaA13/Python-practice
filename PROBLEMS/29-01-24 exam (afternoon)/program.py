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
name       = "Leila"
surname    = "Zanoni"
student_id = "2033176"

#########################################


# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 points

Write the function func1(a_list) that is provided a list of non-empty
lists as parameter. The function modifies the given list in-place
by replacing each sublist by the product of the sublist items.
Additionally, the function returns the number of sublists.

For example, if L = [[1, 2, 3], [-1, 2, 3], [2, 2, -2]], after calling
func1(L) the value of L will be [6, -6, -8]
(as 1 * 2 * 3 = 6, -1 * 2 * 3 = -6 and 2 * 2 * -2 = -8)
and the function returns 3.
'''

def func1(a_list):
    # your code goes here
    res = len(a_list)
    l = []

    for lista in a_list:
        p = 1
        for x in lista:
            p *= x
        l.append(p)
            
    a_list[:] = l
    return res
            
#print(func1([[1, 2, 3], [-1, 2, 3], [2, 2, -2]]))

# %%  ---- FUNC2 ----
''' func2: 2 marks

Write a function func2(a_dictionary) that takes a dictionary as
parameter, in which:
- the keys are single alphabetical characters
- the items are lists of integers

The function returns the character for which the corresponding
list of integers sums to the highest value. If multiple characters
sum to the same maximum value, the first one in alphabetical order
is returned.

For example, func2({"a" : [3, 2, 2], "b" : [4, 2, 3], "c" : [-4, 2, 2]})
returns "b", as the list [4, 2, 3] sums to the highest value among all
the lists in the dictionary.
'''

def func2(a_dictionary):
    # your code goes here
    pass

# %%  ---- FUNC3 ----
'''  func3: 2 marks

Write a function func3(list_A, list_B) that takes two lists with the
same number of strings as input.
The function returns a third list of strings.
Each string in position i in the result list
contains the characters in common between the two strings
in position i in list_A and list_B, all in lower case,
in alphabetical order, and ignoring the case they had
in the strings in list_A and list_B.
The characters in common between the two strings in the two
lists can be in whatever position inside the strings.
The strings in list_A and list_B cannot contain repeating
characters, whatever their case.

For example, if list_A = ["aBd", "baC", "cAb"] and
list_B = ["bcE", "dca", "eDf"], the function returns:
["b", "ac", ""]

'''

def func3(list_A, list_B):
    # your code goes here
    pass

# %%  ---- FUNC4 ----
''' func4: 6 marks

Write a function func4(input_txt, output_txt) that takes two file
names as parameters. The function reads the text file input_txt
and returns the number of words longer than 3 characters contained
in the file. The words can be separated by any number of spaces
or newlines.

The function writes the text file output_txt that contains
the words counted by the function in reversed order, one per line.

For example, if input_txt contains the following text:

The          quick
           brown fox            jumps
    over
           
                 the     lazy             dog

the function returns 5, as 5 words are longer than 3
characters (quick, brown, jumps, over, lazy) and writes the file:

lazy
over
jumps
brown
quick

'''

def func4(input_txt, output_txt):
    # your code goes here
    pass


# %%  ---- FUNC5 ---- %% #
''' func5: 8 marks

Define a function func5(imagefile, output_imagefile) that takes
as input two strings representing two PNG image file names.  The image
in the 'imagefile' file contains only white horizontal segments on a
black background and has a maximum width of 256 pixels.  Each line has
at most one white segment.

The function must create a new image with the same size and segments
as the input image, in which the color of the segments with minimum
and maximum length is changed.

The color to be used (R, G, B) is defined as follows:
    - the R channel corresponds to the length of the segment with
      minimum length
    - the B channel corresponds to the length of the segment with
      maximum length
    - the G channel corresponds to the value that is obtained from the
      average value of the lengths of all the segments (use integer
      division).

The image thus obtained should be saved in PNG format in the file with the
output_imagefile path.
The function returns the number of colored segments in the output image.

'''

import images

def func5(imagefile, output_imagefile):
    # your code goes here
    pass

# for i in range(1, 5):
#     print('func', func5(f'func5/func5_test{i}.png', f'func5/func5_out{i}.png'))
    
# %% ----------------------------------- EX.1 ----------------------------------- #
'''
Ex1: 6 marks

Write a function ex1(target_folder), recursive or using at least one recursive function,
that is provided as input the path of folder target_folder. The function
recursively scans target_folder and all its subfolders, and
returns a list of pairs (path, count), in which:
- path is the full path of one of the subfolders of target_folder
  (nested at any level>=0 inside target_folder; target_folder
  can be considered as a subfolder of itself, for which level=0);
- count is the number of text files contained in the subfolder
  (text files are files whose name ends in ".txt").

The returned list is ordered based on the files counter value,
in decreasing order; if two or more folders contain the same
number of files, they are sorted in alphabetical order.

The only 2 functions that can be imported in your solution are:
os.listdir and os.path.isdir

For example, if the folder structure is:

A
|-B
| |-C
| | |-c1.txt
| | |-c2.txt
| |
| |-b1.txt
| |-b2.txt
| |-b3.txt
|
|-D
| |-d1.txt
| |-d2.txt
|
|-E
| |-e1.txt
|
|-a1.txt
|-a2.txt
|-a3.txt

the function returns the list:
[("A", 3), ("A/B", 3), ("A/B/C", 2), ("A/D", 2), ("A/E", 1)]

'''

from  os import listdir
from os.path import isdir

def ex1(target_folder):
    # your code goes here
    pass



# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: 6 marks

Write a function ex2(T) that is provided as parameter the root T of a binary tree,
stored as a BinaryTree object defined in the tree.py file.
The function is recursive or uses at least one recursive function.
The values in the tree are integers.
The function returns the triple (L, S, D), where:
- L is the number of leaves;
- S is the number of nodes with a single child node;
- D is the number of nodes with two child nodes.

For example, if T is:

                T       
          ______2______  
         |             | 
      __ 7__        ___15___  
     |      |      |       | 
    _4      3     _0_      5_  
   |             |   |       | 
   2             8   3      -9 

The function returns: (5, 2, 4)
'''

from tree import BinaryTree    
    
def ex2(T):
    # your code goes here
    pass

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*' * 50)
    print('ITA\nEseguire grade.py per effettuare il debug con grader incorporato.')
    print('Altrimenti, inserire codice qui per verificare le funzioni con test propri')
    print('*' * 50)
    print('ENG\nRun grade.py to debug the code with the automatic grader.')
    print('Alternatively, insert here the code to check the functions with custom test inputs')
    print('*' * 50)
    
