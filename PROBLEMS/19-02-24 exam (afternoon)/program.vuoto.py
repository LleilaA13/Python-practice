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
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

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

# %% ----------------------------------- FUNC1 ------------------------- #
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
    ## Scrivi qui il tuo codice
    pass

#%% ---------------------------- FUNC 2 ---------------------------- #

'''
Func 2: 2 punti

Define the func2(text) function that receives as an argument:
- text: a text string
and which returns the value of the largest number (sequence of digits) found in the text.

Example:
text = 'under the bench 1234The go3212At SinGs 4S5oV6e7r8t HE BeNcH tHe gOaT dIES'
expected = 3212
'''

def func2(text):
     pass

# text = 'under the bench 1234The go3212At SinGs 4S5oV6e7r8t HE BeNcH tHe gOaT dIES'
# print(func2(text))

#%% ---------------------------- FUNC 3 ---------------------------- #
'''
Func 3: 4 punti
Si definisca la funzione func3(textfile_in, textfile_out) che riceve come argomento:
- textfile_in:  il percorso di un file di testo da leggere
- textfile_out: il percorso di un file di testo da creare

La funzione deve leggere il file textfile_in e scrivere nel file textfile_out.
Il file textfile_in contiene una serie di righe di testo, ciascuna delle quali
contiene una sequenza di numeri interi separati da virgole, spazi o \t.

La funzione deve scrivere nel file textfile_out una riga per ogni riga di textfile_in
contenente la differenza tra il prodotto dei numeri pari e il prodotto dei numeri dispari.
Le righe devono essere ordinate in ordine opposto all'ordine di lettura del file textfile_in.
La funzione deve inoltre ritornare la coppia (somma_pari, somma_dispari) dove somma_pari e somma_dispari
sono, rispettivamente, la somma di tutti i numeri pari e dispari del file.

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

# print(func3('func3/in_4.txt', 'func3/your_output_4.txt'))

#%% ---------------------------- FUNC 4 ---------------------------- #

'''
Func 4: 4 punti
Si definisca la funzione func4(filein) che riceve come argomento
- filein: il percorso di un file di testo contenente una matrice quadrata di interi NxN
  separati da spazi
e che ritorna la differenza tra il prodotto degli elementi che si trovano 
su una delle due diagonali e la somma degli elementi che non sono sulle diagonali.
NOTA: Se la matrice è di ordine dispari l'elemento centrale va usato una sola volta.

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
    pass

#print(func4('func4/in_1.txt'))

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
e quindi non si toccano né in orizzontale/verticale né in diagonale.
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

# print(func5('func5/in_2.png'))


#%% ---------------------------- EX 1 ---------------------------- #

'''
Esercizio 1 ricorsivo (6+2 punti):

Parte 1: 6 punti
Si definisca la funzione es1(root), ricorsiva o che usa funzioni ricorsive,
che riceve in input:
- la radice 'root' di un albero n-ario definito da nodi nary_tree.NaryTree
Assumete che l'albero abbia almeno 2 nodi e che il minimo e massimo valore
siano unici e differenti.

La funzione deve trovare i due nodi di valore minimo e massimo e tornare
la coppia di percorsi che dalla radice portano a questi due nodi, ovvero
- percorso dalla radice al nodo minimo
- percorso dalla radice al nodo massimo.
Un percorso è rappresentato dalla lista dei valori dei nodi attraversati.

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

def ex1(root): # root e' di tipo NaryTree 
    pass

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
Ex2: 6 punti
Si definisca la funzione ex2(dirin, extensions), ricorsiva o che usa funzioni o metodi ricorsivi,
che riceve come argomenti:
  - dirin: il path di una directory
  - extensions: una lista di estensioni di file (stringhe)

La funzione esplora dirin e tutte le sue sottodirectory (a tutti i
livelli) e cerca tutti i file con una delle estensioni indicate.
La funzione ritorna un dizionario che ha come chiavi i path delle directory
e sottodirectory esplorate (con il separatore '/' che vale sia in Windows che Linux)
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
        'Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*' * 50)


