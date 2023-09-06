def es50(s,k):
    my_set={ s[i:i+k] for i in range(len(s)-k+1) if ascending(s[i:i+k])}
    return sorted(list(my_set),reverse=True)

def ascending(string):
    for i in range(len(string)-1):
        if string[i]>=string[i+1]:return False
    return True
