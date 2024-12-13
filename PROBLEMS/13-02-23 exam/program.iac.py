#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER
 3) Change the directory name examPY in your matriculation number

To pass the exam you have to:
    - solve at least 3 func problems and
    - solve at least 1 rec problem
    - get a score greater or equal to 18

The final score is the sum of the solved problems.
"""
name       = "iac"
surname    = "masi"
student_id = "99999"

#########################################

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

# %%  ---- FUNC1 ----
''' func1: 2 points

A dictionary D is provided as input. D has integer keys and its values are
lists of strings with repetitions.

D = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}

Write the function func1(D) that builds and returns the
list W that contains the values obtained by taking, for each key K in D,
the corresponding item from the list L associated to K;
before picking an item, the function sorts L in reversed order.

Given the D as defined above, the function returns:

    W = ["c", "b", "b"]

as the first list sorted in reversed order is ["h", "g", "f", "e", "c"],
and its 4th item is "c"; the second list is ["z", "w", "b", "a"], and its
2nd item is "b"; the third list is ["b", "a", "a"] and its 0th item is "b".

'''

def func1(D):
    out = []
    for k in D.keys():
        D[k].sort(reverse=True)
        out.append(D[k][k])
    return out


# %%  ---- FUNC2 ----
''' func2: 2 points

Implement the func2(list_all, list_rm) function to destructively delete
from list_all all the integers that are not contained in list_rm.
The function does not considers the repetitions in list_all,
so the resulting list will not contain repetitions.

Example: if  list_all = [2, 4, 3, 4, 4, 3, 4, 5, 2, 6]
         and list_rm = [5, 3, 2, 7]
         list_all must be destructively changed to [2, 3, 5]

'''

def func2(list_all, list_rm):
    L = []
    for v in list_all:
        if v not in L and v in list_rm:
            L.append(v)
    list_all[:] = L


# %%  ---- FUNC3 ----
'''  func3: 2 points

Implement the func3(strList) that:
- takes as input a list of strings
- computes the sum of the ascii codes of the characters of each string,
obtaining an integer value for each string, and adding all the obtained
values to a list;
- returns the list of integers sorted, based on the initial string values
in the list strList, in ascending order.

For example, if strList = ["monkey", "cat", "panda", "alligator"]
the corresponding ascii values are: [659, 312, 516, 959]
that, based on the alphabetical ordering of the initial list, are returned as:
[959, 312, 659, 516]
'''

def func3(strList):
    return [sum(map(ord, S)) for S in sorted(strList)]


# %%  ---- FUNC4 ----
''' func4: 5 points

    Implement the function  func4(M) that takes as arguments:
    - M: a 2 dimensional matrix of integers represented as lists of lists

    The function returns the result of R + C, where R is the product
    of the values obtained by summing each row of M, and C is the
    product of the values obtained by summing each column of M.

    Example:
        Suppose M is:
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 0, 1, 2]]
        then, the sums computed on its rows are 10, 26, 12, and their product is 3120;
        the sums computed on its columns are 15, 8, 11, 14, and their product is 18480;
        so, the function returns 21600.

'''


def prod(L, p=1):
    for v in L: p *= v
    return p

    
def func4(M):
    R = prod(map(sum, M))
    C = prod(map(lambda *args: sum(args), *M))
    return R + C


# %%  ---- FUNC5 ----
''' func5: 6 points

Write a function func5(points) that takes a list of (x,y) coordinates
of N points in the Cartesian plane (N >= 3). Each point is a pair of integers.
For each point, we consider its distance from the center of the plane (0,0).

The function must return the barycenter (X, Y) of the 3 points that are closer to
the center of the plane.
All values should be reported to an accuracy of 3 decimal places (you can use
the round function to do that).

  - NOTE: The distance between 2 points (x1, y1) and (x2, y2)
    is the Euclidean distance: sqrt[(x1-x2)² + (y1-y2)²]
  - NOTE: The barycenter of N points is the point (X', Y'),
    where X' is the mean of the x coordinates and Y' is the mean
    of the y coordinates of the N points.

For example, if points = [(2, 2), (-1, 1), (3, 0), (3, 2), (2, -1)]
the corresponding (unsorted) distances are: 2.828, 1.414, 3.0, 3.606, 2.236
and, after sorting them, the resulting barycenter of the 3 points
closest to (0, 0) is: (1.0, 0.667)
'''

def func5(points):
    cl_pts = sorted(points, key=lambda xy: xy[0]**2 + xy[1]**2)[:3]
    return tuple(map(lambda *args: round(sum(args)/3, 3), *cl_pts))


# %% ----------------------------------- EX.1 ----------------------------------- #
'''
Ex1: 6 points
    Implement the ex1(root, result) function, recursive or using
    recursive functions, with 2 arguments:
    - root:  the root of a binary tree;
    - result: an empty list, that will be populated with the result (see below).

    The tree is made of instances of the BinaryTree class defined in tree.py.
    The function should build and return a list in the parameter "result",
    in which each i-th item contains the sum of all the nodes at depth i
    (the root of the tree is at depth 0).

    Example:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    If the tree is the left one, result = [5, 10, 13]
    If the tree is the right one, result = [2, 12, 12, 24]
'''

from tree import BinaryTree


def ex1(root, result, level=0):
    if root.left: ex1(root.left, result, level+1)
    if root.right: ex1(root.right, result, level+1)
    ninc = max(level+1 - len(result), 0)
    result[:] = result + [0]*ninc
    result[level] += root.value



# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: 6 + 3 points
    Implement the ex2(dirin, words) function, recursive or using recursive
    functions or methods, having the argument:
    - dirin: the path of an existing directory
    - words: a list of words
    The function will go through dirin and all its subfolders (at any level),
    and count the occurrences of the words in the input list in all the
    text files (i.e., files having the .txt extension) found in any folder.
    A word occurs in a file, if and only if it is separated from the preceding
    or following word, if there are, by a space, a tab, or a newline character.

    (6 points) The function returns a list of pairs (word, occ), in which the first
    value of each pair is one of the words in the input list and the second
    value of the pair is the number of occurrences of that word in the text files.
    (+ 3 points) The list is sorted on the number of occurrences of the words
    (in descending order); if two or more words have the same number of occurrences,
    they are sorted alphabetically (in ascending order).
    If a word in the input list never occurs, it still has to be returned
    by the function.

    NOTICE 1: you could find useful the functions: os.listdir, os.path.join,
    os.path.isfile, os.mkdir, os.path.exists ...
    NOTICE 2: it is forbidden to use the os.walk function

    For example, given the folder "ex2" and if words = ["cat", "dog"]
    the function returns: [('dog', 11), ('cat', 6)]

'''

import os

def parse_file(full_path, out):
    with open(full_path) as fr:
        for w in fr.read().split():
            if w in out:
                out[w] += 1

def ex2(dirin, words, out=None, start=0):
    if out is None:
        out, start = {w: 0 for w in words}, 1
    for item in os.listdir(dirin):
        full_path = dirin + '/' + item
        if os.path.isfile(full_path) and item.endswith('.txt'):
            parse_file(full_path, out)
        elif os.path.isdir(full_path):
            ex2(full_path, words, out)
    return sorted(((k, v) for k, v in out.items()), key=lambda T: (-T[1], T[0])) if start else None

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    pass
