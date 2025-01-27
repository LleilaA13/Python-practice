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


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 4 points
Define the function func1(D1: dict[str, int], D2: dict[str, int]) -> dict[int, str],
which receives as arguments two dictionaries D1 and D2 with strings as keys
and integers as values. func1 must return a dictionary with 
integers as keys and strings as values.

The output dictionary must contain as keys all the integer values in D1 and
D2 that belong to the keys not in common between the two dictionaries.
For every integer key in the output dictionary, the corresponding value is
the string obtained by concatenating the original keys of D1 or D2 with that
integer as a value.
The strings to be concatenated (if there are more than one) must be sorted in
decreasing order of length and, in case of a tie, in ascending
alphabetical order.

Example:
D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 4}
D2 = {'bb': 4, 'ee': 4, 'ff': 1, 'ggg': 1}

Result: {1: 'gggaaccff', 4: 'dddee'}
'''

def func1(D1,  D2):
    ## Write your code here
    d = {D2[v] : v  for v in D1 if v not in D2  for v in D2 if v not in D1}
    


    return d
            
        
        
    
            

## Tests
D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 4}
D2 = {'bb': 4, 'ee': 4, 'ff': 1, 'ggg': 1}
print(func1(D1, D2))  # {1: 'gggaaccff', 4: 'dddee'}


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Define the function func2(text: str, n: int) -> list[str]
that receives as arguments
- a 'text' string made up of words separated by spaces, tabs and newlines
- an integer 'n'
and returns the list of words in 'text' that have at least n characters,
ordered in the opposite order they have in the input text.

Example:
text = 'la rana in Spagna gracida in campagna'
n = 3
expected result = ['campagna', 'gracida', 'Spagna', 'rana']
'''
def func2(text, n):
    ## Write your code here
    pass

## Tests:
#text = 'la rana in Spagna gracida in campagna'
#n = 3
#print(func2(text, n))  # ['campagna', 'gracida', 'Spagna', 'rana']

# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 2 points
Define the function func3(S1 : set[str], S2 : set[str]) -> dict[str,list[str]]
that receives two sets of strings S1 and S2 as arguments and returns 
a dictionary.
The output dictionary has as keys the strings of S1 that are prefixes of at
least one string of S2 and as values the list of S2 strings that have that prefix.
The lists associated with each key must be sorted in descending order
in length and, in the event of a tie, in ascending alphabetical order.

