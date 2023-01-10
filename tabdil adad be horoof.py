# name : seyed ali mostafavi montazeri
# my Student ID ; 40028441054144
# کلاس برنامه سازی پیشرفته 
# روز یکشنبه ساعت 7:45 دقیقه صبح 




# variable

Numbers = int(input("Enter your number ( between 1 and 9999 ): "))

Numbers_translate = ""
list_numbers = []

list_number_four = []
list_number_three = []
list_number_two = []
list_number_one =[]

four_digits_number = int(Numbers/1000)

three_digits_number = int((Numbers%1000/100))

two_digits_number = int(0)
if 10 < Numbers%100 < 20:
    two_digits_number += int(Numbers%100)
elif (Numbers%100)/10:
    two_digits_number += int((Numbers%100)/10)

one_digits_number = int(Numbers%10)


# list methods

list_numbers.append(four_digits_number)
list_numbers.append(three_digits_number)
list_numbers.append(two_digits_number)
list_numbers.append(one_digits_number)


list_number_four.append(four_digits_number)
list_number_three.append(three_digits_number)
list_number_two.append(two_digits_number)
list_number_one.append(one_digits_number)


# lists
units = [[1,"one "],[2,"two "],[3,"three "],[4,"four "],[5,"five "],[6,"six "],[7,"seven "],[8,"eight "],[9,"nine "]]
eleven = [[11,"eleven "],[12,"twelve "],[13,"thirteen "],[14,"fourteen "],[15,"fifteen "],[16,"sixteen "],[17,"seventeen "],[18,"eighteen "],[19,"nineteen "]]
tens = [[1,"ten "],[2,"twenty "],[3,"thirty "],[4,"forty "],[5,"fifty "],[6,"sixty "],[7,"seventy "],[8,"eighty "],[9,"ninety "]]
hundreds = [[1,"one hundred "],[2,"two hundred "],[3,"three hundred "],[4,"four hundred "],[5,"five hundred "],[6,"six hundred "],[7,"seven hundred "],[8,"eight hundred "],[9,"nine hundred "]]
thousands = [[1,"one thousands "], [2,"two thousands "],[3,"three thousands "],[4,"four thousands "] , [5, "five thousands "],[6,"six thousands "] , [7,"seven thousands "],[8,"eight thousands "],[9,"nine thousands "]]


# convert list to dictionary
units2 = dict(units)
eleven2 = dict(eleven)
tens2 = dict(tens)
hundreds2 = dict(hundreds)
thousands2 = dict(thousands)


for num in list_number_four:
    if num in thousands2.keys():
        Numbers_translate += thousands2.get(num)

for num2 in list_number_three:
    if num2 in hundreds2.keys():
        Numbers_translate += hundreds2.get(num2)
        

for num3 in list_number_two:
    if num3 in tens2.keys():
        Numbers_translate += tens2.get(num3)
        
    
    elif num3 in eleven2.keys():
        Numbers_translate += eleven2.get(num3)

if num3 not in eleven2.keys():
    for num4 in list_number_one:
        if num4 in units2.keys():
            Numbers_translate += units2.get(num4)
            

print("We have converted your entered number into words : ",Numbers_translate)