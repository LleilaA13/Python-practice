def es31(fname1, fname2):
    text = ''
    with open(fname1, encoding='utf8') as f:
        text = f.read()
    word_list = text.split()
    count = {chr(ord('a')+c): 0 for c in range(26)}
    for word in word_list:
        chars = set(word)
        for c in chars:
            if 'a' <= c <= 'z':
                count[c] += 1
    howMany = 0
    for c, v in count.items():
        if v % 2:
            howMany += 1
            text = text.replace(c, c.upper())
    with open(fname2, mode='w', encoding='utf8') as f:
        f.write(text)
    return howMany