Example:
S1 = {'a', 'b', 'c'}
S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
Result = {'a': ['abc', 'aa', 'ab'], 'c': ['cc', 'cd'], 'b': ['bb', 'bc']}
'''

def func3(S1, S2):
    ## Write your code here
    pass

## Tests
#S1 = {'a', 'b', 'c'}
#S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
#print(func3(S1, S2))  # {'a': ['abc', 'aa', 'ab'], 'c': ['cc', 'cd'], 'b': ['bb', 'bc']}

#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 8 points
Define the function func4(png_file: str, N: int) -> int
that receives as arguments
- the name of a PNG file that contains an image with a black background with
     several non overlapping colored squares of at least 3x3 pixels in size
- an integer N indicating what size of squares you need to search for. 
The result is a dictionary that has the colors of the squares as keys
and as values the number of squares of that color, with dimensions NxN
present in the image.

Example:
If the image is "func4/1.png" and N=5, then the dictionary to return is:
{(125, 190, 250): 1, (184, 100, 249): 2, (115, 186, 199): 1, (139, 150, 176): 1, (250, 240, 236): 1, (125, 157, 232): 1}
"""

import images

def func4(png_file, N):
    ## Write your code here
    pass

##Tests
#print(func4('func4/1.png', 5))  # {(125, 190, 250): 1, (184, 100, 249): 2, (115, 186, 199): 1, (139, 150, 176): 1, (250, 240, 236): 1, (125, 157, 232): 1}

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 4 points
Define the function func5(file_txt: str, K: int, P: int) -> list[list[int]]
that receives as arguments
- file_txt: the name of a txt file containing an NxM matrix of integers
  separated by spaces. Each line corresponds to a row of the matrix.
- K and P, two integers
and returns as a result the matrix read from the file, represented as a
list of lists of integers. Moreover, all the multiples of K in the original
matrix must be multiplied by P, while the others are the original values.

Example:
if the matrix read from the file is the following:
1 2 3
4 5 6
7 8 9
10 11 12
and the values of K=3 and M=10, then the matrix to return is:
[[1, 2, 30],
  [4, 5, 60],
  [7, 8, 90],
  [10, 11, 120]]
"""

def func5(file_txt, K, M):
    ## Write your code here
    pass


## Tests
#file_txt = 'func5/1.txt'
#K = 3
#M = 10
#print(func5(file_txt, K, M))  # [[1, 2, 30], [4, 5, 60], [7, 8, 90]]

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points

Define the function ex1(dirname, necessary, forbidden), recursive or using
recursive functions or methods, that receives as arguments
  - dirname: a string containing the name of a directory to search for files
  - necessary: a list of words that must be present in the files
  - forbidden: a list of words that must be absent in the files
and scans the directory and all its subdirectories looking for files that meet
the following conditions:
- have '.txt' extension
- contain all the words present in 'necessary'
- do not contain any of the words in 'forbidden'

Words are sequences of characters separated by whitespaces.

The function must return the list with the paths of all the found files,
sorted in order of increasing depth and in case of a tie in decreasing
alphabetical order.

NOTICE 1: It is recommended to use the os.listdir functions,
os.path.isfile and os.path.isdir and NOT the os.join function in
Windows. Use string concatenation with the '/' character.

NOTICE 2: It is prohibited to use the os.walk function

Example:
dirname = 'ex1/AAA'
necessary: ['hello', 'mom']
forbidden: ['daddy', 'grandfather']

Result: ['ex1/AAA/share/recollection/lamentable/dogsled.txt', 'ex1/AAA/heavy/tomorrow/flare/cellar.txt',
             'ex1/AAA/heavy/spoon/cranberry.txt', 'ex1/AAA/heavy/roster/prosecutor.txt', 'ex1/AAA/gifted/systemize/due.txt',
             'ex1/AAA/gifted/systemize/distinction.txt', 'ex1/AAA/share/help.txt', 'ex1/AAA/regime.txt', 'ex1/AAA/mayonnaise.txt']
"""

import os


def ex1(dirname, necessary, forbidden):
    ## write your code here
    pass

## Tests
# dirname = 'ex1/AAA'
# necessary = ['ciao', 'mamma']
# forbidden = ['papa', 'nonno']
# print(ex1(dirname, necessary, forbidden))
# '''['ex1/AAA/share/recollection/lamentable/dogsled.txt',
# 'ex1/AAA/heavy/tomorrow/flare/cellar.txt',
# 'ex1/AAA/heavy/spoon/cranberry.txt',
# 'ex1/AAA/heavy/roster/prosecutor.txt',
# 'ex1/AAA/gifted/systemize/due.txt',
# 'ex1/AAA/gifted/systemize/distinction.txt',
# 'ex1/AAA/share/help.txt',
# 'ex1/AAA/regime.txt',
# 'ex1/AAA/mayonnaise.txt']
# '''

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 points

Define the function ex2(root), recursive or using recursive functions
or methods, that receives as argument the root of a binary tree,
defined as a node of type tree.BinaryTree.
The function must destructively modify the input tree by swapping the
positions of each child of each node that is at an even depth level.
Assume that the root is at depth 0.
The function must return the number of swapped nodes.

Example:
If the tree is as follows:
                    | depth
         1          |  0
        / \         |
       2   3        |  1
      / \ / \       |
     4  5 6  7      |  2
    / \    \        |
   8   9   10       |  3

it will become:
                    | depth
         1          |  0   2 children swapped
        / \         |
       3   2        |  1    
      / \ / \       |
     6  7 4  5      |  2   3 children swapped
    /    / \        |
   10   9   8       |  3    

and the function returns the number of swapped nodes: 5
"""

import tree

def ex2(root):
    ## Write your code here
    pass

## Tests
'''
root = tree.BinaryTree.fromList([1, [2, [4, [8, None, None],
                                            [9, None, None]],
                                        [5, None, None]],
                                    [3, [6, None,
                                            [10, None, None]],
                                        [7, None, None]]])
toor = tree.BinaryTree.fromList([1, [3, [6, [10, None, None],
                                            None],
                                        [7, None, None]],
                                    [2, [4, [9, None, None],
                                            [8, None, None]],
                                        [5, None, None]]])
print(ex2(root))  # 5
print(root == toor)  # True
'''
###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
