import os
import os.path


def es71(dir, minimum, maximum, depth=0):
    """Define the recursive function (or a function that uses your own
    recursive function) es71(dir, minimum, maximum) that searches in
    the directory dir the files that have a size between minimum and
    maximum size (included).  The function returns a dictionary that
    contains the names of the identified files (without path) as keys,
    and the corresponding depths (counting the initial directory 'dir'
    as depth 0) as values.  In case a file name is present at
    different depths, the dictionary must contain the greater one.
    Note: to find the size of the file you can use the os.stat
    function

    """

    diz = {}
    for p in os.listdir(dir):

        if p[0] == ".":
            continue
        p = os.path.join(dir, p)
        if os.path.isdir(p):
            d = es71(p, minimum, maximum, depth + 1)
            for k, v in d.items():
                diz[k] = max(diz.get(k, 0), v)

        if os.path.isfile(p):
            size = os.stat(p).st_size
            if size >= minimum and size <= maximum:
                diz[os.path.basename(p)] = depth

    return diz


if __name__ == '__main__':
    print(es71('t4', 0, 100,))
