# Count frequency of every word in a paragraph

text = input("Enter a paragraph: ")

words = text.lower().split()

frequency = {}

for word in words:
    word = word.strip(".,!?")
    
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")

for word, count in frequency.items():
    print(word, ":", count) 
    