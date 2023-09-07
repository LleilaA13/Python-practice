

def es50(s, k):
    '''Write the function es50(s,k) that: 

      - receives as an input a string s of characters that are the
        digits from '0' to '9' and an integer k

      - builds the list of all the different substrings of s, with
        length k, whose characters are in a striclty increasing order

      and returns the list of such substrings, ordering the items in a
      descreasing order.

    Note that the list must not contain duplicates.

    Remember that a substring is what you get from s by deleting 0 or
    more initial characters and 0 or more final characters.

    EXAMPLES: 

    with s='9135918246556' and k=3 the function returns the list
    ['359','246', 135']

    with s='1234123412341234' and k=3 the function returns the list
    ['234',123']

    with s='987654321' and k=3 the function returns the list []

    '''
    # enter your code here

    unique_substrings = set()
    
    for i in range(len(s) - k + 1):
      sub = s[i:i+k]
      if all(sub[j] < sub[j+1] for j in range(k-1)):
        unique_substrings.add(sub)
        
    result = sorted(list(unique_substrings), reverse=True)
    return result
if __name__ == '__main__':
    es50('9135918246556', 3)
