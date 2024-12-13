#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è la somma dei punteggi dei problemi risolti.

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False
"""
nome       = "1NOME"
cognome    = "1COGNOME"
matricola  = "1MATRICOLA"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(D1 : dict[str, int], D2 : dict[str, int]) -> dict[int, str]
che riceve come argomenti due dizionari D1 e D2 con chiavi stringhe e valori interi
e che torna come risultato un dizioneario con chiavi intere e valori stringhe.

Il dizionario da ritornare deve contenere come chiavi tutti gli interi che appartengono
a chiavi che non sono comuni tra D1 e D2, e come valori la concatenazione delle chiavi
di D1 o D2 che hanno quel valore.
Le chiavi da concatenare (se sono più di una) devono essere ordinate 
in ordine di lunghezza decrescente ed, in caso di parità, in ordine alfabetico crescente. 

Esempio:
D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 4}
D2 = {'bb': 4, 'ee': 4, 'ff': 1, 'ggg': 1}

Risultato: {1: 'gggaaccff', 4: 'dddee'}
'''
def func1(D1 : dict[str, int], D2 : dict[str, int]) -> dict[int, str]:
    ## Scrivi qui il tuo codice
    non_comuni = set(D1.keys()) ^ set(D2.keys())
    D = {}
    for chiave in non_comuni:
        if chiave in D1:
            V = D1[chiave]
            D[V] = D.get(V, []) + [chiave]
        else:
            V = D2[chiave]
            D[V] = D.get(V, []) + [chiave]
    for k in D:
        D[k] = ''.join(sorted(D[k], key=lambda x: (-len(x), x)))
    return D

def genera_func1(N):
    import random
    import wonderwords
    comuni = wonderwords.RandomWord().random_words(N)
    K1 = wonderwords.RandomWord().random_words(N) + comuni
    K2 = wonderwords.RandomWord().random_words(N) + comuni
    random.shuffle(K1)
    random.shuffle(K2)
    D1 = {k: random.randint(1,N//3) for k in K1}
    D2 = {k: random.randint(1,N//3) for k in K2}
    expected = func1(D1, D2)
    print(f"""
    D1 = {D1}
    D2 = {D2}
    expected = {expected}
    """)

#genera_func1(20)

# Esempio di test
#D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 4}
#D2 = {'bb': 4, 'ee': 4, 'ff': 1, 'ggg': 1}
#print(func1(D1, D2))  # {1: 'gggaaccff', 4: 'dddee'}

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(testo: str, n: int) -> list[str]
che riceve come argomenti 
- una stringa 'testo' comnposta da parole separate da spazi, tab e accapo
- un intero 'n' 
e che torna come risultato la lista di parole del testo che hanno almeno n caratteri, 
ordinate in ordine opposto a quello di apparizione nel testo.

Esempio:
testo = 'la rana in Spagna gracida in campagna'
n = 3
Risultato = ['campagna', 'gracida', 'Spagna', 'rana']
'''
def func2(testo: str, n: int) -> list[str]:
    ## Scrivi qui il tuo codice
    parole = testo.split()
    return [parola for parola in reversed(parole) if len(parola) >= n]

# Esempio di test:
#testo = 'la rana in Spagna gracida in campagna'
#n = 3
#print(func2(testo, n))  # ['campagna', 'gracida', 'Spagna', 'rana']

def genera_func2(N):
    import random
    import wonderwords
    parole = wonderwords.RandomWord().random_words(N)
    spazi = '         \t \n'
    testo = ''.join(random.choices(spazi, k=N//5))
    for p in parole:
        testo += p + ''.join(random.choices(spazi, k=N//5))
    n = random.randint(1, N//2)
    print(f'''
    testo = """{testo}"""
    n = {n}
    expected = {func2(testo, n)}
    ''')

#genera_func2(30)


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(S1 : set[str], S2 : set[str]) -> dict[str,list[str]]
che riceve come argomenti due insiemi di stringhe S1 e S2 e che torna come risultato
un dizionario che come chiavi ha le stringhe di S1 che sono prefissi di almeno una stringa di S2
e come valori la lista di stringhe di S2 che hanno quel prefisso.
Le liste associate a ciascuna chiave devono essere ordinate in ordine decrescente
di lunghezza e, in caso di parità, in ordine alfabetico crescente.

Esempio:
S1 = {'a', 'b', 'c'}
S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
Risultato = {'a': ['abc', 'aa', 'ab'], 'c': ['cc', 'cd'], 'b': ['bb', 'bc']}
'''

def func3(S1 : set[str], S2 : set[str]) -> dict[str,list[str]]:
    ## Scrivi qui il tuo codice
    D = {}
    for prefisso in S1:
        stringhe =[stringa for stringa in S2 if stringa.startswith(prefisso) ]
        if stringhe:
            D[prefisso] = stringhe
            D[prefisso].sort(key=lambda x: (-len(x), x))
    return D

# Esempio di test
#S1 = {'a', 'b', 'c'}
#S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
#print(func3(S1, S2))  # {'a': ['abc', 'aa', 'ab'], 'c': ['cc', 'cd'], 'b': ['bb', 'bc']}

def genera_func3(N):
    import random
    import wonderwords
    parole = set(wonderwords.RandomWord().random_words(N))
    altre  = set(wonderwords.RandomWord().random_words(N))
    altre2 = set(wonderwords.RandomWord().random_words(N))
    prefissi = set([p[:random.randint(1, len(p)//2)] for p in parole])
    altri    = set([p[:random.randint(1, len(p)//2)] for p in altre2])
    S1 = prefissi | altri
    S2 = parole | altre
    print(f'''
    S1 = {S1}
    S2 = {S2}
    expected = {func3(S1, S2)}
    ''')

#genera_func3(15)


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 8 punti
Si definisca la funzione func4(file_png: str, N: int) -> int
che riceve come argomenti 
- il nome di un file PNG che contiene una immagine a sfondo nero in cui sono rpesenti dei 
    quadrati colorati disgiunti e di dimensioni almeno 3x3 di pixel
- un intero N che indica quale dimensione di quadrati dovete cercare
e che torna come risultato un dizionario che ha come chiavi i colori dei quadrati
e come valori il numero di quadrati di quel colore, con dimensioni NxN
presenti nella immagine.

Esempio:
Se l'immagine è "func4/1.png" ed N=5, allora il dizionario da tornare è:
{(125, 190, 250): 1, (184, 100, 249): 2, (115, 186, 199): 1, (139, 150, 176): 1, (250, 240, 236): 1, (125, 157, 232): 1}
"""

