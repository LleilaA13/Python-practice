#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER
 3) Change the directory name `examPY` into your student ID number

To pass the exam you are required to:
    - solve at least 3 func problems,
    - solve at least 1 rec problem, and
    - obtain a score of 18 or greater

The final score is the sum of the scores associated with each problem.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""
name       = "Maurizio"
surname    = "Mancini"
student_id = "12345678"

#########################################

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To avoid running certain tests, comment out the corresponding  entries in
# the 'tests' list at the end of grade.py.
################################################################################

# %%  ---- FUNC1 ----
''' func1: 2 marks

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
    for i, I in enumerate(a_list):
        prod = I[0]
        for p in I[1:]:
            prod *= p
        a_list[i] = prod
    return len(a_list)


# %%  ---- FUNC2 ----
''' func2: 2 marks

Write a function func2(a_dictionary) that takes a dictionary as
parameter, in which:
- the keys are single alphabetical characters
- the items are lists of positive integers

The function returns the character for which the corresponding
list of integers sums to the highest value. If multiple characters
sum to the same maximum value, the first one in alphabetical order
is returned.

For example, func2({"a" : [3, 2, 2], "b" : [4, 2, 3], "c" : [-4, 2, 2]})
returns "b", as the list [4, 2, 3] sums to the highest value among all
the lists in the dictionary.
'''

def func2(a_dictionary):
    for K in a_dictionary:
        a_dictionary[K] = sum(a_dictionary[K])
    L = list(a_dictionary.items())
    L.sort(key=lambda x : (-x[1], x[0]))
    return L[0][0]

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
    res = []
    for A, B in zip(list_A, list_B):
        C = set([x.lower() for x in A]).intersection(set([x.lower() for x in B]))
        C = list(C)
        C.sort()
        C = "".join(C)
        res.append(C)
    return res

# %%  ---- FUNC4 ----
''' func4: 4+2 marks

(4 marks) Write a function func4(input_txt, output_txt) that takes two file
names as parameters. The function reads the text file input_txt
and returns the number of words longer than 3 characters contained
in the file. The words can be separated by any number of spaces
or newlines.

(2 marks) The function writes the text file output_txt that contains
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
    fileRef = open(input_txt, "r", encoding="utf-8")
    res = []
    for line in fileRef:
        L = line.strip().split()
        for item in L:
            if len(item) > 3:
                res.append(item + "\n")
    fileRef.close()
    fileRef = open(output_txt, "w", encoding="utf-8")
    fileRef.writelines(res[::-1])
    fileRef.close()
    return len(res)


# %%  ---- FUNC5 ----
''' func5: 6 marks

Write a function func5 that takes as input an RGB image.
The function counts and returns the number of non-black "isolated"
pixels, that is, pixels preceeded and followed by black pixels (i.e., given
a pixel P, there is a black pixel preceeding and following P).
If a pixel P is on the left or right border of the image
(i.e., it is on the first or last column), then we consider it
"isolated" only if the following or preceeding pixel is black.
Additionally, the function saves an RGB image with the same
width and height of the input image and in which only
the isolated pixels are copied.

For example, if B is a black pixel and * is a non-black pixel,
given the image:

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
    black = (0, 0, 0)
    img = images.load(input_file_name)
    img_out = [[black] * len(img[0]) for _ in range(len(img))]
    counter = 0
    for row_i in range(len(img)):
        for col_i in range(len(img[row_i])):
            pixel = img[row_i][col_i]
            if pixel != black and ((col_i > 0 and img[row_i][col_i - 1] == black) \
            and (col_i < len(img[0]) - 1 and img[row_i][col_i + 1] == black) or \
            (col_i == 0 and img[row_i][col_i + 1] == black) or (col_i == len(img[0]) - 1 and img[row_i][col_i - 1] == black)):
                counter += 1
                img_out[row_i][col_i] = img[row_i][col_i]
    images.save(img_out, output_file_name)
    return counter

# %% ----------------------------------- EX.1 ----------------------------------- #
'''
Ex1: 8 marks

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

def rec_scan(folder, L):
    items = listdir(folder)
    counter = 0
    for item in items:
        if isdir(folder + "/" + item):
            rec_scan(folder + "/" + item, L)
        else:
            if item[-4:] == ".txt":
                counter += 1
    L.append((folder, counter))


