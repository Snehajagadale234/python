# Find the second most frequent character

text = input("Enter a string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

first = second = ""
first_count = second_count = 0

for ch in freq:
    if freq[ch] > first_count:
        second = first
        second_count = first_count
        first = ch
        first_count = freq[ch]
    elif freq[ch] > second_count:
        second = ch
        second_count = freq[ch]

print("Second Most Frequent Character:", second)
print("Frequency:", second_count)
