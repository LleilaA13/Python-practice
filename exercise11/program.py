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



def es10(ftext,k):
   count = []
   with open(ftext, encoding='utf8') as f:
      for line in f:
         for i in range(len(line)):
            if len(line[i]) == k:
               count.append(line[i])
               
   if not count:
      return ""
   
   result = []  
      
   for char in range(k):
      w = []
      for word in count:
         w.append(word[char])
         
      freq = {
         c : w.count(c) for c in w
      }
      charact = max(freq.items(), key = lambda tup: (tup[1],-ord(tup[0])))[0]
      result.append(charact)
   return "".join(result)

if __name__ == "__main__":
   print(es10('ft9.txt', 33))
   
#      charact = max(freq.items(), key = lambda tup: (tup[1],-ord(tup[0])) )[0]