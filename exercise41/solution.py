

def es59(ftext):
    string = ''
    with open(ftext) as f:
        for line in f:
            integers = map(int, line.split())
            string += str(sum(integers)%2)
    return string