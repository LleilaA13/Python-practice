'''
    A common way to store tables is as lists of dictionaries.  Each
    row of the table corresponds to a dictionary whose keys are the
    names of the table columns.  This dictionary collection is then
    stored in a list.  For example the table
    
    name  | year | tel
    --------|------|---------
    Sophie | 1973 | 5553546 
    Bruno  | 1981 | 5558432

can be stored as 
[{'name': 'Sophie', 'year': 1973 ,'tel': 5553546},{'name': 'Bruno', 'year': 1981 ,'tel': 5558432}]
Implement the function es27(table, col, val) that takes as an input

    - a table table represented by a list of dictionaries
    - a string col with the name of one of the columns of the table
    - a value val

    and modifies the table removing the column col and deleting all
    the rows with a value different from val in column col.  The
    function returns the number of deleted rows.

    For example
    - if table = [{'name': 'Sophie', 'year': 1973 ,'tel': 5553546},
                {'name': 'Bruno', 'year': 1981 ,'tel': 5558432}]

    - the function call es27(table, 'year', 1981) returns the number 1
    and the table is modified in [{'name': 'Bruno','tel': 5558432}]

'''


def es27(table, column, value):
    table_new = [{col:val for col,val in row.items() if col != column}
                for row in table if row[column] == value]
    difference = len(table) - len(table_new)
    table[:] = table_new
    return difference