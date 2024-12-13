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
nome       = "OME"
cognome    = "CGNOME"
matricola  = "MARICOLA"

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

'''
Func 1: 2 punti
Si definisca la funzione func1(diz1, diz2) che riceve come argomento:
- list1: una lista di parole (stringhe)
- list2: una lista di parole (stringhe)
e che torna come risultato un dizionario che ha come chiavi degli interi 
e come valori degli insiemi di parole (stringhe) che sono presenti in entrambe le liste
senza distinzione tra minuscole e maiuscole.
Le chiavi del dizionario devono essere le lunghezze delle parole comuni.
I valori associati a ciascuna chiave sono tutte le parole di list1 e list2 comuni
senza distinzioni tra minuscole e maiuscole con la stessa lunghezza.

Esempio:
list1: [ 'a', 'Bc', 'a', 'b', 'cR', 'e', 'a', 'qrt', 'st' ]
list2: [ 'a', 'cd', 'f', 'bC', 'cr', 'E', 'bn', 'c' ]
il risultato sarà  {1: {'e', 'E', 'a'}, 2: {'Bc', 'bC', 'cR', 'cr'}}
'''

def func1(list1, list2):
    d1 = {s.lower():s for s in list1}
    d2 = {s.lower():s for s in list2}
    d = {}
    for w in set(d1)&set(d2):
        if len(w) not in d:
            d[len(w)] = set()
        s = d.get(len(w))
        s.add(d1[w])
        s.add(d2[w])
    return d

list1 = [ 'a', 'Bc', 'a', 'b', 'cR', 'e', 'a', 'qrt', 'st' ]
list2 = [ 'a', 'cd', 'f', 'bC', 'cr', 'E', 'bn', 'c' ]
print(func1(list1, list2))

#%% ---------------------------- FUNC 2 ---------------------------- #

'''
Func 2: 2 points

Define the func2(text) function that receives as an argument:
- text: a text string
and which returns the value of the largest number (sequence of digits) found in the text.

Example:
text = 'under the bench 1234The go3212At SinGs 4S5oV6e7r8t HE BeNcH tHe gOaT dIES'
expected = 3212
'''

def func2(text):
    t = ''
    for c in text:
        t += c if c.isdigit() else ' '
    return max([int(w) for w in t.split()])

text = 'under the bench 1234The go3212At SinGs 4S5oV6e7r8t HE BeNcH tHe gOaT dIES'
print(func2(text))

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

def prod (l):
    i = 1
    for n in l:
        i*=n
    return i

def func3(textfile_in, textfile_out):
    righe = []    
    somma_pari = somma_dispari = 0
    with open(textfile_in) as f:
        for l in f:
            l = l.replace(',',' ')
            numeri = list(map(int, l.split()))
            pari = [n for n in numeri if n%2==0]
            dispari = [n for n in numeri if n%2]
            righe.append(prod(pari) - prod(dispari))
            somma_pari+=sum(pari)
            somma_dispari+=sum(dispari)
    with open(textfile_out, 'w', encoding='utf8') as g:
        for riga in reversed(righe):
            print(riga, file=g) 
    return somma_pari, somma_dispari
print(func3('func3/in_4.txt', 'func3/your_output_4.txt'))

#%% ---------------------------- FUNC 4 ---------------------------- #
def prod (l):
    i = 1
    for n in l:
        i*=n
    return i
'''
Func 4: 4 punti
Si definisca la funzione func4(filein) che riceve come argomento
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
    m = []
    with open(input_filename) as f:
        for line in f:
            m.append(list(map(int, line.split())))
    print([m[i][i] for i in range(len(m))]+[m[i][len(m)-i-1] for i in range(len(m))])
    print(prod([m[i][i] for i in range(len(m))]+[m[i][len(m)-i-1] for i in range(len(m))]))
    a = prod([m[i][i] for i in range(len(m))]+[m[i][len(m)-i-1] for i in range(len(m))])
    b = 0
    for i in range(len(m)):
        for j in range(len(m)):
            if i==j or i == len(m)-j-1:
                continue
            b += m[i][j]
    print(a, b)
    return a-b

print(func4('func4/in_3.txt'))

#%% ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 6 punti
Si definisca la funzione func5(png_input) che riceve come argomento:
- png_input:  il percorso di una immagine PNG

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
def segui(r,c, imm):
    nero = (0,0,0)
    colore = imm[r][c]
    imm[r][c] = nero
    imm[r+2][c] = nero
    imm[r+2][c+2] = nero
    imm[r][c+2] = nero
    imm[r+1][c+1] = nero
    return colore

def func5(png_input):
    imm = images.load(png_input)
    stelle = {}
    conta = 0
    for r, riga in enumerate(imm):
        for c, pixel in enumerate(riga):
            if pixel != (0,0,0):
                colore = segui(r,c,imm)
                stelle[colore] = stelle.get(colore, 0) + 1
                conta+=1
                images.save(imm, f'test{conta}.png')
    return stelle

print(func5('func5/in_2.png'))


#%% ---------------------------- EX 1 ---------------------------- #

'''
Esercizio 1 ricorsivo (6+2 punti):

Parte 1: 6 punti
Si definisca la funzione es1(root), ricorsiva o che usa funzioni ricorsive,
che riceve in input:
- la radice 'root' di un albero n-ario definito da nodi nary_tree.NaryTree
Assumete che l'albero abbia almeno 2 nodi e che il minimo e massimo valore siano unici e differenti.

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


def ex1_min(root):
    if root.sons == []:
        return [root.value]
    m = root.value
    minpath = [root.value]
    for son in root.sons:
        path = ex1_min(son)
        if min(path) < m:
            m = min(path)
            minpath = [root.value] + path
    return minpath

def ex1_max(root):
    if root.sons == []:
        return [root.value]
    m = root.value
    maxpath = [root.value]
    for son in root.sons:
        path = ex1_max(son)
        if max(path) > m:
            m = max(path)
            maxpath = [root.value] + path
    return maxpath

def ex1(root : NaryTree ):
    min_path = ex1_min(root)
    max_path = ex1_max(root)
    i = 0
    while min_path[i] == max_path[i]:
        i+=1
    return min_path, max_path, min_path[-1:i-1:-1]+max_path[i-1:]
    

# root = NaryTree.fromList(
#     [ -7,
#         [1,  [-10, [6],
#                     [-22]],
#               [-3,  [9]]],
#         [2,  [-8,  [7]],
#               [-10, [-9]],
#               [-5   ]],
#         ])

# print(ex1(root))


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
    d = {}
    sizes = []
    for f in os.listdir(dirin):
        fn = dirin+'/'+f
        if os.path.isfile(fn) and any(fn.endswith(e) for e in extensions):
            sizes.append(os.path.getsize(fn))
        elif os.path.isdir(fn):
            d.update(ex2(fn, extensions))
    if len(sizes)>0:
        d[dirin] = [min(sizes), max(sizes)]
    return d


print(ex2('ex2/A', ["txt", "pdf", "png", "gif"]))
print(ex2('ex2', ["png", "gif"]))
print(ex2('ex2/C', ["pdf", "png"]))


######################################################################################

if __name__ == '__main__':
    # Scrivi qui i tuoi test addizionali, attenzione a non sovrascrivere
    # gli EXPECTED!
    print('*' * 50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print(
        'Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*' * 50)


