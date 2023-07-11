
import os
import os.path


def es68(dirname, extensions):
    count = {ext: 0 for ext in extensions}
    for f in os.listdir(dirname):
        fn = os.path.join(dirname, f)
        if os.path.isdir(fn):
            diz = es68(fn, extensions)
            for k, v in diz.items():
                count[k] += v
        else:
            for ext in extensions:
                if fn.endswith(ext):
                    count[ext] += 1
    for k in list(count.keys()):
        if count[k] == 0:
            del count[k]
    return count

'''
count = {ext:0 for ext in extensions}
#initializing a dictionnary using a dictionnary comprehension. 
#the keys of 'count' are the extensions provided in the 'extensions' list,
#and the initial count for each extension is set to 0.
for f in os.listdir(dirname): #iterates over the files and directories spec. in dirname using the method. f represents each file or directory
fn = os.path.join(dirname,f) #constructs the full path of the curr file or directory by using the method and assings it to fn.
if os.path.isdir(fn): #if the current item ('fn') is a directory, it recursively calls the function on that directory w/ the same set of exts.
    diz = es68(fn, extensions) #the returned result is sotred in 'diz'
    for k,v in diz.items(): #iterates over the k-v pairs in the dict obtained from the rec. call. It adds the values to the corr. ext. in the 'count'
    count[k] += v
else:
    for ext in extensions: #iterates over exts in extensions list, 
    if fn.endswith(ext):#if the file's name ends w/ it, it increments the count of that ext. in the count dict
        count[ext] += 1
for k in list(count.keys()): #after processing the files and directories in 'dirname',
if count[k] == 0:
    del count[k] #it removes keys from 'count' for which the count is 0
return count
'''