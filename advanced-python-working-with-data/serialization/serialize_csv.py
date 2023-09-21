# Import necessary modules
import csv
import json
import datetime

# Open and read the JSON data file
with open("30DayQuakes.json", "r") as datafile:
    # Load JSON data into a Python object
    data = json.load(datafile)


# Define a function to filter out earthquakes with magnitude greater than 5
def is_big(x):
    # Extract the magnitude value
    mag = x["properties"]["mag"]
    # Check if the magnitude value is not None and greater than 5
    return mag is not None and mag > 5


# Use the filter function to create a list of large earthquakes
large_quakes = list(filter(is_big, data["features"]))

# Define the headers for the CSV file
headers = ["Place", "Magnitude", "Link", "Date"]
# Initialize an empty list to hold the rows of data for the CSV file
rows = []

# Loop through the list of large earthquakes to populate the rows list
for quake in large_quakes:
    # Convert timestamp to date
    the_date = datetime.date.fromtimestamp(int(quake["properties"]["time"] / 1000))
    # Append relevant data to the rows list
    rows.append([quake["properties"]["place"], quake["properties"]["mag"], quake["properties"]["url"], the_date])

# Open a new CSV file to write the filtered earthquake data.
# Adding newline='' to ensure that rows don't have extra newlines
with open("large_quakes.csv", "w", newline='') as csvfile:
    # Initialize a CSV writer object
    writer = csv.writer(csvfile, delimiter=",")
    # Write the header row to the CSV file
    writer.writerow(headers)
    # Write the rows of data to the CSV file
    writer.writerows(rows)
