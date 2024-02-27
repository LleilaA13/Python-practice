'''The function es55(sel,m,n,A) receives as an input:

    - a string of text containing one character 'r' or 'c'
    - two integers m and n
    - matrix A of integers (represented by a list of lists in which
      each list is a line of the matrix)

    and returns the pair (tuple) of integers with the minimum and
    maximum between the elements of the matrix. At the end, the matrix
    has to be modified in the following way:

      -if sel='r', then row m and row n of the matrix A are swapped.
      -if sel='c', then column m and column n of the matrix A are swapped.

    It can be assumed that the dimensions h and w of the matrix are
    such that m,n<=h and m,n<=w.
    
    For example: 

    - for sel='r', m=1,n=2 and A=[[2,0,-4],[5,10,20],[5,1,-1]] at the
      end of the execution of the function returns the tuple (-4,20)
      and A=[[2,0,-4],[5,1,-1],[5,10,20]]

    - for sel='c', m=0,n=1 and A=[[2,0,-4],[5,10,20],[5,1,-1]] at the
      end of the execution of the function the tuple (-4,10) will be
      returned and you will have A=[[0,2,-4],[10,5,20],[1,5,-1]].

    '''

def es55(sel,m,n,A):
  vmin = vmax = A[0][0]
  for r in A:
    for v in r:
      vmin = min(vmin, v)
      vmax = max(vmax, v)
  if m != n:
    if sel == 'r':
      A[m], A[n] = A[n], A[m]
    else:
      for r in range(len(A)):
        A[r][m], A[r][n] = A[r][n], A[r][m]
  return (vmin, vmax)

if __name__ == '__main__':
  es55('c', 0, 2, [[2, 0, -4], [5, 10, 20], [5, 1, -1]])
