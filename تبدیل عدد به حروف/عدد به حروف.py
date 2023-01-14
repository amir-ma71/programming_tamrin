#به نام خدا
#صدیقه دیانت 40028441054056
#کلاس یکشنبه ساعت 7:45
#برنامه عدد را دریافت و خروجی ان تلفظ اعداد باشد


def numberHub(number):
  num_words = {  
    0: "",  
    1: "one",  
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred"
  }
  result = ""
  counter = 1
  while number > 0:
    r = number % 10 
    if counter < 100:
      result = num_words[r * counter] + " " + result
    else:
      result = num_words[r] + " " + num_words[counter] + " " + result
    number //= 10
    counter *= 10
  return result
  
def numberPronunciation(number):
  thousandMore = ["", "thousand "]
  result = ""
  index = 0
  
  while number > 0:
    remainder = number % 1000
    result = numberHub(remainder) + thousandMore[index] + result
    number //= 1000
    index += 1
  
  return result

number = int(input(" plz enter your number and it should be => (1-9999) : "))
print(numberPronunciation(number))