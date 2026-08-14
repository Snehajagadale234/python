a= int(input("enter the first Number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a > b:
    if a > c:
        print("lagest=",a)
    else:
        print("lagest=",c)
else:
    if b > c: 
        print("largest=",b)
    else: 
        print("largest=",c)