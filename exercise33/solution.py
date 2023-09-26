def es29(table1,table2,col):
    start = len(table1)
    values = [row[col] for row in table1]
    for row in table2:
        if row[col] not in values:
            table1.append(row)
    table1.sort(key=lambda x: x[col])
    return len(table1) - start