
'''Given a sequence S of integers, we define sequence derived from S
    the sequence of n integers where the i-th element is given by the
    sum of the first i integers of S.
    For example: the sequence derived from 
    S= 2, -3, -4, 4, 4, -5, 3, 1.-1 is
    2, -1, -5, -1, 3, -2, 1, 2, 1.
    
    Design and implement a function ex41(fname) such that:..................
    - it takes as arguments the path of a text file 'fname', where it
        is stored a sequence S of integers, separated by a comma and
        some white spaces
    - it returns the number that appears most frequently in the
        sequence derived from S. If there are several numbers with the
        highest number of repetitions, the maximum one is returned.
    Example: if the 'fname' file contains the sequence S= 2, -3, -4,
    4, -5, 3, 1, -1 the function returns the value 2.
    '''


def ex41(fname):
    with open(fname, encoding = 'utf8') as f:
        seq = [int(x) for x in f.read().split(',')]
    sum = 0
    lista = []
    for i in range(len(seq)):
        sum += seq[i]
        lista.append(sum)
    freq = {}
    for x in lista:
        if x in freq:
            freq[x] += 1
        if x not in freq:
            freq[x] = 1
    pairs = max(freq.keys(), key = lambda k:(freq[k], k))
    return pairs


if __name__ == '__main__':
    ex41('fsequenza1.txt')