import images
def func4(file_png: str, N: int) -> dict[tuple[int,int,int], int]:
    img = images.load(file_png)
    D = {}
    for y,riga in enumerate(img):
        for x,pixel in enumerate(riga):
            if pixel != (0,0,0) and is_quadrato(img, x, y, N, pixel):
                #print("quadrato", pixel, x, y)
                D[pixel] = D.get(pixel, 0) + 1
    return D

def is_quadrato(img, x, y, N, colore):
    try:
        for X in range(x,x+N):
            if img[y][X] != colore:
                return False
            if img[y+N-1][X] != colore:
                return False
        for Y in range(y, y + N):
            if img[Y][x] != colore:
                return False
            if img[Y][x+N-1] != colore:
                return False
    except IndexError:
        return False
    return True

def is_free(img, x, y, N):
    b = 0,0,0
    try:
        for X in range(x,x+N):
            if img[y][X] != b:
                return False
            if img[y+N-1][X] != b:
                return False
        for Y in range(y, y + N):
            if img[Y][x] != b:
                return False
            if img[Y][x+N-1] != b:
                return False
    except IndexError:
        return False
    return True

def genera_func4(W,H, N):
    from random import randint
    img = [[(0,0,0) for _ in range(W)] for _ in range(H)]
    colori = [(randint(100,255), randint(100,255), randint(100,255)) for _ in range(10)]
    for _ in range(N):
        L = randint(2,10)
        x = randint(0,W-L)
        y = randint(0,H-L)
        colore = colori[randint(0,9)]
        if is_free(img, x, y, L):
            for X in range(x, x + L):
                img[y][X]           = colore
                img[y + L - 1][X]   = colore
            for Y in range(y, y + L):
                img[Y][x]           = colore
                img[Y][x + L - 1]   = colore
    images.save(img, 'func4/3.png')

#genera_func4(500,200, 1000)
#Esempio di test
#print(func4('func4/1.png', 2))  # {(207, 169, 159): 1, (236, 116, 211): 1, (139, 150, 176): 1, (250, 240, 236): 5}

# %% ----------------------------------- FUNC5 ------------------------- #

