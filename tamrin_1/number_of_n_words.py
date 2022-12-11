

def word_in_sentence(sent,number):
    
    number_of_n = 0
    list_words = []
    words = sent.split()
    for w in words:
        if len(w) == number:
            number_of_n += 1
            list_words.append(w)

    print("number of words with len ",number,"= ",number_of_n)
    print("words are: ", list_words)

sentence = input("type your sent ")
number = int(input("enter number "))



word_in_sentence(sentence, number)
