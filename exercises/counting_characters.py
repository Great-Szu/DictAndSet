# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
characters_to_skip = [" ", ",", ".", "'"]

for letter in text.lower():
    if letter in characters_to_skip:
        continue
    else:
        word_count[letter] = word_count.get(letter, 0) + 1




# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
