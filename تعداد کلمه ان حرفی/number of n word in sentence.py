def word_in_sentence(sent,number):
    number_of_n = 0
    list_word = []
    words = sent.split()
    for w in words :
        if len(w)== number :
            number_of_n += 1
            list_word.append(w)
    print("number of words whit len ", number," = ",number_of_n)
    print("words are : ",list_word)

tex=input("type your sent : ")
number=int(input("enter number : "))

word_in_sentence(tex , number)
