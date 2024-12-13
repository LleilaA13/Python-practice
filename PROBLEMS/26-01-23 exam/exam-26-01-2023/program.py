#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il proprio
    NOME, COGNOME, NUMERO DI MATRICOLA
 3) Rinominare la directory examPY inserendo il proprio numero di matricola

Per superare l'esame e' necessario soddisfare tutti i seguenti vincoli:
    - risolvere almeno 3 esercizi di tipo func; AND
    - risolvere almeno 1 esercizio di tipo ex; AND
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale e' la somma dei punteggi dei problemi risolti.
Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""
nome       = "Leila"
cognome    = "Zanoni"
matricola  = "2033176"


#########################################

################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci
# corrispondenti ai test che non si vogliono eseguire all'interno della lista
# `test` alla FINE di `grade.py`.
#
# Per eseguire il debug di funzioni ricorsive potete disattivare il test di
# ricorsione, assegnando `DEBUG=True` all'interno file `grade.py`.
#
# L'impostazione DEBUG=True attiva anche lo la stampa a terminale dello STACK
# TRACE degli errori, che permette di conoscere il numero della linea di
# program.py che ha generato un errore.
################################################################################


# %% -------------------------------- FUNC.1 -------------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(string_list1, string_list2) che riceve in
ingresso due liste di stringhe e restituisce una nuova lista di stringhe
contenente le stringhe presenti soltanto in una delle due liste in ingresso
(ossia, che non compaiono in entrambe le liste). La lista in output
dev'essere ordinata in ordine lessicografico inverso.
'''
def func1(string_list1, string_list2):
    # Inserire qui il proprio codice
    set1 = set(string_list1)
    set2 = set(string_list2)
    set3 = set1 ^ set2
    lista = list(set3)
    return sorted(lista, reverse=True)

#print(func1(['a','b','c'], ['a','d']))
# %% -------------------------------- FUNC.2 -------------------------------- #
''' func2: 2 punti
Si definisca una funzione funct2(path_to_file) che riceve in ingresso
una stringa che rappresenta il percorso ad un file testuale. La funzione
deve restituire il dizionario che associ ad ogni carattere nel testo il
conteggio delle sue occorrenze.

Esempio:
  Il contenuto di func2_test_1.txt è:
    cat rat fat
    art
  L'output atteso dall'invocazione di func2('func2/func2_test_1.txt') è:
  {'c':1, 'a':4, 't':4, 'r':2, 'f':1, ' ':2, '\n':1}

Nota:
  Aprire il file con encoding 'utf-8'.
'''
def func2(path_to_file):
    # Inserire qui il proprio codice
    d = {}
    with open(path_to_file, encoding='utf8') as f:
        for line in f:
            #line = line.strip()
            print(line)
            for char in line:
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
                
    return d
                
    
        
#print(func2('func2/func2_test_1.txt'))
# %% -------------------------------- FUNC.3 -------------------------------- #
'''  func3: 2 punti
Si definisca una funzione func3(a_list) che riceve in ingresso una lista
di numeri ed opera su di essa (ossia, provocando side-effect) rimuovendo tutti
gli elementi uguali al massimo e al minimo.
La funzione deve restituisce la differenza fra la lunghezza iniziale e la
lunghezza finale della lista.

Esempio:
    se a_list = [3, 12, -3, 4, 6, 12]
    dopo la chiamata a func3(a_list) si ha che
    a_list = [3, 4, 6]
    e la funzione restituisce 3.

