# Reverse the order of words in a sentence

text = input("Enter a sentence: ")

words = text.split()
result = ""

for i in range(len(words) - 1, -1, -1):
    result += words[i] + " "

print("Reversed sentence:", result)
