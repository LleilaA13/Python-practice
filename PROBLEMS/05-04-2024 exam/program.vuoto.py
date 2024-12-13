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
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #

''' func1: 4 punti
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
def func1(D1,  D2):
    ## Scrivi qui il tuo codice
    pass

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
def func2(testo, n):
    ## Scrivi qui il tuo codice
    pass

# Esempio di test:
#testo = 'la rana in Spagna gracida in campagna'
#n = 3
#print(func2(testo, n))  # ['campagna', 'gracida', 'Spagna', 'rana']


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

def func3(S1, S2):
    ## Scrivi qui il tuo codice
    pass

# Esempio di test
#S1 = {'a', 'b', 'c'}
#S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
#print(func3(S1, S2))  # {'a': ['abc', 'aa', 'ab'], 'c': ['cc', 'cd'], 'b': ['bb', 'bc']}


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

def func4(file_png, N):
    ## Scrivi qui il tuo codice
    pass

#Esempio di test
#print(func4('func4/1.png', 5))  # {(125, 190, 250): 1, (184, 100, 249): 2, (115, 186, 199): 1, (139, 150, 176): 1, (250, 240, 236): 1, (125, 157, 232): 1}


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

def func5(file_txt, K, M):
    ## Scrivi qui il tuo codice
    pass

# Esempio di test
#file_txt = 'func5/1.txt'
#K = 3
#M = 10
#print(func5(file_txt, K, M))  # [[1, 2, 30], [4, 5, 60], [7, 8, 90]]


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

def ex1(dirname, necessary, forbidden):
    ## Scrivi qui il tuo codice
    pass

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


# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
