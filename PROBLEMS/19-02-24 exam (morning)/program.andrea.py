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
nome       = "NME"
cognome    = "CGNOME"
matricola  = "MTRICOLA"


#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
'''
Func 1: 2 punti
Si definisca la funzione func1(list1, list2) che riceve come argomento:
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
    ## Scrivi qui il tuo codice
    minuscole1 = [w.lower() for w in list1]
    minuscole2 = [w.lower() for w in list2]
    comuni = set(minuscole1) & set(minuscole2)
    res = {}
    for w in comuni:
        res[len(w)] = res.get(len(w), set()) | {list1[minuscole1.index(w)], list2[minuscole2.index(w)]}
    return res


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(dicts) che prende in ingresso una lista di
dizionari. I dizionari hanno come chiave un intero e come valore una stringa.
E' necessario calcolarsi un dizionario unico che contiene tutte le
chiavi di tutti i dizionari con i valori associati. Nel caso in cui vi
siano ripetizioni delle chiavi e' necessario concatenare le stringhe fra loro.
Ciascuna stringa dentro il dizionario unico deve essere ordinata in ordine
alfabetico.

Se dicts = [{1:'iac', 2:'andrea',3:'mau', 5:'angelo'},
{2:'sterbini', 3:'mancini',1:'masi', 5:'spognardi'}]
si restituise
{1: 'aaciims', 2: 'aabdeeiinnrrst', 3: 'aaciimmnnu', 5: 'aadeggilnnooprs'}

Si assuma che dicts non sia mai vuoto.
'''

