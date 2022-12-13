# Alireza Mohammadi-A
# Sun. 10:10 ~ 12:25

def print_triangle(n):
  for i in range(n):
    for j in range(i+1):
      print("*", end="")
    print("\r")
  for i in range(n-1, 0, -1):
    for j in range(i):
      print("*", end="")
    print("\r")


entered_number = int(input("Enter a number greater than 2: "))

if (entered_number < 3):
  while (entered_number < 3):
    print("Entered number must be greater than 2!")
    entered_number = int(input("Enter a number (n >= 3):"))
    if (entered_number >= 3):
      print_triangle(entered_number)
else:
  print_triangle(entered_number)
