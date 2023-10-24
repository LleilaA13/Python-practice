'''Design and implement the function es31(fname1,fname2) which takes
    as input the address of two text files.
    The function modifies the text of fname1 file as follows:
    - each character between 'a' and 'z' (lowercase) that appears in
    the file in an odd number of words (a word is a maximal sequence
    of characters other than space, tab or new line character) is
    replaced by the corresponding uppercase character.
    The function saves the modified text a new file with path fname2.
    The function returns how many of the 26 characters between 'a' and
    'z' have been modified from lowercase to uppercase in the text.
    For example if:
    - the fname1 file contains the text 'Monti, Sterbini e Spognardi'
    - the fname2 file will contain the text 'MoNtI, SterBINI e SPoGNArDI'
    and the function will return the value 7, since the changed
    letters are NIBPGAD.

    '''
def es31(fname1,fname2):
    with open(fname1, encoding = 'utf8') as f:
        text = f.read()
    lista = text.split()
    alfa = 'abcdefghijklmnopqrstuvwxyz'
    count = {k:0 for k in alfa}
    for word in lista:
        chars = set(word)
        for c in chars:
            if 'a' <= c <= 'z':
                count[c] += 1
    counter = 0
    for k,v in count.items():
        if v % 2 != 0:
            counter += 1
            text = text.replace(k, k.upper())
    with open(fname2, mode = 'w', encoding='utf8') as f:
        f.write(text)
    return counter


        




print(es31('ftesto3.txt', 'risposta3.txt'))














 
