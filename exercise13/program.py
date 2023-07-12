'''Design a function ex11(textfile) such that:
  - it receives as argument the path of a text file that contains
    in each line a distinct string of characters
  - it returns a dictionary having strings as keys and string lists as
    values.
  The dictionary keys are the strings contained in the 'textfile',
  without any vowel and with the remaining characters sorted in
  alphabetical order (for example, the string 'angel' generates the
  key 'ngl').
  The corresponding value of a key is the list of strings of
  'textfile' that generated that key (note that different strings can
  generate the same key as for 'car', 'core' and 'cure').  The strings
  in the list are sorted by decreasing length and, with equal lengths,
  in alphabetical order.

  Example: for the text file f10.txt, the function returns the
  dictionary:
      {'prt': ['parto', 'porta'], 
      'r': ['era', 'ora'], 
      'pr': ['arpia', 'arpa'], 
      'cs': ['casa', 'cosa'], 
      'fll': ['follia', 'fallo', 'folla'], 
      'rt': ['otre', 'tre'], 
      'lp': ['piolo', 'polo']
      }
'''


def ex11(textfile):

    # insert your code here
    diz = {}
    with open(textfile, encoding='utf8') as f:
        for word in f:
            word = word.rstrip()

            if not word:
                continue

            stripped = "".join(sorted([
                c for c in word if c not in "aeiou"
            ]))

            diz[stripped] = diz.get(stripped, [])
            diz[stripped].append(word)

    diz = {
        k: sorted(v, key=(lambda s: (-len(s), s))) for k, v in diz.items()
    }

    return diz


if __name__ == "__main__":

    print(ex11('ft10a.txt'))
