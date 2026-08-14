per = float(input("enter percentage:"))
if per >= 90:
    print("excellent performance")
else:
    if per >= 80:
        print(" very good performance")
    else:
        if per >= 70:
            print("good performance")
        else:
            if per >= 60:
                print("average performance")
            else:
                print(" poor performance")