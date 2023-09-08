def ex63(word_file, triple_file):
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
    # inser your code here


