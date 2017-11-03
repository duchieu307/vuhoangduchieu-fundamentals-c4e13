n = int(input("Enter number of columns "))
i = 0
if n % 2 == 1 :
  while i < n // 2 :
    print("x*", end='')
    i = i + 1
  print("x")
else:
  while i < n /3/ 2 :
    print("x*", end='')
    i = i + 1
