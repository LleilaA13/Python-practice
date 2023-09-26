def es21(matrix):
    matrix1 = [[] for i in range(len(matrix))]
    for j in range(len(matrix[0])):
        column = []
        for i in range(len(matrix)):
            column += [matrix[i][j]]
        column.sort()
        for i in range(len(matrix)):
            matrix1[i] += [column[i]]
    return matrix1
