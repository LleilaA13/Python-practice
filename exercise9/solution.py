def es8(set_in):
    ls_fin=[]
    for p in set_in:
        for p2 in set_in-{p}:
            for i in range(2,len(p)+1):
                if p[-i:]==p2[:i]:
                    ls_fin.append(p+p2[i:])
                else: continue
    ls_fin=set(ls_fin)
    ls_fin=list(ls_fin)
    ls_fin.sort()
    return ls_fin