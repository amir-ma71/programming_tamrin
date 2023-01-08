# name : seyed ali mostafavi montazeri
# my Student ID ; 40028441054144
# کلاس برنامه سازی پیشرفته 
# روز یکشنبه ساعت 7:45 دقیقه صبح 

def word_in_sentence(sent,n):
    number_of_n=0
    list_words=[]
    words = sent.split()
    for w in words :
        if len(w)==n:
            number_of_n += 1
            list_words.append(w)

    print("number of words with len", n ,"=",number_of_n)
    print("words are : ", list_words)
sentence = input("type your sent : ")
number = int(input("enter number : "))


word_in_sentence(sent = sentence , n = number)