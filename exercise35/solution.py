import json


def ex32(fname1):
    strings = []
    with open(fname1, encoding='utf8') as f:
        strings = json.load(f)
    lista = []
    for string in strings:
        even = odd = 0
        for c in string:
            if c in '13579':
                odd += ord(c)-ord('0')
            else:
                even += ord(c) - ord('0')
        lista.append((odd, even))
    return lista
