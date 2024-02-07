# Define a list of even numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

# Define a list of odd numbers
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

# Create a list of squares of even numbers between 4 and 16
even_squared = [e ** 2 for e in evens if 4 < e < 16]
print(even_squared)

# Create a list of squares of odd numbers between 3 and 17
odd_squared = [e ** 2 for e in odds if 3 < e < 17]
print(odd_squared)
