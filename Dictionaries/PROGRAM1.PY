# Input
text = input("Enter a string: ")

# Create a dictionary to count word frequency
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Output
print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
