
import os
"""Design the function  es35(dir1, word_set), that takes as inputs:
        dir1:   the path of a directory
        word_set:  a set of words (character strings between 'a' and 'z')
    and does the following:

    it searches in dir1 for files with extension .txt that contain any
    string present in word_set and returns a dictionary of the found
    words. The function does not consider dir1 subdirectories.  The
    returned dictionary only contains the words actually found within
    the .txt files in dir1 and the attribute of each key is a tuple of
    two integers. The first element of the tuple is the total number
    of times the word can be found in dir1 .txt files. The second
    element of the tuple is the number of different dir1 .txt files in
    which the word can be found.

    A word is a sequence made of characters between 'a' and 'z'.  All
    dir1 .txt files contain only words separated by spaces, tabs or
    new line characters, namely, there are no capital letters or punctuation
    marks.

    """

def es35(dir1, word_set):

    # insert here your code
    diz = {w:[0,0] for w in word_set}
    for fn in os.listdir(dir1):
        if  not os.path.isdir(fn) and fn.endswith('.txt'):
            with open(dir1 + '/' + fn) as f:
                words = f.read().split()

            for w in words:
                if w in word_set:
                    diz[w][0] += 1
            for p in word_set:
                if p in words:
                    diz[p][1] += 1
    return {k: tuple(v) for k, v in diz.items() if v[0]}



        
print(es35('A', {'a', 'b', 'c', 'd'}))
#{'a': (5, 3), 'c': (3, 2), 'b': (1, 1)}