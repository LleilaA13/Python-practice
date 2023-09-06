

def es62(matrix):
    imax = jmax = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] >= matrix[imax][jmax]:
                imax = i
                jmax = j
    imin = jmin = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] < matrix[imin][jmin]:
                imin = i
                jmin = j
    m1 = [[matrix[i][j]
           for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for j in range(len(matrix[0])):
        m1[imin][j] = matrix[imax][j]
        m1[imax][j] = matrix[imin][j]
    for i in range(len(matrix)):
        m1[i][jmin], m1[i][jmax] = m1[i][jmax], m1[i][jmin]
    return m1
