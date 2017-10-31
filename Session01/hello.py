# n = input("what's your name")
# y = int(input("your year of birth"))
# print("hello", n)
# a = 2017 - y
# print("Your age is", a )
# if a < 10 :
#     print("Bạn chưa đủ tuổi để truy cập trang web trên")
# elif a < 18 :
#     print("Đợi lớn một xíu nữa")
# else:
#     print("Bạn đã đủ lớn để các chịu pháp luật địa phương về những dữ liệu trong trang web này")
print("Phuong trinh bac 2: ax^2 + bx + c")
a = float(input("Nhap bien a"))
if a == 0 :
    print("day khong phai phuong trinh bac 2")
else :
    b = float(input("Nhap bien b"))
    c = float(input("Nhap bien c"))
    delta = b**2 - 4*a*c
    if delta < 0 :
        print("Phuong trinh vo nghiem")
    elif delta == 0 :
        print("Phuong trinh co nghiem kep la",(-b)/2*a )
    else :
         e = delta ** 0.5
         x1 = ((-b) + e) / 2*a
         x2 = ((-b) - e) / 2*a
         print("Phuong trinh co 2 nghiem la x1 ={0}, x2 = {1}".format(x1,x2))
