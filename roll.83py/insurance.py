status = input("enter marital status(married/unmarride):")
if status =="married":
    print("driver is insured")
else:
    gender = input("enter gender (male/female):")
    age = int(input("enter age:"))
    if(gender == "male" and age >30)or(gender == "female" and age >25):
        print("driver is insured")
    else:
        print("driver is not insured")