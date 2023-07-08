def ex30(fname1,fname2,fname3):
    mapping = {}
    with open(fname2, encoding='utf8') as f:
        for line in f:
            c, n = line.split()
            mapping[n] = c
    text =''
    with open(fname1,encoding='utf8') as f:
        text = f.read()
    text1 = ''
    counter = 0
    i = 0
    while i < len(text):
        c = text[i]
        if c in '0123456789':
            k = text[i:i+3]
            i += 3
            if k in mapping:
                text1 += mapping[k]
            else:
                text1 += '?'
                counter += 1
        else:
            i += 1
            text1 += c
    with open(fname3, mode='w',encoding='utf8') as f:
        f.write(text1)
    return counter
