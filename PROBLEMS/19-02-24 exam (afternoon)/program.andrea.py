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
    - !!!riempire le informazioni personali nelle variabili qui sotto!!!
    - AND risolvere almeno 1 esercizio di tipo ex (problema ricorsivo)
    - AND risolvere almeno 3 esercizi di tipo func
    - AND ottenere un punteggio maggiore o uguale a 18

Il punteggio finale della prova è la somma dei punteggi dei problemi risolti.
"""
nome       = "NOM"
cognome    = "CONOME"
matricola  = "MTRICOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################

# ---------------------------- FUNC 1 ---------------------------- #

''' func1: 2 punti
Si definisca la funzione func1(lists) che prende in ingresso una lista
di liste. Ciascuna lista interna contiene degli interi. La funzione
restituisce una lista che contiene tutte gli interi che sono presenti
in tutte le liste interne. Gli interi nella lista in uscita sono
ordinati dal più grande al più piccolo.

Se lists = [[4, 4, 10, 4, 1], [4, 2, 1], [1, 4]]

allora la funzione restituisce [4, 1] in quanto 4 e 1 sono in tutte
le liste; invece 2 e 10 non sono inclusi.
Si assuma che lists non sia mai vuota.
'''
def func1(lists):
    return sorted({x for x in lists[0] if all(x in li for li in lists)}, reverse = True)


def genera_func1(N):
    from random import randint, choices, sample
    def genera_parola(L):
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        alfabeto = alfabeto + alfabeto.upper()
        return ''.join(choices(alfabeto, k=L))
    parole1 = [genera_parola(randint(1,10)) for _ in range(2*N)]
    parole2 = [genera_parola(randint(1,10)) for _ in range(2*N)]
    comuni  = {genera_parola(randint(1,10)) for _ in range(N)} - set(parole1) - set(parole2)
    list1 = parole1 + list(comuni)
    list2 = parole2 + list(comuni)
    print('list1 =', sample(list1, len(list1)))
    print('list2 =', sample(list2, len(list2)))
    print('expected =', func1(list1, list2))

#genera_func1(25)

#list1 = [ 'a', 'Bc', 'a', 'b', 'cR', 'e', 'a', 'qrt', 'st' ]
#list2 = [ 'a', 'cd', 'f', 'bC', 'cr', 'E', 'bn', 'c' ]
#print(func1(list1,list2))

#%% ---------------------------- FUNC 2 ---------------------------- #

'''
Func 2: 2 punti

Si definisca la funzione func2(text) che riceve come argomento:
- text: una stringa di testo
e che ritorna il valore del più grande numero (sequenza di digit) che si trova nel testo.

Esempio:
text = 'sOtto lA panca 1234La ca3212Pra Canta 4S5o6p7r8a LA Panca La CaPra crepa'
expected   = 3212
'''

def func2(text):
    pass
    for c in text:
        if not c.isdigit():
            text = text.replace(c, ' ')
    return max([int(x) for x in text.split()])

def genera_func2(N):
    from random import randint, choices
    alfabeto = '           abcdefghijklmnopqrstuvwxyz'
    alfabeto = alfabeto + alfabeto.upper() +'\n'
    testo = ''.join(choices(alfabeto + '0123456789'*5, k=N))
    print(f'text = """{testo}"""')
    print('expected =', func2(testo))

#genera_func2(250)

# text = 'sOtto lA panca 1234La ca3212Pra Canta 4S5o6p7r8a LA Panca La CaPra crepa'
# print(func2(text))

#%% ---------------------------- FUNC 3 ---------------------------- #
'''
Func 3: 4 punti
Definite la funzione func3(textfile_in, textfile_out) che riceve come argomento:
- textfile_in:  il percorso di un file di testo da leggere
- textfile_out: il percorso di un file di testo da creare

La funzione deve leggere il file textfile_in e scrivere nel file textfile_out.
Il file textfile_in contiene una serie di righe di testo, ciascuna delle quali
contiene una sequenza di numeri interi separati da virgole, spazi o \t.

La funzione deve scrivere nel file textfile_out una riga per ogni riga di textfile_in
contenente la differenza tra il prodotto dei numeri pari e il prodotto dei numeri dispari.
Deve inoltre ritornare la coppia (somma_pari, somma_dispari) dove somma_pari e somma_dispari
sono la somma dei numeri pari e dispari rispettivamente.

Le righe devono essere ordinate in ordine opposto all'ordine di lettura del file textfile_in.

Esempio: se il file contiene le righe
    1,    2,    17, 22
    6, -38, 71, 50,  3
    12, -8, 190,  0,  1

Il file in output deve contenere le righe
    -1
    -11613
    27

e la funzione deve tornare la coppia (somma_pari, somma_dispari) = (236, 93)
'''

def func3(textfile_in, textfile_out):
    pass
    somma_pari = somma_dispari = 0
    with open (textfile_in, mode='r', encoding='utf8') as FIN:
        with open (textfile_out, mode='w', encoding='utf8') as FOUT:
            for line in reversed(FIN.readlines()):
                prod_pari = 1
                prod_dispari = 1
                for num in line.split(','):
                    if int(num) % 2 == 0:
                        somma_pari += int(num)
                        prod_pari *= int(num)
                    else:
                        somma_dispari += int(num)
                        prod_dispari *= int(num)
                FOUT.write(f'{prod_pari - prod_dispari}\n')
    return somma_pari, somma_dispari

def genera_func3(N, file):
    from random import randint
    with open(file, mode='w', encoding='utf8') as FOUT:
        for _ in range(N):
            for _ in range(randint(10,100)):
                FOUT.write(f'{randint(-100,100)}, ')
            FOUT.write(f'{randint(-100,100)}\n')

# genera_func3(50, 'func3/in_4.txt')
# print(func3('func3/in_4.txt', 'func3/your_output_4.txt'))

#%% ---------------------------- FUNC 4 ---------------------------- #

'''
Func 4: 4 punti
Si definisca la funzione func5(filein) che riceve come argomento
- filein: un file di testo contenente una matrice quadrata di interi NxN
  separati da spazi
e che ritorna la differenza tra il prodotto degli elementi delle due diagonali
e la somma degli elementi che non sono sulle diagonali.

Esempio:
se il file filein contiene la matrice 
17 23 98
12 51 -30
0 40 17

Le due diagonali contengono rispettivamente gli elementi 17, 51, 17 e 98, 51, 0.
Gli elementi che non sono sulle diagonali sono 23, 12, -30 e 40.
Quindi la funzione deve tornare (17*51*17*98*51*0) - (23+12-30+40) = -45 

'''

def func4(input_filename):
    with open(input_filename, mode='r', encoding='utf8') as FIN:
        mat = [list(map(int, line.split())) for line in FIN]
    P = 1
    S = 0
    L = len(mat)
    for y,riga in enumerate(mat):
        for x,elem in enumerate(riga):
            if x == y or x == L-1-y:
                P *= elem
            else:
                S += elem
    return P - S

def genera_fun4(N, file):
    from random import randint
    with open(file, mode='w', encoding='utf8') as FOUT:
        for _ in range(N):
            for _ in range(N):
                FOUT.write(f'{randint(-100,100)} ')
            FOUT.write('\n')
#genera_fun4(8, 'func4/in_4.txt')

#print(func4('func4/in_1.txt'))

#%% ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 6 punti
Si definisca la funzione func5(png_input) che riceve come argomento:
- png_input:  il percorso di una inmagine PNG

Il file png_input contiene una immagine a sfondo nero, contenente stelline,
ovvero crocette di dimensione 3x3 pixel in diagonale di colori qualsiasi.
Esempio:
.x.x....
..xo.o..
.x.xo...
...o.o..
........

Nell'esempio sono presenti una stellina di colore 'x' ed una di colore 'o'.

Assumete che due qualsiasi stelline dello stesso colore siano separate da almeno un pixel
e quindi non si toccano nè in orizzontale/verticale nè in diagonale.
Assumete che i pixel della immagine siano solo stelline o sfondo nero.

La funzione deve contare il numero di stelline presenti, per ciascun colore
e tornare un dizionario che ha come chiavi i colori delle stelline presenti nell'immagine
e come valori il numero di stelline di quel colore.

Esempio:
Se l'immagine è 'func5/in_2.png' il risultato sarà il dizionario
{(150, 200, 150): 3, (200, 150, 125): 4, (125, 175, 200): 2, 
(125, 100, 125): 3, (125, 175, 125): 4, (200, 100, 150): 2}

'''

import images

def func5(png_input):
    pass
    img = images.load(png_input)
    W,H = len(img[0]), len(img)
    result = {}
    for y,row in enumerate(img):
        for x,px in enumerate(row):
            if px != (0,0,0):
                if 0<y<H-1 and 0<x<W-1:
                    if px == img[y-1][x-1] == img[y+1][x+1] == img[y-1][x+1] == img[y+1][x-1]:
                        if px not in result:
                            result[px] = 0
                        result[px] += 1
    return result

'''
................
...c.c..........
....c...........
...c.c..........
................
................
'''



def genera_func5(W,H,N, file_png):
    from random import randint, choice
    count = {}
    img = [[(0,0,0) for _ in range(W)] for _ in range(H)]
    colors = [(randint(4,8)*25, randint(4,8)*25, randint(4,8)*25) for _ in range(N//5)]
    for _ in range(N):
        x,y = randint(2,W-3), randint(2,H-3)
        c = choice(colors)
        if ((img[y][x] == img[y-1][x-1] == img[y-1][x+1] == img[y+1][x-1] == img[y+1][x+1] == (0,0,0))
            and
            not any([img[Y][X] == c for X in range(x-2,x+3) for Y in range(y-2,y+3)])):
            img[y-1][x-1] = img[y+1][x+1] = img[y-1][x+1] = img[y+1][x-1] = img[y][x] = c
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        else:
            print('non posso inserire una stellina in (',x,',',y,')')
    images.save(img, file_png)
    return count

# print(func5('func5/in_2.png'))


#%% ---------------------------- EX 1 ---------------------------- #

'''
Esercizio 1 ricorsivo (6+2 punti):

Parte 1: 6 punti
Si definisca la funzione es1(root), ricorsiva o che usa funzioni ricorsive,
che riceve in input:
- la radice 'root' di un albero n-ario definito da nodi nary_tree.NaryTree
Assumete che l'albero abbia almeno 2 nodi e che tutti i valori siano differenti.

La funzione deve trovare i due nodi di valore minimo e massimo e tornare
la coppia di percorsi che dalla radice portano a questi due nodi.
- percorso dalla radice al nodo minimo
- percorso dalla radice al nodo massimo

Esempio:
    root:                        
                              *-7*                           |
                          /           \                      |
                       *1*                2                  |
                   */*    *|*        /    |    \             |
                 *-10*    *-3*     -8    -10    -5           | 
                /  *\*     *|*      |      |                 |
               6   *-22*   *9*      7     -9                 | 

Il valore minimo è -22, il valore massimo è 9.
I percorsi da tornare sono: ([-7, 1, -10, -22], [-7, 1, -3, 9])  (evidenziati con asterischi)

ATTENZIONE: definite la funzione ricorsiva a livello esterno,
ovvero con la parola chiave 'def' appoggiata all'inizio della riga.

CONSIGLIO: spezzate il problema in funzioni piccole

Parte 2: 2 punti
La funzione, una volta trovati i due percorsi che portano ai nodi con valore minimo e massimo,
deve calcolare il percorso più breve che li collega, ovvero la lista dei valori dei nodi che
iniziano col valore minimo ed arrivano al valore massimo senza passare due volte sullo stesso nodo.

La funzione in questo caso deve restituire la terna:
- percorso dalla radice al nodo minimo
- percorso dalla radice al nodo massimo
- percorso più corto che va dal minimo al massimo

Esempio:
Nel caso precedente il valore minimo è -22, il valore massimo è 9.
Il percorso più breve che li collega e cha va ritornato è [-22, -10, 1, -3, 9].
La funzione quni dovrà tornare:
    ([-7, 1, -10, -22], [-7, 1, -3, 9], [-22, -10, 1, -3, 9])

'''

from nary_tree import NaryTree

def ex1(root : NaryTree ):
    pass
    m = minpath(root)
    M = maxpath(root)
    common_ancestor = root.value
    mm, MM = m.copy(), M.copy()
    while mm[0] == MM[0]:
        common_ancestor = mm.pop(0)
        MM.pop(0)
    short = mm[::-1] + [common_ancestor] + MM
    return m, M, short

def minpath(root):
    if root is None:
        return []
    if root.sons == []:
        return [root.value]
    return [root.value] + min([minpath(child) for child in root.sons], key=min)

def maxpath(root):
    if root is None:
        return []
    if root.sons == []:
        return [root.value]
    return [root.value] + max([maxpath(child) for child in root.sons], key=max)

def genera_ex1(N):
    from random import randint, sample
    root = NaryTree.randomTree(N)
    print('root =', root.toList())
    print('expected =', ex1(root))

#genera_ex1(10)

'''
root = NaryTree.fromList(
    [ -7,
        [1,  [-10, [6],
                   [-22]],
             [-3,  [9]]],
        [2,  [-8,  [7]],
             [-10, [-9]],
             [-5   ]],
        ])

# print(ex1(root))
'''

# %% ----------------------------------- EX.2 ----------------------------------- #


'''
Ex2: 6 points
Definite la funzione ex2(dirin, extensions), ricorsiva o che usa funzioni o metodi ricorsivi,
che riceve come argomenti:
  - dirin: il path di una directory
  - extensions: una lista di estensioni di file (stringhe)

La funzione esplora dirin e tutte le sue sottodirectory (a tutti i
livelli) e cerca tutti i file con una delle estensioni indicate.
La funzione ritorna un dizionario che ha come chiavi i path delle directory
e sottodirectory esplorate (con il separatore '/' che vale sia in Windows che Unix)
e come valori una coppia (min, max) in cui min e max sono le dimensioni
dei file con una di quelle estensioni più piccolo e più grande rispettivamente
presenti in quella directory.
Le directory che non contengono nessun file con le estensioni indicate non appaiono nel dizionario.

NOTA 1: potete usare le funzioni: os.listdir, os.path.isfile, os.path.isdir, os.path.getsize ...
NOTA 2: è proibito usare la funzione os.walk
NOTA 3: usate il carattere '/' come separatore dei path
(che funzione sia in Windows che su MacOS o Linux)

Esempio:
se il path dirin è "ex2/A" e le extensions = ["txt", "pdf", "png", "gif"]
la funzione ritorna: 
{'ex2/A': [29, 56], 'ex2/A/C': [29, 92], 'ex2/A/B': [25, 28]}
'''

import os

def ex2(dirin, extensions):
    pass
    diz = {}
    for file in os.listdir(dirin):
        file = dirin + '/' + file
        if os.path.isfile(file):
            if file.split('.')[-1] in extensions:
                S = os.path.getsize(file)
                if dirin not in diz:
                    diz[dirin] = [S, S]
                else:
                    if S < diz[dirin][0]:
                        diz[dirin][0] = S
                    if S > diz[dirin][1]:
                        diz[dirin][1] = S
        elif os.path.isdir(file):
            diz.update(ex2(file, extensions))
    return diz

#print(ex2('ex2/A', ["txt", "pdf", "png", "gif"]))
#print(ex2('ex2', ["png", "gif"]))
#print(ex2('ex2/C', ["pdf", "png"]))


######################################################################################

if __name__ == '__main__':
    # Scrivi qui i tuoi test addizionali, attenzione a non sovrascrivere
    # gli EXPECTED!
    print('*' * 50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print(
        'Altrimenii puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*' * 50)


