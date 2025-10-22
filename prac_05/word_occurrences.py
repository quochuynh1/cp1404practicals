"""
Word Occurrences
Estimated: 30 minutes
Actual: 44 minutes
"""

text = input("Text: ")

words = text.split()
# print(words)

word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
# print(word_to_count)

max_word_length = max(len(word) for word in list(word_to_count))

for word in sorted(word_to_count.keys()):
    print(f"{word:{max_word_length}} : {word_to_count[word]}")
