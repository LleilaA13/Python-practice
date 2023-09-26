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

Implement the function es29(table1, table2, col) that takes as an
 input

 - two tables: table1 and table2, represented by a list of
   dictionaries and having the same columns

 - a string col with the name of one of the columns of the two
   tables with respect to which the two tables are sorted in
   ascending order.

 For all the rows, the values in column col are unique in both
 table1 and table2.

 The function has to insert in table1 all the rows of table2 that
 have, in column col, a value not already present in table1
 (namely, for all the rows of table1, the values in column col
 remain unique even after the insertions).  At the end, table1 is
 still orderered with respect to the values of the col column. The
 function also returns the number of rows inserted in table1.

 For example, if:

 -table1=[{'C1': 1, 'C2': 'x'},
          {'C1': 3, 'C2': 'a'},
          {'C1': 4, 'C2': 'a'},
          {'C1': 5, 'C2': 'a'},
          {'C1': 7, 'C2': 'b'}],

 -table2=[{'C1': 2, 'C2': 'a'},
          {'C1': 3, 'C2': 'b'},
          {'C1': 5, 'C2': 'a'},
          {'C1': 6, 'C2': 'b'},
          {'C1': 7, 'C2': 'a'}]

 -col = 'C1'

 the function has to return 2 and table1 changes in
 table1=[{'C1': 1, 'C2': 'x'},
         {'C1': 2, 'C2': 'a'},
         {'C1': 3, 'C2': 'a'},
         {'C1': 4, 'C2': 'a'},
         {'C1': 5, 'C2': 'a'},
         {'C1': 6, 'C2': 'b'},
         {'C1': 7, 'C2': 'b'}]
'''
def es29(table1,table2, col):
   lung = len(table1)
   values = [row[col] for row in table1]
   for row in table2:
      if row[col] not in values:
          table1.append(row)
   table1.sort(key = lambda x: x[col])
   return len(table1) - lung
       
if __name__ == '__main__':
    print(es29([{'C1': 1, 'C2': 'x'},
             {'C1': 3, 'C2': 'a'},
             {'C1': 4, 'C2': 'a'},
             {'C1': 5, 'C2': 'a'},
             {'C1': 7, 'C2': 'b'}],
                      [{'C1': 2, 'C2': 'a'},
                      {'C1': 3, 'C2': 'b'},
                      {'C1': 5, 'C2': 'a'},
                      {'C1': 6, 'C2': 'b'},
                      {'C1': 7, 'C2': 'a'}], 'C1'))     