def ex1(target_folder):
    L = []
    rec_scan(target_folder, L)
    L.sort(key=lambda x : (-x[1], x[0]))
    return L



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

def tree_scan(T, L, S, D):
    if T.left is None and T.right is None:
        L += 1
    if T.left is None and T.right is not None:
        S += 1
    if T.left is not None and T.right is None:
        S += 1
    if T.left is not None and T.right is not None:
        D += 1
    if T.left is not None:
        (nL, nS, nD) = tree_scan(T.left, L, S, D)
        L = nL
        S = nS
        D = nD
    if T.right is not None:
        (nL, nS, nD) = tree_scan(T.right, L, S, D)
        L = nL
        S = nS
        D = nD
    return (L, S, D)
        
    
def ex2(T):
    return tree_scan(T, 0, 0, 0)

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
    
    # L = [[1, 2, 3], [-1, 2, 3], [2, 2, -2]]
    # res = func1(L)
    # print(f"({L}, {res})")
    
    # L = [[-1, 0, 1], [999999, -99999], [1], [0], [-9999999]]
    # res = func1(L)
    # print(f"({L}, {res})")
    
    # L = []
    # res = func1(L)
    # print(f"({L}, {res})")
    
    # L = [[1, 2, 3, 4, 5, 6, 7, 8], [987, 9876, 9876, 9], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0], [-9, -8, -7, -6, -5]]
    # res = func1(L)
    # print(f"({L}, {res})")
    
    # D = {"a" : [3, 2, 2], "b" : [4, 2, 3], "c" : [-4, 2, 2]}
    # print(func2(D))
    
    # D = {"a" : [3, 2, 2, -1, -1], "b" : [4, 2, 3, -4], "c" : [-4, 2, 2]}
    # print(func2(D))
    
    # D = {"C" : [1, 1, 1, 1, 1, 1], "b" : [6]}
    # print(func2(D))
    
    # D = {"C" : [0], "B" : [1], "A" : [1, -1, 1, -1, 1, -1, 1, -1, 1], "a" : [-1]}
    # print(func2(D))
    
    # list_A = ["flash", "ColA", "USED", "lazer"]
    # list_B = ["Rabit", "HELIOS", "trick", "suPER"]
    # print(func3(list_A, list_B))
    
    # list_A = ["RAM", "rom", "JaM", "leAP", "star"]
    # list_B = ["", "aBcDeFgH", "aBcDeFgH", "aBcDeFgH", "aBcDeFgH"]
    # print(func3(list_A, list_B))
    
    # list_A = ["abcdefghijklmnopqrstuwxyz", "abcdefghijklmnopqrstuwxyz"]
    # list_B = ["ZYXWUTSRQPONMLKJIHGFEDCBA", "zyxwutsrqponmlkjihgfedcba"]
    # print(func3(list_A, list_B))
    
    # list_A = ["catode", "dermatoglyphics", "uncopyrightable"]
    # list_B = ["ZYXWUTSRQPONMLKJIHGFEDCBA", "zyxwutsrqponmlkjihgfedcba", "zyxwutsrqponmlkjihgfedcba"]
    # print(func3(list_A, list_B))
    
    # print(func4("func4/in_example1.txt", "func4/exp_example1.txt"))
    # print(func4("func4/in_example2.txt", "func4/exp_example2.txt"))
    # print(func4("func4/in_example3.txt", "func4/exp_example3.txt"))
    # print(func4("func4/in_example4.txt", "func4/exp_example4.txt"))
    
    print(func5("func5/img1_in.png", "func5/img1_exp.png"))
    print(func5("func5/img2_in.png", "func5/img2_exp.png"))
    print(func5("func5/img3_in.png", "func5/img3_exp.png"))
    
    # print(ex1("ex1/A"))
    # print(ex1("ex1/abracadabra"))
    # print(ex1("ex1/1"))
    # print(ex1("ex1/test"))
    
    # root = BinaryTree.fromList([25, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
    # print(ex2(root))
    # root = BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [15, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [-9, None, None]]]])
    # print(ex2(root))
    # root = BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    # print(ex2(root))