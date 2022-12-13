# Alireza Mohammadi-A
# Sun. 10:10 ~ 12:25

def toWords(num: int):
  words = {
      1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
      10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
      20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
  }

  # 1 - 20
  if (num < 20):
    return words[num]

  # 21 - 99
  elif (num < 100):
    # tens only (30,40,50, ...)
    if (num % 10 == 0):
      return words[num]
    # tens with ones
    else:
      return words[num // 10 * 10] + ' ' + words[num % 10]

  # 100 - 999
  elif (num < 1000):
    hundred = words[num // 100] + ' ' + 'hundred'
    # hundreds only (100,200,300, ...)
    if (num % 100 == 0):
      return hundred
    # hundreds with tens and ones
    else:
      return hundred + ' ' + toWords(num % 100)

  # 1000 - 9999
  elif (num <= 9999):
    str = words[num // 1000] + ' ' + 'thousand'
    # thousands only (1000,2000,3000, ...)
    if (num % 1000 == 0):
      return str
    # thousands with hundreds and tens and ones
    else:
      return str + ' ' + toWords(num % 1000)


entered_number = int(input("Enter a number(1<n<9999): "))
number_in_word = toWords(entered_number)
print(number_in_word)
