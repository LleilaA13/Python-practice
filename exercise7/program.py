"""Design a function es68(dirname, extensions) such that:
- it is recursive or uses recursive functions(s)/method(s),
- it receives as arguments:
  - a directory pathname 'dirname', 
  - a list of strings 'extensions' representing the ending part of
    filenames, a list of strings 'words' that do not contain
  - spaces/tab/newlines
- it counts how many files ending with any of the given extensions
  can be found in 'dirname' or any of its subdirectories.
- it returns a dictionary where:
  - the keys are the extensions passed as argument, if at least
    one file ending with such an extension can be found, and
  - the related values are the number of files whose name ends
    with such a keys.

Note: if no file can be found ending with a given extension, such
a key is not included in the returned dictionary.
"""
# insert here your code



import os
import os.path
#The code recursively traverses the directory tree, counting the number of files with specific extensions in the specified directory and its subdirectories. 
# #It uses a dictionary to store the counts, where each key is an extension,
# #and the corresponding value is the count of files with that extension.

def es68(dirname, extensions):
  count = {ext : 0 for ext in extensions}
  for f in os.listdir(dirname):
    fn = os.path.join(dirname,f)
    if os.path.isdir(fn):
      diz = es68(fn, extensions)
      for k,v in diz.items():
        count[k] += v
    else:
      for ext in extensions:
        if fn.endswith(ext):
          count[ext] += 1
  for k in list(count.keys()):
    if count[k] == 0:
      del count[k]
  return count