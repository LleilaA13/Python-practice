'''
    Design a function ex3(set1, set2) that:
    - takes two sets of natural numbers as input,
    - finds all triples (a,b,c) such that:
      - a, b and c are in set1
      - a < b < c and
      - (a + b + c) is in set2
    - returns the set of all such triples.
    Notice that the returned triples should be represented as tuples in a list. Those
    tuples should be sorted based on the sum of their components in ascending
    order. If two tuples map to an equivalent sum, they should be sorted by ascending
    lexicographic order.
    EXAMPLE:
    Given set1={2, 4, 5, 6, 8, 9} and set2={5, 15, 19, 25}, the function returns the
    following list:
    [(2, 4, 9), (2, 5, 8), (4, 5, 6), (2, 8, 9), (4, 6, 9), (5, 6, 8)]
    '''


def ex3(set1, set2):
  pass



if __name__ == '__main__':
  print(ex3({2,4,5,6,8,9}, {5,15,19,25}))
