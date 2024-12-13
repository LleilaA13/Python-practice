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
"""
nome       = "aspo"
cognome    = "aspo"
matricola  = "Aspo"

#########################################

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To avoid running certain tests, comment out the corresponding  entries in
# the 'tests' list at the end of grade.py.
################################################################################

# %%  ---- FUNC1 ----
''' func1: 2 punti

Si definisca la funzione func1(a_list) che viene fornita una lista di liste
non vuote come parametro. La funzione modifica la lista data direttamente,
sostituendo ciascuna sottolista con il prodotto degli elementi della stessa.
Inoltre, la funzione restituisce il numero di sottoliste.

Ad esempio, se L = [[1, 2, 3], [-1, 2, 3], [2, 2, -2]],
dopo aver chiamato func1(L), il valore di L sarà [6, -6, -8]
(poiché 1 * 2 * 3 = 6, -1 * 2 * 3 = -6 e 2 * 2 * -2 = -8),
e la funzione restituirà 3.
'''

def func1(a_list):
    
    for i, l in enumerate(a_list):
        m = 1
        for k in l:
            m *= k
        a_list[i] = m
    return len(a_list)


# %%  ---- FUNC2 ----
''' func2: 2 punti

Si scriva una funzione func2(a_dictionary) che prenda un dizionario
come parametro, in cui:

    - le chiavi sono singoli caratteri alfabetici
    - gli elementi sono liste di numeri interi positivi

La funzione restituisce il carattere per il quale la lista di interi
corrispondente ha la somma più alta. Se più caratteri hanno la stessa
somma massima, viene restituito il primo in ordine alfabetico.

Ad esempio, func2({"a": [3, 2, 2], "b": [4, 2, 3], "c": [-4, 2, 2]})
restituisce "b", poiché la lista [4, 2, 3] ha la somma più alta
tra tutte le liste nel dizionario.
'''

def func2(a_dictionary):
    return min(a_dictionary, key=lambda x: (-sum(a_dictionary[x]), x))
    pass

# %%  ---- FUNC3 ----
'''  func3: 2 punti

Si definisca una funzione func3(list_A, list_B) che prende due liste
con lo stesso numero di stringhe in input. La funzione restituisce
una terza lista di stringhe. Ogni stringa nella posizione i
nella lista risultante contiene i caratteri comuni tra le due stringhe
nella posizione i in list_A e list_B, tutti in minuscolo,
in ordine alfabetico, e ignorando la maiuscola o minuscola che
avevano nelle stringhe in list_A e list_B. I caratteri comuni tra le
due stringhe nelle due liste possono trovarsi in qualsiasi posizione
all'interno delle stringhe. Le stringhe in list_A e list_B non possono
contenere caratteri ripetuti, indipendentemente dalla loro maiuscola o minuscola.

Ad esempio, se list_A = ["aBd", "baC", "cAb"] e list_B = ["bcE", "dca", "eDf"],
la funzione restituisce: ["b", "ac", ""].

'''

def func3(list_A, list_B):
    l = []
    for x, y in zip(list_A, list_B):
        z = set(x.lower()) & set(y.lower())
        z = ''.join(sorted(z))
        l.append(z)
    return l
    pass
print(func3(["aBd", "baC", "cAb"],["bcE", "dca", "eDf"]))
# %%  ---- FUNC4 ----
''' func4: 6 punti

Si definisca una funzione func4(input_txt, output_txt) che prende
due nomi di file come parametri. La funzione legge il file di testo
input_txt e restituisce il numero di parole più lunghe di 3 caratteri
contenute nel file. Le parole possono essere separate da qualsiasi
numero di spazi o nuove righe.

La funzione scrive il file di testo output_txt che contiene
le parole contate dalla funzione in ordine inverso, una per riga.

Ad esempio, se input_txt contiene il seguente testo:

The          quick
           brown fox            jumps
    over
           
                 the     lazy             dog

La funzione restituisce 5, poiché ci sono 5 parole più lunghe di 3 caratteri
(quick, brown, jumps, over, lazy) e scrive il file:

lazy
over
jumps
brown
quick

'''

def func4(input_txt, output_txt):
    with open(input_txt) as f:
        words = [w for w in f.read().split() if len(w)>3]
    with open(output_txt, 'w', encoding='utf8') as f:
        for w in words[::-1]:
            print(w, file=f)
    return len(words)                
    pass


# %%  ---- FUNC5 ----
""" func5: 8 points
Si scriva una funzione func5(imagefile, output_imagefile, color) che prende
in ingresso due stringhe che rappresentano due nomi di file di immagini PNG.
L'immagine nel file 'imagefile' contiene esclusivamente segmenti orizzontali
bianchi su uno sfondo nero e ha larghezza massima di 256 pixel.
Ogni riga ha al più un segmento bianco.
La funzione deve creare una nuova immagine con le stesse dimensioni e
gli stessi segmenti dell'immagine in ingresso, in cui il colore dei
segmenti con lunghezza minima e massima è modificato.
Il colore da utilizzare (R, G, B) è definito in questo modo:
    - il canale R corrisponde al valore del segmento con lunghezza minima
    - il canale B corrisponde al valore del segmento con lunghezza massima
    - il canale G corrisponde al valore che si ottiene dal valore medio delle
      lunghezze di tutti i segmenti (si utilizzi la divisione intera).

