def es43(textfile):
    sums = []
    with open(textfile) as f:
        for line in f:
            numbers = list(map(int, line.split()))
            for i, v in enumerate(numbers):
                if i < len(sums):
                    sums[i] += v
                else:
                    for _ in range(i - len(sums)):
                        sums.append(0)
                    sums.append(v)
    return sums
