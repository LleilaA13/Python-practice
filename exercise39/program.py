

def es56(table):
    '''Write the function es56(table) that takes as input:

    - a table of integers (represented by list of lists in which each list is 
    a row in the table)

    and returns the list with the integers that occur the highest
    number of times in the table. The returned list must be sorted in
    ascending order. Moreover, at the end of the function, the numbers
    occurring the maximum number of times must be replaced by the
    character '*'.

    For example, if table = [[3,2,1,3],[2,1,3,5],[1,3,2,1]]
    the function returns the list [1,3] and the table becomes
    [[*,2,*,*],[2,*,5],[*,*,2,*]].

    '''
    # enter your code here
    freq = {}
    mx = 0
    for lista in table:
        for el in lista:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1
        mx = max(mx, freq[el])
    ls = [x for x in freq.keys() if freq[x] == mx]
    for lista in table:
        for i, el in enumerate(lista):
            if el in ls:
                lista[i] = '*'
    return sorted(ls)
            

if __name__ == '__main__':
    es56([[3, 2, 1, 3], [2, 1, 3, 5], [1, 3, 2, 1]])
