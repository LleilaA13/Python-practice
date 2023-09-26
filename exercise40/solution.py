

def es58(lista):
    movements = {
        'N': (-1,  0),
        'S': (1,  0),
        'E': (0,  1),
        'O': (0, -1),
    }
    nmov = 0
    for i, move in enumerate(lista):
        x = 0
        y = 0
        for c in move:
            if c in 'NSEO':
                nmov += 1
                dx, dy = movements[c]
                x += dx
                y += dy
        lista[i] = abs(x)+abs(y)
    return nmov
