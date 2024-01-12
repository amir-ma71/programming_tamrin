#به نام خدا
#صدیقه دیانت 40028441054056
#کلاس یکشنبه ساعت 7:45
#برنامه محاسبه وام طبق فرمول



def payEachMonth(principal: float, annual_interest_rate: float  , duration: int ):
  monthly_rate = (annual_interest_rate / 100) / 12
  i = duration * 12

  if (monthly_rate == 0):
    return principal / i

  else:
    return (principal*(monthly_rate*(1+monthly_rate)**i)) / (((1+monthly_rate)**i) - 1)


num1 = float(input("enter principal : "))
num2 = float(input("enter annual_interest_rate : "))
num3 = int(input("enter duration : "))

monthlyPayment = payEachMonth(num1,num2,num3)
print(monthlyPayment)