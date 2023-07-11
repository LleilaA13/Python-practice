import treenode
'''A tree is said complete binary if all its internal nodes have
    exactly 2 children and all the leaves are on the same level.
    Design and implement the recursive function es12(k) (or function
    that uses recursive function(s) or recursive method(s)) that:
    - takes as argument an integer k
    and constructs a complete binary tree with height k consisting of
    nodes of type Node, as defined in the library treenode.py. Leaf
    identifiers, read from left to right are the 2^k-integers ranging
    from 1 to 2^k (note that a complete binary tree with height k
    always has 2^k leaves). The identifiers of the internal nodes are
    given by the sum of the identifiers of their two children.
    The function returns as a result the root of the built tree. 
    Example: 
    - es12(2) creates and returns the tree on the left
    - es12(3) creates and returns the tree on the right

                    10                                  36               
            _______|______                      _______|______         
        |              |                    |              |        
        3              7                   10             26        
        ___|___        ___|__               ___|___        ___|__      
    |       |      |      |             |       |      |      |     
    1       2      3      4             3       7     11     15     
                                        _|_     _|_    _|_    _|_    
                                        |   |   |   |  |   |  |   |   
                                        1   2   3   4  5   6  7   8

'''
def es12(k):

    # enter your code here
    pass