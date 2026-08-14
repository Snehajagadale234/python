a= int(input("enter the first Number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a < b:
    if a < c:
        print("smallest=",a)
    else:
        print("smallest=",c)
else:
    if b < c: 
        print("smallest=",b)
    else: 
        print("smallest=",c)