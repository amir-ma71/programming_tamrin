def word_in_sentence(sent,n):
    number_of_n= 0
    list_words =[]
    words=sent.split()
    for w in words:
        if len (w)==n:
            number_of_n +=1
            list_words.append(w)

    print('number of word with ien ',number,'=',number_of_n)
    print('word are:',list_words)

sentence = input('type your sent')
number=int(input('enter number '))

word_in_sentence (sentence , number)


'[[[[[zahra montaseri ,hamed moayed]]]]]'
