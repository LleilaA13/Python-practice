'''Design function es21(matrix) that takes as input a matrix of
     characters represented by a list of character lists and returns a
     new matrix where the columns of the input matrix are
     alphabetically ordered. At the end of the function, the input
     matrix should not be modified.

     For example, if the input matrix is
     [['q','s','g','g'],
      ['b','a','m','f'],
      ['a','b','n','z']] 

    the function will return the matrix:
     [['a','a','g','f'],
      ['b','b','m','g'],
      ['q','s','n','z']]

'''


def es21(matrix):
    #empty matrix and then we fill it, crearla intanto:
    m = [[] for i in range(len(matrix))]
    for j in range(len(matrix[0])):
        cols = []
        for i in range(len(matrix)):
            cols += [matrix[i][j]]
        cols.sort()
        for i in range(len(matrix)):
            m[i] += cols[i]
    return m

print(es21([['q','s','g','g'],['b','a','m','f'],['a','b','n','z']]))