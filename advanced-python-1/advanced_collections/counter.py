# Importing the Counter class from the collections' module.
from collections import Counter

# Sample lists representing students in two different classes.
class1 = ["Or", "Hasson", "Bob", "James", "Chad", "Darcy", "Penny", "Hannah", "Kevin", "James", "Melanie", "Becky",
          "Steve", "Frank"]
class2 = ["Or", "Hasson", "Bill", "Barry", "Cindy", "Debbie", "Frank", "Gabby", "Kelly", "James", "Or", "Hasson", "Joe",
          "Sam", "Tara", "Ziggy"]

# Creating Counter objects for both class1 and class2.
c1 = Counter(class1)
c2 = Counter(class2)

# Printing the number of times "James" appears in class1.
print(c1["James"])

# Printing the total number of students in class1.
print(sum(c1.values()), "students in class 1")

# Updating the c1 counter by adding counts from class2.
# After this operation, c1 will have combined counts from both class1 and class2.
c1.update(class2)
print(sum(c1.values()), "total occurrences of students names in class1 and class2 combined")

# Printing the three most common names and their counts after the update.
print(c1.most_common(3))

# Subtracting the counts of students in class2 from the updated c1 counter.
# This will adjust the counts in c1 based on the occurrences in class2.
c1.subtract(class2)
print(c1.most_common(1))  # Printing the most common name and its count after subtraction.

# Printing common elements between c1 and c2, and their counts.
# This is essentially an intersection of the two counters.
print(c1 & c2)
