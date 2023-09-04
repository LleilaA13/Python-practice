'''Write the function es37(dictionariesList) that takes as an input a
list of dictionaries and returns a dictionary.

The input dictionaries in dictionariesList have character strings
between 'a' and 'z' as keys and lists of integers as attributes.

The output dictionary has as keys the keys common to at least half
of the dictionaries of the input list.  Each x key of this output
dictionary is associated with a set.  An integer is present in the
set with key x if and only if it is present in the attribute list
of key x for at least one dictionary in dictionariesList.

For example:
- if dictionariesList contains the three dictionaries
{'a': [1,3,5],'b':[2,3 ],'d':[3]},
{'a':[5,1,2,3], 'b':[2],'d':[3]},
{'a':[3,5], 'c':[4,1,2],'d':[4]}
the returned dictionary will be
{'a':{1,2,3,5},'b':{2,3},'d':{3,4}}

'''

def es37(dictionariesList):

    N = len(dictionariesList)
    count = {}
    
    for d in dictionariesList:
        for k in d:
            if k in count:
                count[k] += 1
            else:
                count[k] = 1
                
    diz = {}
    for d in dictionariesList:
        for k, v in d.items():
            if count[k] >= N/2:
                if k in diz:
                    diz[k] = diz[k].union(v)
                else:
                    diz[k] = set(v)
    return diz
    

if __name__ == '__main__':
    print(es37([{'a': [1, 3, 5], 'b':[2, 3], 'd':[3]}, {'a': [5, 1, 2, 3], 'b':[2], 'd':[3]}, {
        'a': [3, 5], 'c':[4, 1, 2], 'd':[4]}]))










