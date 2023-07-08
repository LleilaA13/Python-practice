import tree


def ex48(root):
    if root == None:
        return 0
    count = ex48(root.sx) + ex48(root.dx)
    if root.sx != None and root.dx != None:
        count += 1
    return count
