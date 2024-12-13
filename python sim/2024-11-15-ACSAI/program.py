#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

"""
#####################    INSTRUCTIONS FOR THE SIMULATION.  ####################

FIRST OF ALL: Assign the following variables with your
    FIRST NAME, LAST NAME, REGISTRATION NUMBER

Add your implementations of the functions described below.
To get the score, execute the file grade.py contained in the folder.
To pass the simulation, it is sufficient to obtain a score greater than or equal to 18.
"""

from os.path import isfile, isdir
from os import listdir
name = "Leila"
surname = "Zanoni"
student_id = "2033176"

################################################################################
################################################################################
################################################################################

################################################################################
# %% ----------------------------------- FUNC.1 ------------------------------ #
################################################################################
'''func1: 4 marks

Define the function func1(file_in) that takes as input a string indicating
the path to a text file and returns a list of strings. The function opens the
text file and extracts all words, converting them all to lowercase. The
function returns a list of unique words found in the text file,
sorted in alphabetical order.
Words are sequences of characters (alphabetical and non-alphabetical)
separated by any number of spaces, tabs or newlines.

Example:
if file_in points to 'txt/in_01.txt', the function returns
expected = ['bat', 'car', 'cat', 'condor', 'rat']

'''


def func1(file_in):
    # your code goes here
    strings = []
    with open(file_in, encoding='utf8') as f:
        for line in f:
            word = line.strip().split()
            strings.append(word)
    lista = [element.lower() for inner in strings for element in inner]
    unique = list(set(lista))
    return sorted(unique)


# print(func1('txt/in_01.txt'))
# print(func1('txt/in_02.txt'))
# print(func1('txt/in_03.txt'))
# print(func1('txt/in_04.txt'))

################################################################################
# %% -------------------------------- FUNC.2 --------------------------------- #
################################################################################
''' func2: 4 marks
Define the function func2(file_in_a)
that takes as input 1 string pointing to a text file.

The function opens the text files and looks for
sequences of any number of consecutive spaces.
Sequences of spaces cannot span multiple lines.
That is, a sequence of consecutive spaces will interrupt
when a newline character is reached.
The function returns the longest sequence of consecutive
spaces found in the file.

Example:
for input 'txt/in_01.txt' the function returns 
'''


def func2(file_in_a):
    with open(file_in_a, encoding='utf8', mode='r') as f:
        max_count = 0
        for line in f:
            count = 0
            for char in line:
                if char == ' ':
                    count += 1
                    if count > max_count:
                        max_count = count
                else:
                    count = 0
    return max_count

# print(func2('txt/in_01.txt'))
# print(func2('txt/in_02.txt'))
# print(func2('txt/in_03.txt'))
# print(func2('txt/in_04.txt'))


################################################################################
# %% -------------------------------- FUNC.3 --------------------------------- #
################################################################################
'''func3: 6 marks
Implement the func3(list_s, list_i, filepath): 
that takes as arguments: 
- a list of lists of strings, called list_s 
- a list of lists of integers, called list_i 
- a string filepath, indicating the path of a text file the function must write.
The inner lists of list_s and list_i have the same number of elements.
The function returns an integer.

For each list of words in list_s, the function writes a line in filepath.  
The writing order of the words on each line is specified 
by the corresponding list of integers in list_i, which should be 
considered as the positions of the words to read from the lists 
and write to the file.

The function returns the total number of words written to the out file.

Example if:
lists = [["monkey", "cat",], 
         ["panda", "alligator"], 
         ["zoo", 'zuu','zotero']] 
listi=  [[1, 0],	# first the word at position 1 then 0
         [0, 1],	# first the word at position 0 then 1
         [2, 1, 0]]	# first the word at position 2 then 1 then 0
the return value is 7 and the file out contains:

cat monkey
panda alligator
zotero zuu zoo
'''


def func3(list_s, list_i, filepath):
    # your code goes here          

    # your code goes here
    with open(filepath, 'w') as f:
        for j, string in enumerate(list_s):
            print(" ".join(string[i] for i in list_i[j]), file=f)

    return sum(len(s) for s in list_s)


#print(func3([["monkey", "cat"], ["panda", "alligator"], ["zoo", 'zuu', 'zotero']],[[1, 0], [0, 1], [2, 1, 0]], 'txt/out_01.txt'))


################################################################################
# %% ----------------------------------- FUNC.4 ------------------------------ #
################################################################################
""" func4: 6 marks

Write a function func4(list_A) that takes a list of tuples.
In each tuple, the first item is a string, the second item is a list
of integers.
The function returns a dictionary, in which:
- each key K is one of the strings in the tuples in list_A;
- the corresponding value V is the list obtained by merging
    the lists in the tuples of list_A having K as first item, sorted
    in ascending order; V cannot contain duplicates.

For example, if list_A = [("cat", [7, 3]), ("dog", [1, 4]), ("cat", [2, 7])]
the function returns {"cat":[2, 3, 7], "dog": [1, 4]}
"""

