def ex63(word_file, triple_file):
    counter = 0
    with open(word_file, encoding='utf8') as fin:
        with open(triple_file, mode='w', encoding='utf8') as fout:
            for line in fin:
                string = line.strip()
                l = len(string)
                counter += l
                v = 0
                m = 0
                for c in string:
                    if c in 'aiuoeAIUOE':
                        v += 1
                    if c.isupper():
                        m += 1
                fout.write(str((l, v, m)) + '\n')
    return counter
