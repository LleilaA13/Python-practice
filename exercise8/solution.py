import treenode


def es7(tree,id_set,k,count=0):
    if tree.sons==[]:
        return count
    a=0
    for el in tree.sons:
        count=es7(el,id_set,k,count)
        if el.id in id_set:
            a+=1
    if a==k:
        return count+1
    else:
        return count
