# Convert first letter of every word to uppercase

text = input("Enter a sentence: ")

words = text.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:].lower() + " "

print("Title Case:", result)
