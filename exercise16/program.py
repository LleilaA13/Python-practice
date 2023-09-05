'''Implement the function es36(dictionariesList) that takes as an
input a list of dictionaries and returns a dictionary.

The input dictionaries in the dictionariesList have character
strings between 'a' and 'z' as key and lists of integers as
attributes.

The keys in the output dictionary are the keys common to all the
dictionaries in dictionariesList.  Each x key of the output
dictionary is associated with a list of integers.  An integer is
present in the list of a key x if and only if it is present in the
attribute list of key x for all the dictionaries of
dictionariesList.  The list is also sorted in ascending order.

For example:
- if the dictionariesList contains the three dictionaries
{'a': [1,3,5],'b':[2,3 ],'d':[3]},
{'a':[5,1,2,3], 'b':[2],'d':[3]},
{'a':[3,5], 'c':[4,1,2],'d':[4]}
- the returned dictionary is
{'a':[3,5],'d':[]}

'''


def es36(dictionariesList):
    diz = {}
    keys = []
    for d in dictionariesList:
        keys.append(set(d.keys()))
        
    inter_keys = keys[0]
    for k in keys[1:]:
        inter_keys = inter_keys.intersection(k)
        
    for k in inter_keys:
        vals = []
        for d in dictionariesList:
            vals.append(set(d[k]))
        inter_val = vals[0]
        for v in vals[1:]:
            inter_val = inter_val.intersection(v)
        diz[k] = sorted(list(inter_val))
    return diz
        




if __name__ == '__main__':
    print(es36([{'a': [1, 3, 5], 'b': [2, 3], 'd': [3]}, {'a': [5, 1, 2, 3], 'b': [2], 'd': [3]},
                {'a': [3, 5], 'c': [4, 1, 2], 'd': [4]}]))

'''


'''