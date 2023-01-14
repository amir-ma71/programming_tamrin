# Alireza Mohammadi Aghgonei
# 40028441054323
# Sun. 10:10 ~ 12:25

def n_letter_dictionary(myStr):
  lowerStr = myStr.lower()
  allWords = lowerStr.split(" ")

  allLens = []
  for word in allWords:
    lenWord = len(word)
    allLens.append(lenWord)
  allLens.sort()
  
  uniqueLens = {}
  for wLen in allLens:
    uniqueLens[wLen] = []

  for wLen in uniqueLens.keys():
    for word in allWords:
      if (len(word) == wLen):
        if not word in uniqueLens[wLen]:
          uniqueLens[wLen].append(word)
  
  return(uniqueLens)

print(n_letter_dictionary("The python is very good this is test sentence we all love Python Testingg test"))
