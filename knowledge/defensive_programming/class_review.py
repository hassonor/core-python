# Class Ex1

s = "singing in the rain and playing in the rain are two entirely different situations"
vowels = ['a', 'e', 'i', 'o', 'u']

# first way
num_vowels = 0
for letter in s:
    if letter in vowels:
        num_vowels += 1

print(num_vowels)

# second way
num_vowels = sum(1 for letter in s if letter in vowels)
print(num_vowels)

# third way
num_vowels = len([1 for letter in s if letter in vowels])
print(num_vowels)

# 2
sentence = "students flock to the arb for a variety of outdoor activities such as jogging"

same_letter_count = 0

# first way
for word in sentence.split(" "):
    if len(word) > 0 and word[0] == word[-1]:
        same_letter_count += 1

print(same_letter_count)

# second way
same_letter_count = sum(1 for word in sentence.split(" ") if len(word) > 0 and word[0] == word[-1])
print(same_letter_count)

# third way
same_letter_count = len([word for word in sentence.split(" ") if len(word) > 0 and word[0] == word[-1]])
print(same_letter_count)

new_dict = {}
with open("file.txt", "r") as f:
    for line in f:
        split_val_and_key = line.split("=")
        new_dict[split_val_and_key[0]] = split_val_and_key[1].strip("\n")

print(new_dict)
