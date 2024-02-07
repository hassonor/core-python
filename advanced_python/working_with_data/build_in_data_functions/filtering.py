import json


# Define a function to filter out even numbers (return True for odd numbers)
def filter_evens(x):
    if x % 2 == 0:
        return False
    return True


# Define a function to filter out uppercase characters (return True for lowercase characters)
def filter_uppers(x):
    if x.isupper():
        return False
    return True


# Sample tuple of numbers
nums = (1, 7, 4, 5, 11, 13, 26, 381, 411, 58, 46)
# Sample string of characters
chars = "abcDeFgHiJKlmNoP"

# Use the filter function to extract only odd numbers from the nums tuple
odds = list(filter(filter_evens, nums))
print(odds)

# Use the filter function to extract only lowercase characters from the chars string
lowers = list(filter(filter_uppers, chars))
print(lowers)

# Open the JSON data file containing earthquake and other event information, and load it into the variable "data"
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


# Define a function to filter out earthquake events (return True for non-earthquake events)
def not_earthquake(q):
    if q["properties"]["type"] == "earthquake":
        return False
    return True


# Use the filter function to extract only non-earthquake events from the data
events = list(filter(not_earthquake, data["features"]))
print(f"Total non-quake events: {len(events)}")

# Print the types of the first 10 non-earthquake events
for i in range(0, 10):
    print(events[i]["properties"]["type"])
