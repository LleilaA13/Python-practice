
def es76(word):
    if not word:
        return []
    else:
        return [word] + es76(word[1:])
