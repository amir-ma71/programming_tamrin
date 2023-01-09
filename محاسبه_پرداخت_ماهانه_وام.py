# name : ali mostafavi 
# کلاس برنامه سازی پیشرفته 
# روز یکشنبه ساعت 7:45 دقیقه صبح 



def loan (prinicipal , annual_interest_rate , duration):

    prinicipal = float(prinicipal)
    annual_interest_rate = float(annual_interest_rate)
    duration = int(duration)
    monthly_payment = float(0.0)
    n = duration*12
    r = (annual_interest_rate/100)/12

    if annual_interest_rate == 0:
        print("ZeroDivisionError")
        monthly_payment = prinicipal/n
    
    else:
        one = ((1+r)**n)
        monthly_payment = (prinicipal*(r*(one)))/ one -1
    print(monthly_payment)

loan(1000.0,4.5,5)