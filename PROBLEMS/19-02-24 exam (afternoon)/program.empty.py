#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Steps to do FIRST:
 1) save this file as program.py
 2) assign the variables below with your
    FIRST NAME, LAST NAME, STUDENT ID (Sapienza matriculation number)

To pass the exam it is necessary to:
    - !!!fill in your personal information in the variables below!!!
    - AND solve at least 1 ex-type exercise (recursive problem)
    - AND solve at least 3 func-type exercises
    - AND obtain a score greater than or equal to 18

The final score is the sum of the scores of the solved problems.
"""

name       = 'NAME'
surname    = 'SURNAME'
student_id = 'STUDENT_ID'    # your Sapienza registration number

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################

#%% ---------------------------- FUNC 1 ---------------------------- #

'''
Func 1: 2 points
Let us define the function func1(lists) that takes as input a list
of lists. Each internal list contains integers. The function
returns a list that contains all the integers that are present
in all the inner lists. The integers in the output list are
ordered from largest to smallest.

If lists = [[4, 4, 10, 4, 1], [4, 2, 1], [1, 4]]

then the function returns [4, 1] since 4 and 1 are in all of the
lists; instead 2 and 10 are not included.
Assume that lists is never empty.
'''

def func1(lists):
    # write your code here
    pass



#%% ---------------------------- FUNC 2 ---------------------------- #

'''
Func 2: 2 points

Define the func2(text) function that receives as an argument:
- text: a text string
and which returns the value of the largest number (sequence of digits) found in the text.

Example:
text = 'under the bench 1234The go3212At SinGs 4S5oV6e7r8t HE BeNcH tHe gOaT dIES'
expected = 3212
'''

def func2(text):
    pass

# text = 'under the bench 1234The go3212At SinGs 4S5oV6e7r8t HE BeNcH tHe gOaT dIES'
# print(func2(text))

# ---------------------------- FUNC 3 ---------------------------- #
'''
Func 3: 4 points
Define the function func3(textfile_in, textfile_out) that receives as an argument:
- textfile_in: the path to a text file to read
- textfile_out: the path to a text file to create

The function must read the textfile_in file and write to the textfile_out file.
The textfile_in file contains a series of lines of text, each of which
contains a sequence of integers separated by commas, spaces, or \t.

The function must write one line to the textfile_out file for each line of textfile_in
containing the difference between the product of even numbers and the product of odd numbers.
It must also return the pair (sum_even, sum_odd) where sum_even and sum_odd
are the sum of even and odd numbers respectively.

The lines must be sorted in the opposite order to the reading order of the textfile_in file.

Example: if the file contains lines
     1, 2, 17, 22
     6, -38, 71, 50, 3
     12, -8, 190, 0, 1

The output file must contain lines
     -1
     -11613
     27

and the function must return the pair (sum_even, sum_odd) = (236, 93)
'''

def func3(textfile_in, textfile_out):
    pass

# print(func3('func3/in_1.txt', 'func3/out_1.txt'))

#%% ---------------------------- FUNC 4 ---------------------------- #

'''
Func 4: 4 points
Define the func5(filein) function that receives as an argument
- filein: a text file containing a square matrix of NxN integers
   separated by spaces
and which returns the difference between the product of the elements 
belonging to either one of of the two diagonals
and the sum of the elements that are not on the diagonals.
NOTICE: If the matrix has odd size the centre element must be used only once.

Example:
if the file filein contains the array
17 23 98
12 51 -30
0 40 17

The two diagonals contain the elements 17, 51, 17 and 98, 51, 0 respectively.
The elements that are not on the diagonals are 23, 12, -30 and 40.
So the function must return (17*51*17*98*51*0) - (23+12-30+40) = -45
'''
def func4(filein):
    pass

#print(func4('func4/in_1.txt'))

#%% ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 6 points
Define the function func5(png_input) that receives as an argument:
- png_input: the path to a PNG image

The png_input file contains an image with a black background, containing stars,
i.e. crosses measuring 3x3 pixels diagonally in any colour.
Example:
.x.x....
..xo.o..
.x.xo...
...o.o..
........

In the example there is a star of color 'x' and one of color 'o'.

Assume that any two stars of the same color are separated by at least one pixel
and therefore they do not touch each other either horizontally/vertically or diagonally.
Assume that the pixels in the image are only stars or a black background.

The function must count the number of stars present, for each color
and return a dictionary that has the colors of the stars in the image as keys
and the number of stars of that color as value.

Example:
If the image is 'func5/in_2.png' the result will be the dictionary
{(150, 200, 150): 3, (200, 150, 125): 4, (125, 175, 200): 2,
(125, 100, 125): 3, (125, 175, 125): 4, (200, 100, 150): 2}
'''

import images


def func5(png_input):
    pass

# print(func5('func5/in_2.png'))


# ---------------------------- EX 1 ---------------------------- #

'''
Recursive Exercise 1 (6+2 points):

Part 1: 6 points - recursive
Define the function es1(root), recursive or that uses recursive functions,
which receives as input:
- the root 'root' of an n-ary tree defined by nary_tree.NaryTree nodes
Assume that the tree has at least 2 nodes and that the maximmum and the minimum values are unique and different.

The function must find the two minimum and maximum value nodes and return
the pair of paths that lead from the root to these two nodes.
- path from root to minimum node
- path from root to maximum node

Example:
    root:                        
                              *-7*                           |
                          /           \                      |
                       *1*                2                  |
                   */*    *|*        /    |    \             |
                 *-10*    *-3*     -8    -10    -5           | 
                /  *\*     *|*      |      |                 |
               6   *-22*   *9*      7     -9                 | 

The minimum value is -22, the maximum value is 9.
The paths to return are: ([-7, 1, -10, -22], [-7, 1, -3, 9]) (highlighted with asterisks)

ATTENTION: define the recursive function at the external level,
that is, with the keyword 'def' placed at the beginning of the line.

TIP: Break the problem into small functions

Part 2: 2 points
The function, once the two paths leading to the nodes with minimum and maximum values have been found,
must also calculate the shortest path that connects them, i.e. the list of values of the nodes that
start with the minimum value and reach the maximum value without passing through the same node twice.

The function in this case must return the triple:
- path from root to minimum node
- path from root to maximum node
- shortest path going from minimum to maximum

Example:
In the previous case the minimum value is -22, the maximum value is 9.
The shortest path that connects them and which must be returned is [-22, -10, 1, -3, 9].
The function must return:
     ([-7, 1, -10, -22], [-7, 1, -3, 9], [-22, -10, 1, -3, 9])
'''

from nary_tree import NaryTree


def ex1(root): # root type is NaryTree 
    pass

'''
root = NaryTree.fromList(
    [ -7,
        [1,  [-10, [6],
                   [-22]],
             [-3,  [9]]],
        [2,  [-8,  [7]],
             [-10, [-9]],
             [-5   ]],
        ])

# print(ex1(root))
'''

# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: 6 points
Define the function ex2(dirin, extensions), which is recursive or uses recursive functions or methods,
which receives as arguments:
   - dirin: the path of a directory
   - extensions: a list of file extensions (strings)

The function explores dirin and all its subdirectories (all
levels) and searches for all files with one of the indicated extensions.
The function returns a dictionary whose keys are the directory paths
and explored subdirectories (with the '/' separator which applies to both Windows and Unix)
and as values a pair (min, max) where min and max are the dimensions
of files with one of those smaller and larger extensions respectively
present in that directory.
Directories that do not contain any files with the indicated extensions do not appear in the dictionary.

NOTE 1: you can use the functions: os.listdir, os.path.isfile, os.path.isdir, os.path.getsize ...
NOTE 2: Using the os.walk function is prohibited
NOTE 3: use the '/' character as path separator
(which works on both Windows and MacOS or Linux)

Example:
if the dirin path is "ex2/A" and the extensions = ["txt", "pdf", "png", "gif"]
the function returns:
{'ex2/A': [29, 56], 'ex2/A/C': [29, 92], 'ex2/A/B': [25, 28]}
'''

import os

def ex2(dirin, extensions):
    pass


#print(ex2('ex2/A', ["txt", "pdf", "png", "gif"]))
#print(ex2('ex2', ["png", "gif"]))
#print(ex2('ex2/C', ["pdf", "png"]))

######################################################################################

if __name__ == '__main__':
    print('*' * 50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*' * 50)
