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
'''

def es28(table, col, val):
    '''Implement the function es28(table, col, val) that takes as an
    input

    - a table table represented by a list of dictionaries
    - a string col with the name of one of the columns of the table
    - a value val
    
    and returns a new table obtained from table removing the column
    col and deleting all the rows with a value different from val in
    col. The original table should not be modified. The rows in the
    new output table have the same order of the original table.

    For example,

    -if table = [{'name': 'Sophie', 'year': 1973 ,'tel': 5553546},
                {'name': 'Bruno', 'year': 1981 ,'tel': 5558432}]
    - the function call es28(table, 'year', 1981) returns the table
    [{'name': 'Bruno','tel': 5558432}]

    '''
    table3 = [
      {c:v for c,v in row.items() if c != col} for row in table if row[col] == val
    ]
    return table3
    print(table3)