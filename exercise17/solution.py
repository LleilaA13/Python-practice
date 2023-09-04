def es37(dictionariesList):
    # I must keep only the keys that appear in at least N/2 dictionaries
    # so first of all I count them
    N = len(dictionariesList)
    count = {}
    # For each dictionary and for each key, I count how many times the key appears
    for d in dictionariesList:
        for k in d:
            if k in count:
                count[k] += 1
            else:
                count[k] = 1
    # once counted, I collect for each key that appears more than N/2 times
    # all values common to all dictionaries (merging of value sets)
    diz = {}
    for d in dictionariesList:
        for k, v in d.items():
            if count[k] >= N/2:
                if k in diz:
                    diz[k] = diz[k].union(v)
                else:
                    diz[k] = set(v)
    return diz
