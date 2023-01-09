# name : seyed ali mostafavi montazeri
# my Student ID ; 40028441054144
# کلاس برنامه سازی پیشرفته 
# روز یکشنبه ساعت 7:45 دقیقه صبح 


# inputs
input_number = int(input("Please, Enter your integer number : "))

# Variables
star = "*" * input_number
counter = 0

# Loops
for i in star:
    counter += 1
    print(star[0:counter])

for i in star:
    counter -= 1
    print(star[0:counter])


