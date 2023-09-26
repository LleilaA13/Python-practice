def es20(string1):
    alf='abcdefghilmnopqrstuvz'
    d={alf[i]:i+1 for i in range(len(alf))}
    string=''
    n=0
    string1=string1.lower()
    for x in string1:
        if x in d: 
            n+=d[x]
        else:
            if n !=0:
                string=string+str(n)
                string=string+' '
                n=0
    if n !=0:
        string=string+str(n)
    return string