import json
import pprint
import datetime


def square_func(x):
    return x ** 2


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


nums = (1, 7, 4, 5, 13, 25, 381, 410, 57, 47)
grades = (81, 89, 91, 77, 78, 62, 67, 97, 74)

squares = list(map(square_func, nums))
print(squares)

grades = sorted(grades)
grades_letters = list(map(to_grade, grades))
print(grades_letters)

# Open the JSON data file containing earthquake information and load it into the variable "data"
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def big_mag(q):
    return q['properties']['mag'] is not None and q['properties']['mag'] >= 6


results = list(filter(big_mag, data["features"]))


def simplify(q):
    return {
        "place": q["properties"]["place"],
        "magnitude": q["properties"]["mag"],
        "date": str(datetime.date.fromtimestamp(q["properties"]["time"] / 1000))
    }


results = list(map(simplify, results))
pprint.pp(results)
