'''
Es 9: 3 punti
Si definisca la  funzione es18(d1,d2) che, 
- riceve due dizionari aventi per chiavi degli interi e per attributo insiemi di interi.
- restituisce un dizionario.
il dizionaro deve contenere come chiavi le chiavi che sono in comune ad entrambi i dizionari e come 
attributo una tupla di due elementi, il primo elemento e' 
l'insieme intersezione degli attributi della chiave nei due dizionari mentre 
il secondo e' l'unione degli attributi della chiave nei due dizionari.
Ad ESEMPIO se
d1={1: {1,2,3}, 2:{1,2,3}, 5:{1} } e 
d2={1: {3,4,5}, 3:{1,2,3}, 5:{3}, 8: {6} }
allora la funzione  restituisce il dizionario 
{1: ({3}, {1, 2, 3, 4, 5}), 5: (set(), {1, 3})}
'''


def es18(d1, d2):
    diz = {}
    set1 = set(d1)
    set2 = set(d2)
    # print(set1, set2)
    set3 = set1.intersection(set2)

    lista = list(set3)
    set_union = set()
    set_intersection = set()
    # print(lista)
    for k in lista:
        diz[k] = (set_intersection, set_union)
    for k in d1.keys():
        if k in d2.keys():
            set_union = d1[k] | d2[k]
            set_intersection = d1[k] & d2[k]
            diz[k] = (set_intersection,set_union)
    return diz

    #intersection_set = set1.intersection(set2)
    #print(union_set,intersection_set)


    # set_valori1 = set(lista_valori1)
    # set_valori2 = set(lista_valori2)
    # diz = (set_valori1.union(set_valori2), set_valori1.intersection(set_valori2))


if __name__ == '__main__':
    print(es18({1: {1, 2, 3}, 2: {1, 2, 3}, 5: {1}}, {1: {3, 4, 5}, 3: {1, 2, 3}, 5: {3}, 8: {6}}))
    'Daje Leylaa che sei brava bravaa!!'