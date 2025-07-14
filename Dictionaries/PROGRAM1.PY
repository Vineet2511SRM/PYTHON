# Input
text = input("Enter a string: ")

# Create a dictionary to count word frequency
words = text.split()
word_cnt = {}

for word in words:
    word_cnt[word] = word_cnt.get(word, 0) + 1

# Output
print("Word frequencies:")
for word, count in word_cnt.items():
    print(f"{word}: {count}")
