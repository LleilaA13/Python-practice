#! /usr/bin/env python

'''Design the function ex63(word_file, triple_file) such that:
    - it receives as arguments a filename 'word_file' of a text file
    containing one string for each line, and a filename
    'triple_file' of a text file to create
    - it reads the words in word_file file and creates a new text file
    named 'triple_file'
- it returns the total number of characters present in the strings
    of  word_file file (ignoring spaces and newlines).
    The created file has the same number of lines as the read file
    (one for each word).  In the corresponding line of a string 's' in
    'word_file', 'triple_file' has a tuple (a,b,c) of integers where:
    - a is the length of 's',
    - b is the number of vowels in 's', and
    - c is the number of uppercase letters in 's'

    Example: if word_file contains the two strings 'PytHon' and
    'fonDAMenti', then the function returns 16 and writes in
    'triple_file' the following two lines:
    (6,1,2)
    (10,4,3)

'''


def ex63(word_file, triple_file):

    # inser your code here
    result = 0
    text = ''

    with open(word_file, encoding='utf8') as f:
        text = f.read()
    text = text.split()
    with open(triple_file, mode='w') as f2:
        for s in text:
            a = len(s)
            b = 0
            c = 0
            result += a
            for ch in s:
                if ch in 'aieouAIEOU':
                    b += 1
                if ch.isupper():
                    c += 1
            f2.write(f"{(a, b, c)}\n")

    return result


if __name__ == '__main__':
    print(ex63('ftesto1.txt', 'fterne1.txt'))