"""Steps:
    1- create dict
    2- put the strings as keys
    3- merge the lists (sets so no duplicate)
    4- sort
    """


def func4(list_A):
    # your code goes here
    diz = {}
    for s, l in list_A:
        if s not in diz:
            diz[s] = set(l)
        else:
            diz[s].update(set(l))

    for k, v in diz.items():
        diz[k] = sorted(v)
    return diz

#print(func4([("cat", [7, 3]), ("dog", [1, 4]), ("cat", [2, 7])]))
# print(func4([("cat", [1, 7, 3]), ("dog", [1, 4, 5, 7]), ("cat", [2, 7]), ("bat", [7, 6, 5, 4, 2])]))
# print(func4([("cat", [1, 7, 3]), ("dog", [1, 4, 5, 7]), ("cat", [2, 7]), ("bat", [7, 6, 5, 4, 2]),
#              ("dog", [1, 5, 4, 7]), ("velociraptor", [0])]))
# print(func4([("cat", [1]), ("dog", [1]), ("cat", [1]), ("bat", [1]),
#              ("dog", [1]), ("velociraptor", [0])]))


################################################################################
# %% -------------------------------- FUNC.5 --------------------------------- #
################################################################################

""" func5: 6 marks

Write a function that reads an input file filein and writes a file fileout.
All the words read from the file input are written in the file in output in one
single line, separated by a comma followed by one space and sorted by their
lengths in decreasing order, in case of a tie, by the number of vowels in
increasing order and, finally, in alphabetical order.
The function returns the number of words found in filein.
"""
def count_vowels(w):
    s = 0
    for c in "aieouAEIOU":
        s += w.count(c)
    return s

def func5(filein, fileout):
    # Your code goes here
    with open(filein, encoding='utf8') as f:
        text = f.read().split()
        
    with open(fileout, mode='w') as f:
        print(", ".join(sorted(text, key=lambda x: (-len(x), count_vowels(x), x))), file=f)
        
    return len(text)
#print(func5('txt/in_01.txt', 'txt/out_f5_01.txt'))

################################################################################
# %% -------------------------------- FUNC.6 --------------------------------- #
################################################################################


''' func6: 8 marks

Write a function func5(folderpath) that reads the content of a given folder,
including all files and subfolders within it, recursively.

The function should return a dictionary with the following keys and values:
- "file_paths": A list of file paths (as strings) for all files
  in the folder and its subfolders, sorted by the length of each path.
  If paths have the same length, they should be sorted alphabetically.
- "subfolder_paths": A list of paths (as strings) for all subfolders
  in the folder and its subfolders, sorted by the length of each path.
  If paths have the same length, they should be sorted alphabetically.

If the folder contains no files, "file_paths" should be an empty list.
If the folder contains no subfolders, "subfolder_paths" should be an empty list.

YOU CANNOT USE THE FUNCTION os.walk()

Hint:
- You can use the os.listdir() function to get a list of items in a folder.
- To create the full path for each item, join the folder path and item name with +'/'+.
- To check if an item is a file or a folder, use os.path.isfile() or os.path.isdir().

Example:

Suppose the folder contains the following structure:
- A file at "folder/b.txt"
- A file at "folder/subfolder/abc.txt"
- A file at "folder/a.txt"
- A subfolder at "folder/subfolder"
- A subfolder at "folder/subfolder/nested_folder"

The function will return:

{
  "file_paths": ["folder/a.txt", "folder/b.txt", "folder/subfolder/abc.txt"],
  "subfolder_paths": ["folder/subfolder", "folder/subfolder/nested_folder"]
}
'''


def my_key(x):
    # your code goes here
    return (len(x), x)


def func6(folderpath):
    # your code goes here
    d = { 'file_paths' : [], 'subfolder_paths' : []}
    for file in listdir(folderpath):
        filepath = folderpath + '/' + file
        if isfile(filepath):
            d['file_paths'].append(filepath)
        elif isdir(filepath):
            d['subfolder_paths'].append(filepath)
            res = func6(filepath)
            d['file_paths'].extend(res['file_paths'])
            d['subfolder_paths'].extend(res['subfolder_paths'])

    for l in d.values():
        l.sort(key = my_key)
    return d

print(func6("func6/A"))
# print(func5("func5/B"))
# print(func5("func5/C"))
# print(func5("func5"))


###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

# %%
