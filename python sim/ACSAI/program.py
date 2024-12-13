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
'''func1: 4 marks
Define the function func1(int_list, m, n) that takes as its
input a list of integers int_list and two integer m and n.
The function returns a dictionary in which the keys are the
integers of the int_list not included in the range [m, n]
included and the corresponding values are the number of
repetition of the key in the int_list.

Example:
    func1([4, 4, 10, 4, 2, 1, 2], 4, 8) should return the dictionary
    {1: 1, 2: 2, 10: 1}
'''


def func1(int_list, m, n):
    # Write your code here
    my_dict = {k: 0 for k in int_list if k < m or k > n}
    for k in my_dict.keys():
        for x in int_list:
            if k == x:
                my_dict[k] += 1
    return my_dict
# if __name__ == 'main':
# print(func1([4, 4, 10, 4, 2, 1, 2], 3, 8))


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 4 marks
Define a function func2(str1, str2) that takes as input two strings of
the same length and constructs a new string str3 obtained by
considering, for each pair of characters in str1 and str2 in position i,
the highest one in alphabetical order. The input strings str1 and str2
are made of lower case alphabetical characters. The function returns the
constructed string, all uppercase.

Example:
    func2('plane', 'react') must return the string 'PEACE'

'''


def func2(str1, str2):
    return "".join(min(a, b) for a, b in zip(str1, str2)).upper()
# print(func2('plane', 'react'))


# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 4 marks
Define a function func3(L0, L1) that receives 2 lists L0 and L1.
The first list L0 contains strings S0, S1, ... Sn-1,
the second list L1 contains positive integers I0, I1, ... In-1.
The function returns a string obtaining by concatenating each string
Sj repeated Ij times.
For example, if L0 = ['ab', 'o o'] and L1 = [2, 3] the function returns:
'ababo oo oo o'.
'''


def func3(L0, L1):
    # Write your code here
    res = ''
    for i, count in enumerate(L1):
        if i < len(L0):
            res += L0[i] * count
    return res


# print(func3(['ab', 'o o'], [2, 3]))


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 marks
Define a function func4(D) that receives as input a dictionary, in which
each key is a string and the corrisponding value is a collection
(a set, a dictionary, a list, ...).
The function returns a list of lists, in which each sublist S corresponds
to an item of the input dictionary and contains the following:
- as first item I0, the key of the corresponding dictionary item
- as second item I1, the value of the corresponding dictionary item
The sublists are sorted by the length of the second item I1 in each sublists,
in reversed order (from the longest to the shortest).
If the two sublists have a second item with the same length, they are sorted
based on the value of the first item I0 (alphabetically, or numerically).
For example, if D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
the function returns: [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]]
"""


def func4(D):

        # Create a list of sublists, each containing the key and its corresponding value
    lista = [[k,v] for k, v in D.items()]
    return sorted(lista, key = lambda x:(-len(x[1]), x[0]))


#print(func4({"f": (1, 2, 3), "a": ["h", "w"], "c": {"f": 3, "g": [1, 2]}}))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 6 marks
Write a function func5(list_A, list_B) that takes two lists with the
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
"""


def func5(list_A, list_B):
    # Write your code here
    result = []
    for a, b in zip(list_A, list_B):
        set_a = set(a.lower())
        set_b = set(b.lower())

        set_c = set_a & set_b
        result.append("".join(sorted(set_c)))
    return result

print(func5(["aBd", "baC", "cAb"], ["bcE", "dca", "eDf"]))

# %% ----------------------------------- FUNC6 ------------------------- #
""" func6: 6 marks
Write a function func6(a_dictionary) that takes a dictionary as
parameter, in which:
- the keys are single alphabetical characters
- the items are lists of positive integers

The function returns the character for which the corresponding
list of integers sums to the highest value. If multiple characters
sum to the same maximum value, the first one in alphabetical order
is returned.

For example, func6({"a" : [3, 2, 2], "b" : [4, 2, 3], "c" : [-4, 2, 2]})
returns "b", as the list [4, 2, 3] sums to the highest value among all
the lists in the dictionary.
"""


def func6(a_dictionary):
    max_num = -200000000000
    max_char = ""

    for c, numbers in a_dictionary.items():
        sum_nums = sum(numbers)
        if sum_nums > max_num:
            max_num = sum_nums
            max_char = c
        elif max_num == sum_nums and c < max_char:
            max_char = c
    return max_char
        
    


###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

# %%
