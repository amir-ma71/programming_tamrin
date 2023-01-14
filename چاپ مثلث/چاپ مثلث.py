#به نام خدا
#صدیقه دیانت 40028441054056
#کلاس یکشنبه ساعت 7:45
#برنامه به تعداد عد عدد دریافتی مثلث ستاره ای چاپ کند
# رجوع به سایت https://pynative.com

def nStarToTriangle(number):
  for N in range(number):

    for M in range(N+1):
      print("*", end="")
    print("\r") 

  for N in range(number-1, 0, -1):
    #then
    for M in range(N):
      print("*", end="")
    print("\r")


number1 = int(input("Enter a number more than 2: "))

if (number1 < 3):
  while (entered_number < 3):
    print("Entered number must be more than 2 . try next time ")
else:
  nStarToTriangle(number1)
