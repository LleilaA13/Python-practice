'''
define the recursive function (or one that uses a recursive function) Suffix(word), which taken as input a string of characters and returns the list of word suffixes

the elements of the list must be ordered by decreasing length

a word suffix is one which is obtained by deleting 0 or more characters from the initial word

for example, Suffix('foundations') will return:
['foundations', 'oundations', 'undations', 'ndations', 'dations', 'ations', 'tions', 'ions', 'ons', 'ns', 's']
'''


def Suffix(word: str) -> list:
    # define base case first, which is word empty
    if word == "":
        return []
    # now, let's work on the recursive case, when there is a word to 'slice'
    else:
        return [word] + Suffix(word[1:])


if __name__ == "__main__":
    print(Suffix("foundations"))
