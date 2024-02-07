# Import the required modules: json for parsing JSON files and datetime for date manipulation
import json
import datetime

# Open the JSON file containing earthquake data and load it into a Python object
with open("30DayQuakes.json", "r") as date_file:
    data = json.load(date_file)


# Define a function to filter out earthquakes with magnitude greater than 6
def is_big(x):
    # Extract the magnitude from the earthquake data
    mag = x["properties"]["mag"]
    # Return True if magnitude is not None and greater than 6, otherwise return False
    return mag is not None and mag > 6


# Define a function to simplify the earthquake data
def simple_quake(q):
    return {
        # Extract the place of the earthquake
        "place": q["properties"]["place"],
        # Extract the magnitude of the earthquake
        "mag": q["properties"]["mag"],
        # Extract the link to more information about the earthquake
        "link": q["properties"]["url"],
        # Convert the timestamp to a human-readable date
        "date": str(datetime.date.fromtimestamp(int(q["properties"]["time"] / 1000)))
    }


# Filter the original data to keep only large earthquakes (magnitude > 6)
large_quakes = list(filter(is_big, data["features"]))

# Simplify the earthquake data using the simple_quake function
large_quakes = list(map(simple_quake, large_quakes))

# Convert the simplified data to a JSON-formatted string, sorted and indented for readability
large_quakes_str = json.dumps(large_quakes, sort_keys=True, indent=4)

# Print the JSON string to the console
print(large_quakes_str)

# Save the simplified and filtered earthquake data to a new JSON file
with open("large_quakes.json", "w") as outfile:
    # Save the simplified and filtered earthquake data to a new JSON file.
    # - `large_quakes` is the Python object containing the data to be written.
    # - `outfile` is the file object representing the output file.
    # - `sort_keys=True` sorts the keys in ascending order for readability.
    # - `indent=4` indents nested structures by 4 spaces for better formatting.
    json.dump(large_quakes, outfile, sort_keys=True, indent=4)
