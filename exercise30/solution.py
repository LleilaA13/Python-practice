

def ex3(set1, set2):
    if(len(set1) < 3):
        return []
    l1 = list(set1)
    l1.sort()
    result = []
    for i, a in enumerate(l1[:-2]):
        for b in l1[i+1:-1]:
            for c in l1[l1.index(b)+1:]:
                if(a+b+c in set2):
                    result.append(tuple([a, b, c]))
    result = sorted(result)
    return sorted(result, key=lambda t: t[0]+t[1]+t[2])
