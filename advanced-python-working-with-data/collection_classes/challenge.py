# Importing required libraries
import json
from collections import Counter, defaultdict

# Open the JSON data file containing earthquake information and load it into the variable "data"
with open("30DayQuakes.json", "r") as datafile:
    # Using json.load() to parse the JSON from the file into a Python dictionary
    data = json.load(datafile)

# First Way to Solve
# ------------------------------------------
# Using a list comprehension to extract 'type' values from each feature in the data
types_list = [feature['properties']['type'] for feature in data['features']]

# Using the Counter class to count occurrences of each 'type'
c = Counter(types_list)

# Printing the counts
print(c)

# Second Way to Solve
# ------------------------------------------
# Using a defaultdict to initialize the counts to 0 for each 'type'
totals = defaultdict(int)

# Iterating over each feature/event in the data
for event in data['features']:
    # Incrementing the count for the specific 'type' by 1
    totals[event['properties']['type']] += 1

# Printing out the counts for each 'type' in a formatted manner
for k, v in totals.items():
    print(f"{k:15}: {v}")
