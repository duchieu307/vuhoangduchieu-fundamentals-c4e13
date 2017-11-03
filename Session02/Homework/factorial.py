print("Factorial of n")
n = int(input("Enter n "))
if n < 0:
  print("Factorial of n does not exist")
elif n == 0 :
  print("Factorial of n is 1")
else :
  i = 1
  s = 1
  while i <= n :
    s = s * i
    i = i + 1
  print("Factorial of n is", s)
