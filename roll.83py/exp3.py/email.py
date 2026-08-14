# Validate email format

email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") > 0:
    print("Valid Email")
else:
    print("Invalid Email")

