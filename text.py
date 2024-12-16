def weird(items =[]):
    items.append(1)
    return items
A = weird()
A = weird()
A = weird()
print(A)


str1 = str("James")
str2 = "James"

print(str1 is str2)
print(str1 == str2)