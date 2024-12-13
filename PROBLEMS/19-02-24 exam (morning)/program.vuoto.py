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
    pass


#list1 = [ 'a', 'Bc', 'a', 'b', 'cR', 'e', 'a', 'qrt', 'st' ]
#list2 = [ 'a', 'cd', 'f', 'bC', 'cr', 'E', 'bn', 'c' ]
#print(func1(list1,list2))

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(dicts) che prende in ingresso una lista di
dizionari. I dizionari hanno come chiave un intero e come valore una stringa.
La funzione costruisce e ritorna un dizionario unico che contiene tutte le
chiavi di tutti i dizionari con i valori associati. Nel caso in cui dei
dizionari hanno delle chiavi in comune, è necessario concatenare fra loro
le stringhe ad esse associate nei dizionari.
Ciascuna stringa del dizionario in uscita deve essere ordinata in ordine
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


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(lists) che prende in ingresso una lista dove
ogni elemento di lists è composto da liste annidate con al massimo un solo
elemento per lista. Se una lista di lists contiene un elemento allora
questo è una lista.
Ad esempio: lists puo' essere [[[]], [[[[[[]]]]]], [[]]]
La funzione deve restituire un intero che rappresenta la profondità massima
di annidamento delle liste di lists.

Nell'esempio sopra la profondità massima è 6, infatti lists[1] ha 
6 parentesi aperte e 6 chiuse.
'''


def func3(lists):
    ## Scrivi qui il tuo codice
    pass


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Si definisca la funzione func4(input_filename, output_filename) che
prende due nomi di file come parametri. La funzione legge il file di
testo input_filename e restituisce una lista. Per ogni riga del file, la
funzione calcola la somma della rappresentazione numerica di ogni
carattere delle parole presenti su quella riga e restituisce una lista con le
somme calcolate ordinate in ordine crescente.
La funzione inoltre scrive un file di testo nella posizione output_filename.
Per ogni riga i del file input_filename inserisce nella riga i del file
output_filename la posizione occupata dalla somma calcolata per quella riga
nella lista in uscita.

Ad esempio, il contenuto del file func4/func4_test1.txt è
cat bat    rat
Condor baT
Cat cAr CAR

Sommando i caratteri delle SOLE parole (escluso whitespaces) produce
la lista [ 950, 892, 772 ]
 num.riga   0    1    2

Per cui la funzione restituisce [772, 892, 950].

Inoltre, poiché l'ordinamento delle righe è 2, 1, 0, la funzione scrive
nel file func4/func4_out1.txt le righe
2
1
0
"""


def func4(input_filename, output_filename):
    ## Scrivi qui il tuo codice
    pass


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 6 punti
Si definisca la funzione func5(H, W, sx, sy, outpath) che prende in ingresso
l'altezza H e la larghezza W di un'immagine che deve essere creata come segue.
Su un'immagine di sfondo NERO dobbiamo disegnare delle "griglie" di colore
BIANCO che dipendono dai parametri sx, sy. Il parametro sx rappresenta
la quantità di spazi neri che ci sono in orizzontale fra due tratti della griglia;
ugualmente sy rappresenta la quantità di spazi neri che ci sono in verticale
fra due tratti della griglia.
Quando si disegna si parte sempre in alto a sinistra, e si procede verso il
basso a destra.
L'immagine creata deve essere salvata in outpath e si devono restituire il
numero di pixel BIANCHI dell'immagine creata.

Se ad esempio: se H=9,W=17,sx=3,sy=1 la funzione ritorna il valore 105.
e crea la seguente immagine ne file in outpath:

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

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 7 punti

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

def ex1(root):
    ## Scrivi qui il tuo codice
    pass


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 7 punti

Si definisca la funzione ex2(alphabet), ricorsiva o che utilizza
funzioni o metodi ricorsivi, che prende in ingresso una stringa
"alphabet" e restituisce un set.  La stringa alphabet può contenere
caratteri maiuscoli e minuscoli oppure tutti in un solo stile (tutto
maiuscolo, o tutto minuscolo). La funzione deve generare tutte le
possibili parole che si possono creare combinando i caratteri di
"alphabet" usando le segueni regole:
  1. una volta che un carattere è stato usato non si può più utilizzare
  (come nelle permutazioni)
  2. un carattere maiuscolo deve essere seguito da un carattere minuscolo
  e viceversa. Questo vuol dire che NON si possono concatenare due caratteri
  tipo maiuscolo maiuscolo oppure minuscolo e minuscolo. 

Se alfabet='icA' si deve generare il set:
{'i', 'Ai', 'cAi', 'iAc', 'Ac', 'cA', 'c', 'A', 'iA'}
"""


def ex2(alphabet):
    ## Scrivi qui il tuo codice
    pass


    
# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
