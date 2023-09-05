'''Design  function es16(s,k) that receives as input
- a string s of characters 
- an integer k 

and returns the list with the different substrings of s made of
exactly k distinct characters. The list of substrings are ordered
by decreasing lengths and, for equal lengths, in alphabetical
order. The list should not contain duplicates.

Remember that a substring of s is what you can get from s by
eliminating 0 or more characters from the left end and 0 or more
characters from the right end.

For example,
- if  s='aabbb' and k=1
- the function returns the list ['bbb', 'aa', 'bb', 'a', 'b']

- if  s='bcafedg' and k=3
- the function returns the list ['afe', 'bca', 'caf', 'edg', 'fed']

- if s='ccaabbdd' and k=3
- the function returns the list 
  ['aabbdd', 'ccaabb', 'aabbd', 'abbdd', 'caabb', 'ccaab', 'abbd', 'caab']

'''

def es16(s, k):

  #a substring is valid if its set is equal to k
  def is_valid_substring(sub):
    return len(set(sub)) ==  k
  lista= []
  tmp = set()
  for i in range(0, len(s)+1):
    for j in range(i+k, len(s)+1):
      tmp.add(s[i:j])
      if is_valid_substring(s[i:j]):
        lista.append(s[i:j])
  lista = set(lista)
  lista = list(lista)
  sorted_lista = sorted(lista, key=lambda x:(-len(x), x))
  return sorted_lista
if __name__ == '__main__':
  print(es16('aabbb', 1))