IMPORTANTE: la lista `a_list` deve risultare cambiata alla fine
dell'esecuzione della funzione.
'''

def func3(a_list):
    # Inserire qui il proprio codice
    lung1 = len(a_list)
    mini= min(a_list)
    maxi = max(a_list)
    
    a_list[:] = [x for x in a_list if x != mini and x != maxi]
    
    return lung1 - len(a_list)

        
#print(func3(a_list = [3, 12, -3, 4, 6, 12]))
# %% -------------------------------- FUNC.4 -------------------------------- #
""" func4: 6 punti
Si definisca una funzione func4(input_filepath, output_filename) che
riceve in ingresso due percorsi a file:
  - Il file `input_filepath` contiene una sequenza di parole, ossia stringhe
    separate da spazi, tabulazioni o invii a capo.
  - Il file `output_filename` indica dove salvare un nuovo file di testo,
    i cui contenuti sono specificati di seguito.
Il file in output deve contenere tutte le parole presenti in
`input_filename`, ripetute una sola volta e organizzate in righe nel modo
seguente.

Le righe nel file di output sono in ordine alfabetico.
All'interno di ogni riga, le parole
  - hanno la stessa lettera iniziale, senza distinzione fra maiuscole e
    minuscole;
  - sono separate da uno spazio;
  - sono ordinate in base alla loro lunghezza e, in caso di pari
    lunghezza, in base all'ordine alfabetico, senza distinzione fra
    maiuscole e minuscole. Nel caso in cui nessuno dei criteri sin qui
    forniti distingua le parole, quelle coincidenti devono essere
    disposte secondo ordinamento lessicografico (ovverosia, si tiene conto
    della differenza tra lettere maiuscole e minuscole solo in ultima
    istanza).

La funzione deve restituire il numero di righe scritte nel file
`output_filename`.

Esempio:
  Nel file 'func4/func4_test1.txt' sono presenti le seguenti due righe:
cat bat    rat
Condor baT
  L'invocazione di func4('func4/func4_test1.txt', 'func4/func4_out1.txt')
  dovrà scrivere nel file 'func4/func4_out1.txt' le seguenti tre righe
  restituendo il valore 3:
baT bat
cat Condor
rat
"""

def func4(input_filename, output_filename):
    #apriamo file, leggiamolo, splittiamo:
    with open(input_filename, encoding = 'utf8') as fin:
        parole = fin.read().split()
    
    #init dizionario, la logica qui è avere un dizionario con le iniziali, cosi da poter scrivere riga per riga
    iniziali = {}
    
    #for loop, per riempire il dizionario, usiamo get!!
    for w in parole:
        iniziale = w[0].lower() #lavoriamo sulle iniziali che poi useremo come chiavi. puliamo le chiavi giu
        
        if w not in iniziali.get(iniziale, []):
            iniziali[iniziale] = iniziali.get(iniziale, []) + [w]
            '''
              This checks if the initial letter (iniziale) already exists as a key in the dictionary iniziali.
            If the key exists: Returns the list of words associated with that letter.
            If the key does not exist: Returns an empty list ([]) as the default.
              Concatenates the current list of words (or an empty list if the key doesn't exist) with a new list containing only the word w.
            '''    
    
    with open(output_filename, mode = 'w', encoding = 'utf8') as fout:
        for i, words in sorted(iniziali.items()):
            print(*sorted(words, key = lambda w : (len(w), w.lower(), w)), file = fout)
            '''
                The * operator takes an iterable (e.g., a list) and unpacks 
                its elements so that each element is treated as a separate value.
            '''
        
    return len(iniziali)
            
    
            

    
    
    
#print(func4('func4/func4_test1.txt', 'func4/func4_out1.txt'))   
    
    
    
    
    

# %% -------------------------------- FUNC.5 -------------------------------- #
""" func5: 8 punti
Si definisca una funzione func5(imagefile, output_imagefile, color) che riceve
in ingresso due stringhe che rappresentano due percorsi a file di immagini PNG e
un colore fornito come una tupla RGB.
L'immagine nel file `imagefile` contiene esclusivamente segmenti orizzontali
bianchi su uno sfondo nero. Ogni riga ha al più un segmento bianco.
La funzione deve creare una nuova immagine in cui sono presenti gli stessi
segmenti dell'immagine in ingresso e modificare il colore dei segmenti con
lunghezza massima utilizzando il colore `color` in ingresso.

L'immagine così ottuenuta deve essere salvata in formato PNG nel file con
percorso `output_imagefile`.

La funzione restituisce il numero di segmenti colorati nell'immagine
in output.
"""
import images
def func5(imagefile, output_imagefile, color):
    # Inserire qui il proprio codice
    white = 255, 255, 255
    black = 0, 0, 0
    
    img = images.load(imagefile)
    
    segmenti = {}
    
    for i, riga in enumerate(img):
        minn = maxx = None
        for x, c in enumerate(riga):
            if c == white:
                if minn is None:
                    minn = x
                if maxx is None:
                    maxx = x
                elif x > maxx:
                    maxx = x
        if minn is not None:
            segmenti[i] = minn, maxx  
            
    lunghezze = [maxx - minn for minn, maxx in segmenti.values()]
    mass = max(lunghezze)
    N = 0
    for y, [minn, maxx] in segmenti.items():
        if maxx - minn == mass:
            N += 1
            for x in range(minn, maxx +1):
                img[y][x] = color
                
    images.save(img, output_imagefile)
                
        
    return N
        
  
    
# %% --------------------------------- EX.1 --------------------------------- #
"""
Ex1: 6 punti

Implementare la funzione ex1 (in modo ricorsivo o utilizzando funzioni
ricorsive) come segue. La funzione ex1 riceve in ingresso i seguenti
argomenti:
  - `directory`, una stringa che rappresenta il percorso di una directory
  - `ext`, una stringa che rappresenta un'estensione di file.
La funzione deve cercare in modo ricorsivo all'interno della `directory`
e in tutte le sue sottodirectory i file che abbiano `ext` come estensione.
Questi file devono essere interpretati come file di testo. La funzione
ex1 deve calcolare la somma delle dimensioni di tutti i file trovati
nelle sottodirectory e restituire un dizionario strutturato come
come segue:
  - le chiavi sono tutte le sottodirectory in cui è presente almeno
    un file con estensione `ext`
  - i valori sono la somma delle dimensioni di tali file contenuti in quella
  sottodirectory.
Le sottodirectory devono essere riportate con il percorso relativo alla
directory corrente. Per esempio, data la struttura di directory:
A/
  B/
    file1.png    #4 byte
  file2.txt      #8 byte

L'invocazione `ex1("A", ".png")` deve restituire `{"A/B":4}`

La dimensione di un file può essere calcolata contando il numero di caratteri
letti dal file.

Si consiglia di utilizzare le funzioni os.listdir, os.path.isfile e
os.path.isdir e NON la funzione os.join in Windows. Utilizzare
la concatenazione tra stringhe con il carattere '/'.
"""

import os
    
def ex1(directory, ext, base_dir=None):
    if base_dir is None:
        base_dir = directory
    dizio = {}
    try:
        for item in os.listdir(directory):
            full_path = directory + '/' + item
            relative_path = os.path.relpath(directory, base_dir)
            if os.path.isdir(full_path):
                dizio.update(ex1(full_path, ext, base_dir))
            elif os.path.isfile(full_path) and item.endswith(ext):
                size = os.stat(full_path).st_size
                dizio[relative_path] = dizio.get(relative_path, 0) + size
    except PermissionError:
        pass
    return dizio


#print(ex1('ex1/A' , '.py'))
            



# %% --------------------------------- EX.2 --------------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root) che riceve in ingresso la radice di un
albero binario, come definito nella classe `BinaryTree` del modulo tree.py.
La funzione deve restituire la somma di tutti i valori associati ai nodi che
sono ad un livello pari nell'albero con radice `root`, e sottraendo tutti i
valori associati ai nodi ad un livello dispari. La radice si assume a livello 0.

Esempio:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

  Se l'albero è quello di sinistra, la funzione deve restituire il valore 8.
  Se l'albero è quello di destra, la funzione deve restituire il valore -22.
"""


def ex2(root):
    # Inserire qui il proprio codice
    return _ex(root, 0, 0)
def _ex(root, level, total):
    if root is None: #leaf
        return total
    if level % 2 == 0:
        total += root.value
    else:
        total -= root.value
    total = _ex(root.left, level +1, total)
    total = _ex(root.right, level + 1, total)
    return total

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
