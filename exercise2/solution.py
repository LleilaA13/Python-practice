def es27(table, column, value):
    table2 = [
        {
            c: v for c, v in row.items() if c != column
        } for row in table if row[column] == value
    ]
    diff = len(table) - len(table2)
    table[:] = table2
    return diff
