# n = int(input("n "))
# for i in range(0, n, 2):
#     # range(start, stop, step)
#     print(i, end=', ')

n = int(input("n "))
for i in range(n):
    # i la bien gan voi cac gia tri cua n
    if i % 2 == 0 :
        print("Fizz")
    elif i % 3 == 0 :
        print("buzz")
    else i % 2 % 3 == 0 :
        print("Fizzbuzz")
