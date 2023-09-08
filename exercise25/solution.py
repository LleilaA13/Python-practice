import os
import os.path


def es71(dir, minimum, maximum, depth=0):
    depths = {}
    for f in os.listdir(dir):
        fn = "{}/{}".format(dir, f)
        if os.path.isdir(fn):
            diz = es71(fn, minimum, maximum, depth+1)
            for k, v in diz.items():
                if k not in depths or v > depths[k]:
                    depths[k] = v
        else:
            stat = os.stat(fn)
            if minimum <= stat.st_size <= maximum:
                if f not in depths or depth > depths[f]:
                    depths[f] = depth
    return depths
