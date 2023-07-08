

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


def es27(table, column, value):
    '''Implement the function es27(table, col, val) that takes as an input

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
    # insert here your code
    table_new = [
        {
            col: val for col, val in row.items() if col != column
        } for row in table if row[column] == value
    ]
    diff = len(table) - len(table_new)
    table[:] = table_new
    return diff


'''This code appears to be a Python snippet that manipulates a table data structure. Let's break it down step by step:

1. `table_new = [...]`: This creates a new list called `table_new` using list comprehension. The new list will contain dictionaries.

2. `{col:val for col,val in row.items() if col != column}`: This is a dictionary comprehension that iterates over each key-value pair in `row.items()`, 
which represents a single row of the table. 
It filters out key-value pairs where the key (`col`) is not equal to the value of the variable `column`. 
The resulting key-value pairs are used to construct a new dictionary.

3. `for row in table if row[column] == value`: This is the outer loop of the list comprehension. 
It iterates over each `row` in the `table` list, but only includes rows where the value of `row[column]` is equal to the value of the variable `value`. 
In other words, it filters rows based on a specific condition.

4. `]`: This marks the end of the list comprehension for `table_new`.

5. `diff = len(table) - len(table_new)`: This calculates the difference in length between the original `table` list and the `table_new` list. 
It subtracts the length of `table_new` from the length of `table` and assigns the result to the variable `diff`.

6. `table[:] = table_new`: This replaces the content of the `table` list with the content of the `table_new` list. 
The `[:]` notation is a way to modify a list in-place, preserving the reference to the original list.

7. `return diff`: This statement returns the value of the variable `diff` as the result of the function or code block.

In summary, the code filters rows from a table based on a specific condition, removes those rows from the original table, and replaces the original table with the filtered rows. 
Finally, it returns the difference in the number of rows before and after the filtering operation.'''
