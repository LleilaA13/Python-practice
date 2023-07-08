import copy


def ex54(mylist):
    diz = {}
    for v in copy.copy(mylist):
        if isinstance(v, str):
            mylist.remove(v)
            if v in diz:
                diz[v] += 1
            else:
                diz[v] = 1
    return diz
