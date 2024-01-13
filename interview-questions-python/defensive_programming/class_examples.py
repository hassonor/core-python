s = "singing in the rain and playing in the rain are two entirely different situations"
vowels = ['a', 'e', 'i', 'o', 'u']

num_vowels = 0

for ch in s:
    if ch in vowels:
        num_vowels += 1

print(num_vowels)

# Oneline Way1
num_vowels = sum(1 for ch in s if ch in vowels)

print(num_vowels)

# Oneline Way2
num_vowels = len([ch for ch in s if ch in vowels])
print(num_vowels)

# Oneline Way3
num_vowels = sum(map(lambda x: 1 if x in vowels else 0, s))
print(num_vowels)

# Exercise 2
sentence = "students flock to the arb for a variety of outdoor activities such as jogging"

same_letter_count = 0
for ele in sentence.split(" "):
    if len(ele) >= 1 and ele[0] == ele[-1]:
        same_letter_count += 1

print(same_letter_count)

# Oneline Way1
same_letter_count = len([ele for ele in sentence.split(" ") if len(ele) >= 1 and ele[0] == ele[-1]])
print(same_letter_count)

# Oneline Way2
same_letter_count = sum(1 for ele in sentence.split(" ") if len(ele) >= 1 and ele[0] == ele[-1])
print(same_letter_count)
