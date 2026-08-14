# Find the frequency of a character in a string

text = input("Enter a string: ")
ch = input("Enter the character to find: ")

count = 0

for c in text:
    if c == ch:
        count += 1

print("Frequency of", ch, "is:", count)