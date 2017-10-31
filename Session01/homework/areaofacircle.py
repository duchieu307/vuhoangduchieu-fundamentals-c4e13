print("The area of a circle")
r = float(input("Enter radius")) 
if r < 0 :
    print("The radius input must > 0")
else :
        s = 3.14 * r**2
        print("The area of a circle is s = {0}".format(s),"unit area")
