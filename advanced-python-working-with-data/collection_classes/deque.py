# importing the collections module to use data structures like deque
import collections
# importing the string module to get access to string constants like ascii_lowercase
import string

# Initializing a deque with lowercase alphabets
d = collections.deque(string.ascii_lowercase)

# Printing the count of items in the deque
print(f"Item Count: {len(d)}")

# Looping through each element in the deque and printing its uppercase version
for element in d:
    print(element.upper())

# Removing the item from the rightmost end of the deque
d.pop()
# Removing the item from the leftmost end of the deque
d.popleft()
# Adding the integer 7 to the rightmost end of the deque
d.append(7)
# Adding the integer 1 to the leftmost end of the deque
d.appendleft(1)

# Printing the modified deque after the above operations
print(d)

# Rotating the deque one step to the right
# After rotation, the rightmost item becomes the first item of the deque
d.rotate(1)
print(d)