""" func5: 4 punti 
Si definisca la funzione func5(file_txt: str, K: int, P: int) -> list[list[int]] 
che riceve come argomenti:
- file_txt: il nome di un file txt contenente una matrice NxM di interi separati da spazi, su righe separate
- K ed P, due interi 
e che torna come risultato la matrice letta dal file, rappresentata come lista di liste di interi
in cui tutti i valori multipli di K sono stati moltiplicati per P, e gli altri sono i valori originali

Esempio:
se la matrice letta dal file è la seguente:
1 2 3
4 5 6
7 8 9
10 11 12
ed i valori di K=3 e M=10, allora la matrice da tornare è:
[[1, 2, 30],
 [4, 5, 60],
 [7, 8, 90],
 [10, 11, 120]]
"""

def func5(file_txt: str, K: int, M: int) -> list[list[int]]:
    ## Scrivi qui il tuo codice
    with open(file_txt) as f:
        matrice = [[int(x) for x in riga.split()] for riga in f]
    for y,riga in enumerate(matrice):
        for x, V in enumerate(riga):
            if V % K == 0:
                matrice[y][x] *= M
    return matrice

# Esempio di test
#file_txt = 'func5/1.txt'
#K = 3
#M = 10
#print(func5(file_txt, K, M))  # [[1, 2, 30], [4, 5, 60], [7, 8, 90]]

