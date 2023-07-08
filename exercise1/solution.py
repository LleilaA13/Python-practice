def es26(table, column):
    table.sort(key=lambda x: x[column], reverse=True)
    return len(table[0])
