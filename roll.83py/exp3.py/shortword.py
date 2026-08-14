# Find the shortest word in a sentence

text = input("Enter a sentence: ")

words = text.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)