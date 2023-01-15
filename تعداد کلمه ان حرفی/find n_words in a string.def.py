# Alireza Mohammadi-A
# Sun. 10:10 ~ 12:25

def n_words(str, n):
  words = []
  for word in str.split(" "):
    if (len(word) == n):
      words.append(word)
  print("{} words have length {}:\n".format(len(words), n) + ", ".join(words))


n_words("my name is amir and i love python", 4)

# Output
"""
3 words have length 4:
name, amir, love
"""
