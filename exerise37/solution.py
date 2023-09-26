def ex41(fname1):
    with open(fname1, encoding='utf8') as f:
        sequence = [int(x) for x in f.read().split(',')]

    derived = [sequence[0]]
    for el in sequence[1:]:
        derived.append(derived[-1]+el)
    freq = {}
    for x in derived:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    pairs = [(v, k) for k, v in freq.items()]
    return max(pairs)[1]
