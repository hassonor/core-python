import json

# Objectives:
# 1: Determine the total number of earthquakes.
# 2: Count how many earthquakes were reported to be felt by at least 100 people.
# 3: Display the place of the earthquake felt by the most people and its number of reports.
# 4: List the top 10 most significant earthquake events and their significance values.

# Load the earthquake data from the JSON file.
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Q1: Total earthquakes
# Using a generator expression to count earthquakes with a type value.
total_quakes = sum(quake["properties"]["type"] is not None for quake in data["features"])
print(f"Total earthquakes: {total_quakes}")

# Q2: Earthquakes felt by at least 100 people
# Using metadata count for the number of earthquakes felt by at least 100 people.
quake_count = data["metadata"]["count"]
print(f"Earthquakes felt by at least 100 people: {quake_count}")


# Helper function for filtering earthquakes based on felt reports.
def felt_report(q):
    f = q["properties"]["felt"]
    return f is not None and f >= 100


felt_reports = list(map(felt_report, data["features"]))
print(f"Number of quakes felt by at least 100 people: {len(felt_reports)}")


# Q3: Place of the earthquake felt by the most people
# Helper function for extracting the felt value of an earthquake.
def get_felt(q):
    f = q["properties"]["felt"]
    return f if f is not None else 0


# Find the earthquake felt by the most people using the max function and the get_felt helper function.
most_felt_quake = max(data["features"], key=get_felt)
print(f"Place: {most_felt_quake['properties']['title']}, Reports: {most_felt_quake['properties']['felt']}")


# Q4: Top 10 most significant earthquake events
# Helper function for extracting the significance value of an earthquake.
def get_sig(q):
    s = q["properties"]["sig"]
    return s if s is not None else 0


# Sort the earthquake data by significance in descending order.
sig_events = sorted(data["features"], key=get_sig, reverse=True)
for i in range(10):
    print(f"Event: {sig_events[i]['properties']['title']}, Significance: {sig_events[i]['properties']['sig']}")