def func2(dicts):
    ## Scrivi qui il tuo codice
    pass
    return {k: ''.join(sorted(''.join([d.get(k, '') for d in dicts])) ) for k in set().union(*dicts)}


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(lists) che prende in ingresso una lista dove
ogni elemento di lists sono liste annidate con al massimo un solo elemento
per lista. Se la lista contiene almeno un elemento allora contiene una lista.
Ad esempio: lists puo' essere [[[]], [[[[[[]]]]]], [[]]]
e si deve restituire la profondita' massima della liste
annidate. Nell'esempio sopra la profondita' massima e' 6 in quanto in
lists[1] abbiamo 6 parentesi aperte e chiuse.
'''


def func3(lists):
    ## Scrivi qui il tuo codice
    pass
    return max([0] + [str(l).count('[') for l in lists])


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Si definisca la funzione func4(input_filename, output_filename) che
prende due nomi di file come parametri. La funzione legge il file di
testo input_filename. Considerando una riga del file, si consideri la
somma della rappresentazione numerica di ogni carattere delle parole
presenti su quella riga.  La funzione restituisce una lista con le
somme calcolate su ciascuna riga del file input_filename ordinate in
ordine crescente.

Nel file func4/func4_test1.txt l'ultima riga
Cat cAr CAR
ha somma  772 sommando i caratteri delle SOLE parole (escluso
whitespaces).

Quindi il file avra' somme su ogni riga:
somme = [ 950, 892, 772]
      riga 0   1     2

e si restituisce [772, 892, 950].

La funzione inoltre scrive un file di testo nella posizione output_filename
che contiene gli indici che ordinano "somme", un indice per ogni riga.

Nel file func4/func4_out1.txt deve essere scritto:
2
1
0
"""


def func4(input_filename, output_filename):
    ## Scrivi qui il tuo codice
    pass
    with open(input_filename, 'r') as f:
        somme = [sum([ord(c) for l in line.split() for c in l ]) for line in f]
    with open(output_filename, 'w') as f:
        f.write('\n'.join(map(str, sorted(range(len(somme)), key=lambda i: somme[i])))
                + '\n')
    return sorted(somme)


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti
Si definisca la funzione func5(H, W, sx, sy, outpath) che prende in ingresso
l' altezza H e la larghezza W di un'immagine che deve essere creata come segue.
Sull'immagine di sfondo NERO dobbiamo disegnare delle "griglie" di colore
BIANCO che dipendono dai parametri sx, sy. Il parametro sx rappresenta
la quantita' di spazi neri che ci sono in orizzontale fra due tratti della griglia;
ugualmente sy rappresenta la quantita' di spazi neri che ci sono in verticale
fra due tratti della griglia. Quando si disegna si parte sempre in alto a sinistra,
e si procede verso il basso a destra. L'immagine creata deve essere salvata in outpath
e si devono restituire il numero di pixel BIANCHI dell'immagine creata.

Se ad esempio: H=9,W=17,sx=3,sy=1 si disegna:

.................
.xxx.xxx.xxx.xxx.
.................
.xxx.xxx.xxx.xxx.
.................
.xxx.xxx.xxx.xxx.
.................
.xxx.xxx.xxx.xxx.
.................

dove . = BIANCO e x = NERO, infatti in verticale si disegna
una riga si e uno no; in verticale si disegna una colonna si e 3 no.
"""

import images


def func5(H, W, sx, sy, outpath):
    ## Scrivi qui il tuo codice
    pass
    b = 0,0,0
    w = 255,255,255
    img = [ [b]*W for _ in range(H)]
    count = 0
    for y in range(0, H, sy+1):
        for x in range(W):
            img[y][x] = w
            count += 1
    for x in range(0, W, sx+1):
        for y in range(H):
            if img[y][x] == b:
                img[y][x] = w
                count += 1
    images.save(img, outpath)
    return count

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si definisca la funzione ex1(node), ricorsiva o che usa un metodo
ricorsivo, che prende in ingresso il nodo root che è la radice di
un albero binario costituito da nodi del tipo BinaryTree,
come definito nel modulo tree.py.
La funzione deve ritornare una lista di set. Ogni elemento della
lista corrisponde ad un livello dell'albero: in particolare l'elemento
i-esimo della lista contiene un set con tutti i valori dell'albero
raccolti al livello i.

Esempio:

        root     
    ______25______            livello = 0
   |             | 
   8__        ___2___         livello = 1
      |      |       | 
      3      9       1        livello = 2

   expected = [{25}, {8, 2}, {9, 3, 1}]
   livello      0       1        2
"""

def ex1(node):
    ## Scrivi qui il tuo codice
    pass
    return _ex1(node, 0, [])

def _ex1(node, level, res):
    if node is not None:
        if len(res) <= level:
            res.append(set())
        res[level].add(node.value)
        _ex1(node.left, level+1, res)
        _ex1(node.right, level+1, res)
    return res


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(alfabet), ricorsiva o che utilizza
funzioni o metodi ricorsivi, che prende in ingresso una stringa
"alfabet" e restituisce un set.  La stringa "alfabet" puo' contenere
caratteri maiuscoli e minuscoli oppure tutti in un solo stile (tutto
maiuscolo, o tutto minuscolo). La funzione deve generare tutte le
possibili parole che si possono creare combinando i caratteri di
"alfabet" con le segueni regole:
  1. Una volta che un carattere e' usato non si puo' piu' utilizzare
  (come nelle permutazioni)
  2. NON si possono concatenare due caratteri con maiuscolo maiuscolo
  oppure minuscolo e minuscolo.  In altre parole gli stili dei due
  caratteri concatenati deve essere "discordi" (maiuscolo e minuscolo va bene
  e minuscolo maiuscolo va bene).

Se alfabet='icA' si deve generare il set:
{'iAc', 'cAi', 'Ai', 'Ac'}
"""


def ex2(alfabet):
    ## Scrivi qui il tuo codice
    pass
    minuscole = [ c for c in alfabet if c.islower() ]
    maiuscole = [ c for c in alfabet if c.isupper() ]
    Sm = _ex2(minuscole, maiuscole)
    SM = _ex2(maiuscole, minuscole)
    return Sm | SM

def _ex2(gruppo1,gruppo2, livello=0):
    res =  set(gruppo1) | set(gruppo2)
    for i, c in enumerate(gruppo1):
        rest = gruppo1[:i] + gruppo1[i+1:]
        sottosoluzioni = _ex2(gruppo2,rest, livello+1)
        res |= sottosoluzioni
        res |= { c + s for s in sottosoluzioni if c.islower() != s[0].islower() }
    return res

    
# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
