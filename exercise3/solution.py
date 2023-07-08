def es28(table,column,value):
    table2 = [
        {
            c: v for c, v in row.items() if c != column
        } for row in table if row[column] == value
    ]
    return table2