'''Write the function es51(ls,c) that: 

    - receives as an input a list of words ls and a character c

    - deletes from ls the words that contain the character c (both in
      upper and lower case)

    - returns the number of deleted words from ls. 

    Note that at the end of the function the list MUST be modified
    (remember that the lists are mutable).

    EXAMPLES:

    If ls=[ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio',
    'Luca', 'Ugo'] and c='a'

    the function returns 5 and the list ls becomes ['Lucio','Ugo'].  

    If ls=[ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio',
    'Luca', 'Ugo'] and c='G'] and c='G'

    the function returns 2 and the list ls becomes ['Andrea',
    'Fabio', 'Francesco', 'Lucio','Luca']
'''


def es51(ls, c):

    count = 0
    for word in ls:
        if c.lower() in word.lower():
            count += 1
    lr = [word for word in ls if c.lower() not in word.lower()]
    ls[:] = lr
    return count


if __name__ == '__main__':
    es51(['Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca', 'Ugo'],
        'f')
