import os

def ex9(pathDir):
    ls1 = scan_dir(pathDir)
    ls1 = [pathDir]
    ls_fin = []
    for el in ls1:
        space = 0
        for perc in os.listdir(el):
            p = el + '/' + perc
            if os.path.isfile(p):
                if p[-4:] == '.txt':
                    space +=  os.getsize(p)
        ls_fin.append((os.path.basename(p), space))
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