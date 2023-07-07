
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

def es26(table, column):
    '''Define the function es26(table, col) that takes as an input

    - a table table represented by a list of dictionaries
    - a string col with the name of one of the columns of table

    and modifies table by reordering the rows in descending order with
    respect to the values contained in column col. The function
    returns the number of columns in the table.

    For example, 
    - if table = [{'name': 'Sophie','year': 1973, 'tel': 5553546},
                  {'name': 'Bruno', 'year': 1981 ,'tel': 5558432}]

    - the function call es26(table, 'year') returns 3 and  modifies 
    table in [{'name': 'Bruno', 'year': 1981,'tel': 5558432},
              {'name': 'Sophie','year':1973 ,'tel': 5553546}]

    '''
    # enter your code here
