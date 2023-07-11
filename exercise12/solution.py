

import treenode

def es12(k):
    # enter your code here
    t,_ = create_tree(k,1)
    return t

def create_tree(k, n):
    """
    creates the tree with k levels from the value n
    returns the tree and the last n used
    """
    if k:       # if we are on an internal node
        t = treenode.Node( None )
        left, n1 = create_tree(k-1, n)
        right,   n2 = create_tree(k-1, n1+1)
        t.sons = [left, right]
        t.id = left.id + right.id
        return t, n2
    else:
        t = treenode.Node(n)
        return t, n

