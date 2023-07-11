


class Node:
    def __init__(self,V):
        self.id=V
        self.sons=[]


################### FROM HERE ARE ONLY FUNCTIONS NEEDED FOR TESTING #####################

def fromLista(lista):
    '''Create the tree from a list [value, child list].
           Where child list contains trees or is an empty list. '''
    r=Node(lista[0])
    r.sons=[fromLista(x) for x in lista[1]]
    return r

def toLista(nodo):
    ''' Convert the tree into a list of lists [value, child list].'''
    return [nodo.id, [toLista(x) for x in nodo.sons]] 