L'immagine così ottenuta deve essere salvata in formato PNG nel file con
percorso output_imagefile.

La funzione ritorna il numero di segmenti colorati nell'immagine in output.
"""
import images

def follow(img, i, j):
    x = j
    while x< len(img[i]) and img[i][x] == (255,255,255):
        x+=1
    return x-j

def func5(imagefile, output_imagefile):
    ## Scrivi qui il tuo codice
    img = images.load(imagefile)
    segments = {}
    for i, row in enumerate(img):
        for j, pix in enumerate(row):
            if img[i][j] == (255,255,255):
                length = follow(img, i, j)
                segments[length] = segments.get(length, []) + [(i,j)]
                break
    R = min(segments.keys())
    G = sum([k*len(v) for k,v in segments.items()])//sum(map(len, segments.values()))
    B = max(segments.keys())
    # print(R, G, B)
    count = 0
    for length in {R, B}:
        # print(length)
        for i, j in segments[length]:
            # print(i,j)
            img[i][j:j+length] = [(R,G,B)]*length
            count += 1
    # img[0][0] = (255,255,9)
    images.save(img, output_imagefile)
    return count

# for i in range(1, 5):
#     print('func', func5(f'func5/func5_test{i}.png', f'func5/func5_out{i}.png'))
    

# %% ----------------------------------- EX.1 ----------------------------------- #
'''
Ex1: 6 punti

Si definisca una funzione ex1(target_folder), ricorsiva o che utilizzi almeno una
funzione ricorsiva, che prenda in input il percorso di una cartella di destinazione.
La funzione scandisce in modo ricorsivo la cartella target_folder e tutte
le sue sottocartelle, restituendo una lista di coppie (percorso, conteggio), in cui:
- il percorso è il percorso completo di una delle sottocartelle della cartella target_folder
(nidificate a qualsiasi livello >= 0 all'interno della cartella di destinazione;
la cartella di destinazione può essere considerata una sottocartella di se stessa,
per cui il livello=0);
- il conteggio è il numero di file di testo contenuti nella sottocartella
(i file di testo sono file il cui nome termina con ".txt").

La lista restituita è ordinata in base al valore del contatore dei file, in ordine decrescente;
se due o più cartelle contengono lo stesso numero di file, vengono ordinate in ordine alfabetico.

Le uniche due funzioni che possono essere importate nella soluzione sono: os.listdir e os.path.isdir.

Ad esempio, se la struttura della cartella è la seguente:

A
|-B
| |-C
| | |-c1.txt
| | |-c2.txt
| |
| |-b1.txt
| |-b2.txt
| |-b3.txt
|
|-D
| |-d1.txt
| |-d2.txt
|
|-E
| |-e1.txt
|
|-a1.txt
|-a2.txt
|-a3.txt

La funzione restituisce la lista:

[("A", 3), ("A/B", 3), ("A/B/C", 2), ("A/D", 2), ("A/E", 1)]

'''

from  os import listdir
from os.path import isdir

def ex1(target_folder):
    count = 0
    ret = []
    for f in listdir(target_folder):
        fname = target_folder+'/'+f
        if isdir(fname):
            ret.extend(ex1(fname))
        elif f.endswith('.txt'):
            count += 1
    return sorted(ret + [(target_folder, count)], key = lambda x: (-x[1], x))
    pass



# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: 6 marks

Si definisca una funzione ex2(T) che prende come parametro la radice T
di un albero binario, memorizzato come un oggetto BinaryTree definito
nel file tree.py. La funzione è ricorsiva o utilizza almeno una
funzione ricorsiva. I valori nell'albero sono interi.
La funzione restituisce la terna (L, S, D), dove:
- L è il numero di foglie;
- S è il numero di nodi con un solo nodo figlio;
- D è il numero di nodi con due nodi figli.

Ad esempio, se T è:

                T       
          ______2______  
         |             | 
      __ 7__        ___15___  
     |      |      |       | 
    _4      3     _0_      5_  
   |             |   |       | 
   2             8   3      -9 

La funzione restituisce: (5, 2, 4)
'''

from tree import BinaryTree    
    
def ex2(T):
    if T == None:
        return (0, 0, 0)
    if T.right==None and T.left==None:
        return 1, 0, 0
    L1, S1, D1 = ex2(T.left)
    L2, S2, D2 = ex2(T.right)
    if T.right and T.left:
        D2+=1
    else:
        S2+=1
    return L1+L2, S1+S2, D1+D2
        

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*' * 50)
    print('ITA\nEseguire grade.py per effettuare il debug con grader incorporato.')
    print('Altrimenti, inserire codice qui per verificare le funzioni con test propri')
    print('*' * 50)
    print('ENG\nRun grade.py to debug the code with the automatic grader.')
    print('Alternatively, insert here the code to check the functions with custom test inputs')
    print('*' * 50)
    