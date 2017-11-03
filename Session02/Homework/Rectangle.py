a = int(input("Enter number of columns "))
b = int(input("Enter number of rows" ))
for i in range(a):
  if i % 2 == 0 :
    for j in range(b):
      if j % 2 == 0 :
        print("x", end='')
      else:
        print("*", end='')
    print()
  else :
    for j in range(b):
      if j % 2 == 0 :
        print("*", end='')
      else:
        print("x", end='')
    print()
    
