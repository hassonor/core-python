import json
import pprint
import datetime


# Define a function to square a given number
def square_func(x):
    return x ** 2


# Define a function to convert a numerical grade to its letter grade
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


# Sample tuple of numbers
nums = (1, 7, 4, 5, 13, 25, 381, 410, 57, 47)
# Sample tuple of numerical grades
grades = (81, 89, 91, 77, 78, 62, 67, 97, 74)

# Use the map function to square each number in the nums tuple
squares = list(map(square_func, nums))
print(squares)

# Sort the grades and convert each numerical grade to its letter grade
grades = sorted(grades)
grades_letters = list(map(to_grade, grades))
print(grades_letters)

# Open the JSON data file containing earthquake information, and load it into the variable "data"
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


# Define a function to filter events based on their magnitude (return True for events with magnitude 6 and above)
def big_mag(q):
    return q['properties']['mag'] is not None and q['properties']['mag'] >= 6


# Use the filter function to extract events with magnitude 6 and above
results = list(filter(big_mag, data["features"]))


# Define a function to simplify the earthquake data to display place, magnitude, and date
def simplify(q):
    return {
        "place": q["properties"]["place"],
        "magnitude": q["properties"]["mag"],
        # Convert the timestamp to a date string
        "date": str(datetime.date.fromtimestamp(q["properties"]["time"] / 1000))
    }


# Use the map function to apply the simplify function to each event in the results list
results = list(map(simplify, results))
# Pretty print the simplified results
pprint.pp(results)
