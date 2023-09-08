
def ex43(textfile):
    '''Design a function es43(textfile) such that
    - it receives as arguments the address of a text file 'textfile' that 
      contains lines with integers separated by spaces
    - it returns a list of integers.
    The length of the list is given by the maximum number of integers
    that appear in a row of 'textfile'. In the generic position i of
    the list there is the sum of all the integers at position i in all
    the lines with at least i integers.
    For example, if the file contains the 3 lines:
    ' 0 2 4
      6 8 10
      4 0 1'
    the function returns the list [10,10,15] i.e. the sums in column
    if the file contains the 4 lines (with different lengths):
    ' 1 2 3
      4 5 6 7 3 6
      1
      1 2'
    the function returns the list [7,9,9,7,3,6].

    '''
    # insert your code here

    matrix = []
    max_len = 0
    result = []

    with open(textfile, mode='r', encoding='utf8') as f:
        for line in f:
            integers = [int(num) for num in line.split()]
            matrix.append(integers)
    for lista in matrix:
        if len(lista) > max_len:
            max_len = len(lista)

    for lista in matrix:
        for i in range(max_len):
          if len(lista) < max_len:
            lista.append(0)
            
    num_row = len(matrix)
    num_col = len(matrix[0])
    
    for col in range(num_col):
      sum = 0
      for row in range(num_row):
        sum += matrix[row][col]
        if row + 1 == num_row:
          result.append(sum)
    return result

