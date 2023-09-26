

def es64(number_list):
    m = max(number_list)
    rows = len(str(m))
    string_list = ["{:{r}}".format(n, r=rows) for n in number_list] # format will align to the right, by rows positions
    s = ""
    for i in range(rows):
        digit_list_row_i = [number[i] for number in string_list]
        s += " ".join(digit_list_row_i)
        s += "\n"
    # the same as above, using two join functions
    # s = "\n".join(" ".join([n[i] for n in ls]) for i in range(rows))
    return s
