import os
'''Define a function ex9(pathDir) such that:
    - it is recursive or uses recursive functions(s)/method(s);
    - it receives the pathname 'pathDir'of a directory as argument;
    - it returns a list of pairs (tuple with two elements). Each tuple
        contains the name of a subdirectory that can be reached from
        'pathDir' and the total amount of bytes of all the files with
        extension .txt is that subdirectory.
    The list are sorted in descending order with respect to their
    second component (the amount of bytes of the .txt files) and, in
    case of tie, in alphabetical order with respect to the first
    component (the name of the subdirectory).  Files and directories
    whose name begins with the '.'  character should not be
    considered.

    For the purposes of the exercise, the following may be useful the
    following functions in the os module: os.listdir(),
    os.path.isfile(), os.path.isdir(), os.path.basename(),
    os.path.getsize()

    Example: with es9('Informatica/Software') it is returned the list:
    [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

'''

def ex9(pathDir):
    ls1 = scan_dir(pathDir)
    ls1 += [pathDir]
    ls_fin = []
    for el in ls1:
        size = 0
        for pc in os.listdir(el):
            p = el + '/' + pc
            if os.path.isfile(p):
                if p[-4:] == '.txt':
                    size += os.path.getsize(p)
        ls_fin.append((os.path.basename(el), size))
    ls_fin = sorted(ls_fin, key = lambda x : (-x[1], x[0]))
    return ls_fin

def scan_dir(path):
    if os.path.isfile(path):
        return []
    ls = []
    for el in os.listdir(path):
        p = path + '/' + el
        ls = ls + scan_dir(p)
        if os.path.isdir(p):
            ls += [p]
    return ls