'''Design and implement the function es10(ftext,k) that takes as input
   a text file path and an integer k, and returns a string with length
   k.

   The input text file contains strings of different length (one per
   line and each line ends with '\n'), as the file f9.txt.

   The k characters of the string returned by the function are
   obtained considering all the strings in ftext that are k character
   long.  The i-th character of the string will be the character that
   appears most frequently as the i-th character of the strings with
   length k in ftext. In case of equal occurrences, the first
   character in alphabetical order among the most frequent characters.
   An empty string will be returned if the text file does not contain
   words with length k.

   As an example, for the text file f9.txt and k=3 the function
   returns the string 'are' because in the f9.txt file there are the
   following 4 strings with length 3: tre due amo ora

'''
'''
tre
due
amo
ora
'''



def es10(ftext,k):
   
   text = ''
   lista = []
   result = []
   
   with open(ftext, encoding = 'utf8') as f:
      text = f.read()
   text = text.split('\n')
   
   for x in text:
      if len(x) == k:
         lista.append(x)
         
   if not lista:
         return ""
      
      
   for i in range(k):
      dic = {}
      for word in lista:
         dic[word[i]] = dic.get(word[i], 0) + 1
      
      char = sorted(dic.items(), key = lambda tup: (-tup[1], tup[0]))
      
      result.append(char[0][0])
      
      
   return "".join(result)

   print(lista)

   
      
   #return "".join(final)
if __name__ == "__main__":
   print(es10('ft9.txt', 3))
   
#      charact = max(freq.items(), key = lambda tup: (tup[1],-ord(tup[0])) )[0]
