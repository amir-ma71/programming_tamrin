# Alireza Mohammadi-A
# Sun. 10:10 ~ 12:25

def calcMonthlyPayment(principal: float, duration: int, annual_interest_rate: float = 0.0):
  monthly_rate = (annual_interest_rate / 100) / 12
  n = duration * 12
  if (monthly_rate == 0):
    return principal / n
  else:
    return (principal*(monthly_rate*(1+monthly_rate)**n)) / (((1+monthly_rate)**n) - 1)


monthlyPayment = calcMonthlyPayment(1000.0, 5, 4.5)
print(monthlyPayment)