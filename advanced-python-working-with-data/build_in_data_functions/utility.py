import json

values = [0, 1, 2, 3, 4, 5]

print(any(values))
print(all(values))
print(sum(values))

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Are there any quake reports that were felt by more than 25,000 people?
print(
    any(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > 25000 for quake in data["features"]))

# How many quakes were felt by more than 500 people?
print(sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 500 for quake in data["features"]))

# How many quakes had a magnitude of 6 or larger?
print(sum(quake["properties"]["mag"] is not None and quake["properties"]["mag"] >= 6 for quake in data["features"]))
