import json

# Declare an array with some sample data in it
values = [2.0, 2.5, 5.1, 4.1, 1.8, 1.2, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]

# The min() function finds the minimum value
print(f"The minimum value is: {min(values)}")
print(f"The minimum value is: {min(strings, key=len)}")

# The max() function finds the maximum value
print(f"The minimum value is: {max(values)}")
print(f"The minimum value is: {max(strings, key=len)}")


# define a custom "key" function to extract a data field
def get_mag(data_item):
    magnitude = data_item["properties"]["mag"]
    if magnitude is None:
        magnitude = 0
    return float(magnitude)


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print(data["metadata"]["title"])
print(len(data["features"]))
print(min(data["features"], key=get_mag))
print(max(data["features"], key=get_mag))


