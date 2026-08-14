# Find the most frequent character

text = input("Enter a string: ")

max_char = ""
max_count = 0

for ch in text:
    count = text.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch

print("Most Frequent Character:", max_char)
print("Frequency:", max_count)
