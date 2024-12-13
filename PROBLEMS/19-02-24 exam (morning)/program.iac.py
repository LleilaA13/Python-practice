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
nome       = "iac"
cognome    = "masi"
matricola  = "1"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(lists) che prende in ingresso una lista
di liste. Ciascuna lista interna contiene degli interi. La funzione
restituisce una lista che contiene tutte gli interi che sono presenti
in tutte le liste interne. Gli interi nella lista in uscita sono
ordinati dal piu grande al piu piccolo.

Se lists = [[4, 4, 10, 4, 1], [4, 2, 1], [1, 4]]

allora si restituisce [4, 1] in quanto 4 e' in tutte le liste
cosi come 1; invece 10 non e' nel risultato perche' compare
solo in lists[0]. Si assuma che lists non sia mai vuota.
'''


def func1(list1, list2):
    # da andrea
    minuscole1 = [x.lower() for x in list1] # minuscole nello stesso ordine di list1
    minuscole2 = [x.lower() for x in list2] # minuscole nello stesso ordine di list2
    comuni = set(minuscole1).intersection(set(minuscole2))
    diz = {}
    for parola in comuni:
        if len(parola) not in diz:
            diz[len(parola)] = set()
        diz[len(parola)] |= {list1[minuscole1.index(parola)], list2[minuscole2.index(parola)]}
    return diz



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
    out = dicts[0]
    for D in dicts[1:]:
        for k, v in D.items():
            if k in out:
                out[k] += v
            else:
                out[k] = v
    for k in out.keys():
        out[k] = ''.join(sorted(out[k]))
    return out


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
    maxC = 0
    for lista in lists:
        count = 1
        while len(lista) != 0:
            count += 1
            lista = lista[0]
        maxC = max(maxC, count)
    return maxC


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
    with open(input_filename) as fr, open(output_filename, mode='wt') as fw:
        out = []
        for i, line in enumerate(fr):
            words = line.split()
            out.append((i, sum(ord(c) for word in words for c in word)))
        out.sort(key=lambda T: (T[1]))
        idx, summ = map(lambda *args: args, *out)
        print(*idx, sep='\n', file=fw)
    return list(summ)


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

def writecol(im,x,H):
    for y in range(H):
        im[y][x] = (255,)*3

def func5(H, W, sx, sy, outpath):
    black = (0,)*3
    im = [[black]*W for _ in range(H)]
    for y in range(0, H, sy+1):
        im[y][:] = [(255,)*3]*W
    for x in range(0, W, sx+1):
        writecol(im,x,H)
    images.save(im, outpath)
    return sum(p != black for line in im for p in line)

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

def explore(node, D, level):
    if node is None: return 
    if node.left: explore(node.left,D, level+1)
    if node.right: explore(node.right,D, level+1)
    D[level] = D.get(level, set()) | {node.value}

def ex1(node):
    D = {}
    explore(node, D, level=0)
    return [D[k] for k in sorted(D)]


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


def discord(last, curr):
    return any([last.isupper() and curr.islower(),
                last.islower() and curr.isupper()])


def gen(state, W):
    out, leaf = set(), True
    for i in range(len(W)):
        if not state or discord(state[-1], W[i]):
            leaf = False
            out |= gen(state+W[i], W[:i]+W[i+1:])
    if leaf:
        out.add(state)
    return out


def ex2(alfabet):
    return gen('', alfabet)

def ex2(alfabet):
    # da aspo
    if all(a.islower() for a in alfabet) or all(a.isupper() for a in alfabet):
        return set(alfabet)
    s = set()
    for i, c in enumerate(alfabet):
        s1 = ex2(alfabet[:i]+alfabet[i+1:])
        s.update(s1)
        for v in s1:
            if (v[0].islower() and c.isupper()) or v[0].isupper() and c.islower():
                s.add(c+v)
    return s


    
# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
