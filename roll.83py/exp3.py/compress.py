# String Compression

text = input("Enter a string: ")

result = ""
count = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        result += text[i] + str(count)
        count = 1

result += text[-1] + str(count)

if len(result) < len(text):
    print("Compressed String:", result)
else:
    print("Original String:", text)
    