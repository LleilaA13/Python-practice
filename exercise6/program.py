import tree


def ex48(root):
    '''Design a function ex48(tree) such that:
    - it is recursive or uses recursive functions(s)/method(s),
    - it receives as arguments a tree that consist of nodes of type
      BinaryTree, defined in the attached tree.py library
    - it returns the number of nodes of the tree having EXACTLY two
      children
    Example: if the tree is

             7
            /\
           1  3
          / \
        4    6
       /    /
      5    2
     /     \
    9       8

    the function will return the value 2, since there are only two
    nodes with exactly two children, namely the nodes with value 7 and
    1.

    '''
    if root == None:
        return 0
    count = ex48(root.sx) + ex48(root.dx)
    if root.sx != None and root.dx != None:
        count += 1
    return count
  
