def ex11(textfile):
    with open(textfile) as f:
        text=f.read()
    text=text.strip()
    ls_words=text.split('\n')
    for i in range(len(ls_words)):
        ls_words[i]=ls_words[i].strip()
    d=dict()
    for par in ls_words:
        ls1=[]
        for i in range(len(par)):
            if par[i] not in 'aeiou':
                ls1.append(par[i])
        ls1.sort()
        key=''.join(ls1)
        d[key]=d.get(key,[])
        d[key].append(par)
    for c in d:
        ls=d[c]
        ls=sorted(ls,key=lambda x: (-len(x),x))
        d[c]=ls
    return d
