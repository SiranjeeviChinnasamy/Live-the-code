def myfunc(word):
 new_word=""
 for index, item in enumerate (word):
     if index % 2 == 0:
         new_word = new_word + item.upper()
     else :
         new_word = new_word + item.lower()
 return new_word 
print (myfunc('siranjeevi'))
