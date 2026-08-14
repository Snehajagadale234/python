# Remove all spaces from the input string

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch != " ":
        result += ch

print("String without spaces:", result)