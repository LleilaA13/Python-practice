import copy

def ex54(mylist):
  '''Design a function ex54(mylist) such that:
  - it receives as arguments a list containing integers and strings
  - it modifies the list by deleting all the strings
  - it returns a dictionary.
  The function deletes from 'mylist' all the elements that are
  strings and returns a dictionary where:
  - the keys are the deleted strings
  - the values are the number of times the related key-string was
    deleted from 'mylist'.
  The use of the library copy is allowed.

  Example: if mylist=[1,'a',2,'b','a',8,'d',8], the function returns
  the dictionary {'a':2,'b':1,'d':1} and the list becomes [1,2,8,8]

  '''
    # insert here your code
  dix = {}
  for v in copy.copy(mylist):
    if isinstance(v, str):
      mylist.remove(v)
      if v in dix:
        dix[v] += 1
      else:
        dix[v] = 1
  return dix
  #print(dix)
  #print(mylist)
  #copy() is important because modifying a list while iterating 
  #over it can cause errors or unexpected results,here is the code w/o the copy module:
  '''  dix = {}
  for v in mylist:
    if isinstance(v, str):
      mylist.remove(v)
      if v in dix:
        dix[v] += 1
      else:
        dix[v] = 1
  print(dix)
  print(mylist)'''
if __name__ == "__main__":
  ex54([1,'a',2,'b','a',8,'d',8])
