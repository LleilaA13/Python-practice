
import os
import os.path


def es68(dirname, extensions):
    count = {ext: 0 for ext in extensions}
    for f in os.listdir(dirname):
        fn = os.path.join(dirname, f)
        if os.path.isdir(fn):
            diz = es68(fn, extensions)
            for k, v in diz.items():
                count[k] += v
        else:
            for ext in extensions:
                if fn.endswith(ext):
                    count[ext] += 1
    for k in list(count.keys()):
        if count[k] == 0:
            del count[k]
    return count
