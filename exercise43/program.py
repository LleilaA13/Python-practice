import os
import os.path


def es70(dirname, extensions, words):
    """Design a function es70(dirname, extensions, words) such that:
    - it is recursive or uses recursive functions(s)/method(s),
    - it receives as arguments:
      - a directory pathname 'dirname', 
      - a list of strings 'extensions' representing the ending part of
         filenames,
      - a list of strings 'words' that do not contain spaces nor tab
        nor newlines
    - it counts how many times the strings in 'words' are present in
      the files which name does NOT end with any of the indicated
      extensions, ignoring any distingcion between upper and lower
      case,
    - it returns a dictionary where:
       - the keys are the searched words in lower case
       - the related values are the number of times (>0) that the
          word appear (regardless of upper/lower case) overall the files
          which name does not end with any of the given extensions.

    Note: if a word only appears in files ending with the given
    extensions, it is not included in the dictionary.

    Note: assume that all the files in 'dirname' and its
    subdirectories are text files regardless of their extension.

    """
    # insert here your code