def genera_func5(N):
    import random
    ID = 4
    M = random.randint(N//2,N*2)
    with open(f'func5/{ID}.txt', 'w') as f:
        for _ in range(N):
            f.write(' '.join(str(random.randint(1,1000)) for _ in range(M)) + '\n')
    K = random.randint(2,N*2)
    P = random.randint(2,N*2)
    print(f'''
    file_txt = 'func5/{ID}.txt'
    K = {K}
    P = {P}
    expected = {func5(f'func5/{ID}.txt', K, P)}
    ''')

#genera_func5(15)

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si definisca la funzione ex1(dirname, necessary, forbidden), ricorsiva o che utilizza funzioni 
o metodi ricorsivi, che riceve come argomenti:
 - dirname: il nome di una directory in cui cercare dei file
 - necessary: una lista di parole che devono essere presenti nei file trovati
 - forbidden: una lista di parole che devono essere assenti  nei file trovati
e che esplora la directory e tutte le sue sottodirectory per cercare i file che soddisfano le seguenti condizioni:
- hanno come estensione '.txt'
- contengono tutte le parole presenti in 'necessary'
- non contengono nessuna delle parole presenti in 'forbidden'

La funzione ritorna come risultato la lista di percorsi dei file trovati, 
ordinati in ordine di profondità crescente, e in caso di parità in ordine alfabetico decrescente.

AVVISO 1: Si consiglia di utilizzare le funzioni os.listdir,
os.path.isfile e os.path.isdir e NON la funzione os.join in
Windows. Utilizzare la concatenazione tra stringhe con il carattere '/'.

AVVISO 2: è vietato utilizzare la funzione os.walk

Esempio:
dirname = 'ex1/AAA'
necessary: ['ciao', 'mamma']
forbidden: ['papa', 'nonno']

Risultato: ['ex1/AAA/share/recollection/lamentable/dogsled.txt', 'ex1/AAA/heavy/tomorrow/flare/cellar.txt', 
            'ex1/AAA/heavy/spoon/cranberry.txt', 'ex1/AAA/heavy/roster/prosecutor.txt', 'ex1/AAA/gifted/systemize/due.txt', 
            'ex1/AAA/gifted/systemize/distinction.txt', 'ex1/AAA/share/help.txt', 'ex1/AAA/regime.txt', 'ex1/AAA/mayonnaise.txt']


"""
import os

def ex1(dirname: str, necessary: list[str], forbidden: list[str]) -> list[str]:
    L = []
    _esplora_dir(dirname, necessary, forbidden, L)
    L.sort(key=lambda x: (x.count('/'), x), reverse=True)
    return L

def is_good(filepath, necessary, forbidden):
    with open(filepath) as f:
        parole = f.read().split()
    return set(necessary).issubset(parole) and not set(forbidden).intersection(parole)

def _esplora_dir(dirname, necessary, forbidden, L):
    for nome in os.listdir(dirname):
        path = dirname + '/' + nome
        if os.path.isdir(path):
            _esplora_dir(path, necessary, forbidden, L)
        elif path.endswith('.txt') and is_good(path, necessary, forbidden):
            L.append(path)

def genera_ex1(dirname, N, necessary=None, forbidden=None):
    import wonderwords, random
    os.makedirs(dirname, exist_ok=True)
    extensions = ['txt', 'txt', 'txt', 'ttx', 'xtt']
    if necessary is None:
        necessary = wonderwords.RandomWord().random_words(N)
        print('necessary=', necessary)
    if forbidden is None:
        forbidden = wonderwords.RandomWord().random_words(N)
        print('forbidden=', forbidden)
    if N:
        names = wonderwords.RandomWord().random_words(2*N)
        for name in names:
            fullname = dirname + '/' + name
            if random.randint(1,100) < 50:
                genera_ex1(fullname, N-1, necessary, forbidden)
            else:
                filename = fullname + '.' + random.choice(extensions)
                other = wonderwords.RandomWord().random_words(200)
                X = random.randint(1,100)
                if X < 30:
                    words = necessary + other
                elif X < 60:
                    words = forbidden + other
                else:
                    words = necessary + forbidden + other
                random.shuffle(words)
                with open(filename, 'w') as f:
                    f.write(' '.join(words))

'''
# Esempio di test
dirname = 'ex1/AAA'
necessary = ['ciao', 'mamma']
forbidden = ['papa', 'nonno']
print(ex1(dirname, necessary, forbidden))
# ['ex1/AAA/share/recollection/lamentable/dogsled.txt',
# 'ex1/AAA/heavy/tomorrow/flare/cellar.txt',
# 'ex1/AAA/heavy/spoon/cranberry.txt',
# 'ex1/AAA/heavy/roster/prosecutor.txt',
# 'ex1/AAA/gifted/systemize/due.txt',
# 'ex1/AAA/gifted/systemize/distinction.txt',
# 'ex1/AAA/share/help.txt',
# 'ex1/AAA/regime.txt',
# 'ex1/AAA/mayonnaise.txt']
'''
# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root), ricorsiva o che utilizza funzioni
o metodi ricorsivi, che riceve come argomento la radice di un albero
binario formato da nodi di tipo tree.BinaryTree.
La funzione deve modificare distruttivamente l'albero scambiando tra di loro
i due figli di ogni nodo che si trova a profondità pari 
(considerando che la radice sia a profondità 0).
La funzione deve tornare come risultato il numero di nodi spostati.

Esempio:
Se l'albero è il seguente:
                    | profondità
         1          |  0
        / \         |
       2   3        |  1
      / \ / \       |
     4  5 6  7      |  2
    / \    \        |
   8   9   10       |  3
Diventerà:
                    | profondità
         1          |  0   2 figli spostati
        / \         |
       3   2        |  1    
      / \ / \       |
     6  7 4  5      |  2   3 figli spostati
    /    / \        |
   10   9   8       |  3   
e la funzione ritorna il numero di nodi spostati: 5
"""

import tree

def ex2(root):
    ## Scrivi qui il tuo codice
    pass
    return _ex2(root, 0)

def _ex2(nodo, profondità):
    if nodo is None:
        return 0
    quanti = 0
    if profondità % 2 == 0:   # profondità pari del nodo padre  => scambio i figli
        nodo.left, nodo.right = nodo.right, nodo.left
        if nodo.left  is not None: quanti += 1
        if nodo.right is not None: quanti += 1
    return quanti + _ex2(nodo.left, profondità+1) + _ex2(nodo.right, profondità+1)

# Esempio di test
'''
root = tree.BinaryTree.fromList([1, [2, [4, [8, None, None],
                                            [9, None, None]],
                                        [5, None, None]],
                                    [3, [6, None,
                                            [10, None, None]],
                                        [7, None, None]]])
toor = tree.BinaryTree.fromList([1, [3, [6, [10, None, None],
                                            None],
                                        [7, None, None]],
                                    [2, [4, [9, None, None],
                                            [8, None, None]],
                                        [5, None, None]]])
print(ex2(root))  # 5
print(root == toor)  # True
'''

def genera_ex2(N):
    root = tree.BinaryTree.randomTree(N)
    root_as_list = root.toList()
    res = ex2(root)
    toor_as_list = root.toList()
    print(f'''
    root_as_list     = {root_as_list}
    expected_as_list = {toor_as_list}
    expected = {res}
    ''')

#genera_ex2(15)

# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
