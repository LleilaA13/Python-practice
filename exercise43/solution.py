import os
import os.path


def es70(dirname, extensions, words):
    words = [p.lower() for p in words]
    count = {p: 0 for p in words}
    for f in os.listdir(dirname):
        fn = os.path.join(dirname, f)
        if os.path.isdir(fn):
            diz = es70(fn, extensions, words)
            for k, v in diz.items():
                count[k] += v
        elif not fn.endswith(tuple(extensions)):
            with open(fn) as f:
                for line in f:
                    for word in line.split():
                        word = word.lower()
                        if word in words:
                            count[word] += 1
    for k in list(count.keys()):
        if count[k] == 0:
            del count[k]
    return count
