
def es62(matrix):
    '''
    define the function es62(matrix) that takes a matrix (list of lists) as an input
    of integers and that:
        - identifies the coordinates x1,y1 of the MINIMUM value contained in matrix
            (in case of parity take the element with x minimum
            and in case of further parity the one with minimum y)
        - identifies the coordinates x2,y2 of the MAXIMUM value contained in matrix
            (in case of parity take the element with maximum x
            and in case of further parity the one with y maximum)
        - creates a new matrix where the two rows y1 and y2 and the two columns
            x1 and x2 are swapped.

    The function must return the newly created matrix.
    The original matrix must not be modified.
    The function must be able to work even if x1==x2 and/or y1==y2.

    Examples:
             | 2  0 -4 |           | 5 10 20 |
    matrix = | 5 10 20 | result => | 2  0 -4 |
             | 5  1 -1 |           | 5  1 -1 |

             |  2  0 -4 |           | -1 1  25 |
    matrix = |  5 10 10 | result => | 10 10  5 |
             | 25  1 -1 |           | -4 0   2 |
    '''
    # enter your code here
