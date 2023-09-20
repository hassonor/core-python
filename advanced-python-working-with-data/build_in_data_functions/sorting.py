import json

# Sample list of numbers and names
numbers = [41, 52, 18, 17, 23, 31, 15, 7]
names = ["Or", "Hasson", "Adel", "Zach", "Joe", "John", "Stacy"]

# Sort the numbers list and print it
result = sorted(numbers)
print(result)

# Sort the names list in descending order and print it
names.sort(reverse=True)
print(names)

# Open the JSON data file containing earthquake information and load it into the variable "data"
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


# Define a function to extract magnitude from each earthquake data item
def get_mag(data_item):
    magnitude = data_item["properties"]["mag"]

    # If magnitude is None (not provided), set it to 0
    if magnitude is None:
        magnitude = 0

    return float(magnitude)


# Sort the earthquake data based on magnitude in descending order
data["features"].sort(key=get_mag, reverse=True)

# Print the places of the top 10 largest earthquakes based on magnitude
for i in range(0, 10):
    print(data["features"][i]["properties"]["place"])
