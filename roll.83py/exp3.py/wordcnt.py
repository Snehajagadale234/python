# Count total number of words in a sentence

text = input("Enter a sentence: ")

words = text.split()

count = 0

for word in words:
    count += 1

print("Total words:", count)