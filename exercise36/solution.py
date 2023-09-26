import os


def es35(dir1, word_set):
    # I initialize the dictionary with the words to look up and the counters to zero
    diz = {w: [0, 0] for w in word_set}
    # I scan the directory and take only files with the extension '.txt'.
    for fn in os.listdir(dir1):
        if not os.path.isdir(fn) and fn[-4:] == '.txt':
            with open(dir1 + "/" + fn) as f:
                # I extract the words from the file, since they are separated by space/accapo/tab it's enough to use split
                words = f.read().split()
                # for every word in the file, if it is one of those searched increase its count
                for w in words:
                    if w in word_set:
                        diz[w][0] += 1
                # for each word searched, if it is in the file increase the count of the number of files that contain it
                for p in word_set:
                    if p in words:
                        diz[p][1] += 1
    # at the end I return a dictionary with only the searched words that have been found in some file
    return {k: tuple(v) for k, v in diz.items() if v[0]}
