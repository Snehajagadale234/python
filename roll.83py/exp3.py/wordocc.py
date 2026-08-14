# Count occurrences of a word

text = input("Enter a sentence: ")
word = input("Enter the word to search: ")

words = text.split()

count = 0

for w in words:
    if w == word:
        count += 1

print("Occurrences:", count)
