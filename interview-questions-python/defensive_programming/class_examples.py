import shelve
import pickle
import os.path
from os import path

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

# Range Example
a, b = 0, 1

# Fibonacci
for num in range(8):
    print(a)
    a, b = b, a + b

for num in range(10, -1, -1):
    print(num)

# Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed
print('orange' in basket)  # fast membership testing
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)  # unique letters in 'a'
print(a - b)  # letters in 'a' but not in 'b'
print(a | b)  # letters in 'a' or 'b' or both
print(a & b)  # letters in both 'a' and 'b'
print(a ^ b)  # letters in a or b but not in both

# Dictionary
"""
clear() - מוחק את תוכן המילון
copy() - מעתיק את המילון 
fromkeys() - יוצר מילון חדש עם סדרת מפתחות וערך נתון
get() - מחזיר את הערך שמתאים למפתח מסוים
items() - מייצר רשימה של 
     tuples 
    מהצורה key-value

keys() - מחזיר רשימה של כל מפתחות המילון
values() - מחזיר רשימה של כל הערכים במילון
pop() - מוחק מהמילון את הערך עם המפתח הנתון
"""
thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}

print(thisdict["Year"])
print(thisdict.get("Year"))  # Here if the key is not exist return None
thisdict["Year"] = 1980
print(thisdict["Year"])

default_value = "Unknown"
new_dict = dict.fromkeys(thisdict, default_value)
print(new_dict)

print(thisdict.items())
print(thisdict.keys())
print(thisdict.values())

# Files
f = open("zip.py", "r")  # Open a file in read mode
# print(f.read())  # read() method return all content of the file in one piece
# print(f.read(5))  # read just 5 chars
print(f.readline())  # read only 1 line
f.close()

# read line by line
f2 = open("tuple.py", "r")
for x in f2:
    print(x)
f2.close()

f3 = open("files.py", "r")
print(f3.readlines())  # list of all lines on the file
f3.close()

f4 = open("files/ex2.txt", "r")
new_dict_2 = {}

for line in f4:
    val, key = line.split("=")
    new_dict_2[val] = int(key)

print(new_dict_2)

# Check before open a file
if path.isfile("files/demofile.txt"):
    # Now open the file
    f = open("files/demofile.txt")
    # Can we really read it?
    if f.readable():
        """Proceed with reading the file"""
    else:
        print("Unable to read file demofile.txt")

else:
    print("File demofile.txt does not exist!")

f5 = open("files/demofile3.txt", "w")
f5.write("Woops! I have deleted the content!\n")
f5.close()

f6 = open("files/demofile2.txt", "a")
f6.write("Now the file has more content!\n")
f6.close()

# Open and read the file after appending
f7 = open("files/demofile2.txt", "r")
print(f7.read())
f7.close()

# Serialization
sh = shelve.open("files/data")
sh["a"] = 97
sh["b"] = "98"
sh.close()

sh = shelve.open("files/data")
print(sh.dict.keys())
sh.close()

foo = [1, 2, 3]
f9 = open("files/data2", "wb")
pickle.dump(foo, f9)
f9.close()

f9 = open("files/data2", "rb")
print(pickle.load(f9))

# Functions
print("Word1", "Word2", "Word3", sep="*")
print("Word1", "Word2", "Word3", end=" ")
print("Word1", "Word2", "Word3")
