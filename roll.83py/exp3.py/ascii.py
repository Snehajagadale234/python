# Display each character with its ASCII value

text = input("Enter a string: ")

for ch in text:
    print(ch, ":", ord(ch))