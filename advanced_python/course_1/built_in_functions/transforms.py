# Define a function to convert a numerical grade to a letter grade
def to_grade(x):
    if x >= 90:
        return "A"
    elif 80 <= x < 90:
        return "B"
    elif 70 <= x < 80:
        return "C"
    elif 65 <= x < 70:
        return "D"
    return "F"


# Initialize a tuple of numerical values
nums = (1, 7, 4, 5, 12, 25, 280, 411, 67, 47)

# Initialize a string of characters
chars = "abcDeFGHIjKlMnOp"

# Initialize a tuple of grades
grades = (81, 90, 94, 77, 60, 66, 99, 75)

# Filter out the odd numbers from the tuple 'nums'
# lambda function checks if the remainder of x divided by 2 is not 0
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)

# Filter out the lowercase characters from the string 'chars'
# lambda function uses the islower() method to check if a character is lowercase
lowers = list(filter(lambda ch: ch.islower(), chars))
print(lowers)

# Square each element in the tuple 'nums'
# lambda function multiplies each element by itself
squares = list(map(lambda x: x * x, nums))
print(squares)

# Sort the grades tuple in descending order
grades = sorted(grades, reverse=True)

# Convert numerical grades to letter grades using the to_grade function
letters = list(map(to_grade, grades))
print(letters)
