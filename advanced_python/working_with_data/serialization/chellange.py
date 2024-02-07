# Import required modules for handling JSON, CSV, and datetime operations
import json
import csv
from datetime import datetime


# Function to convert Unix timestamp to a date string in the 'YYYY-MM-DD' format
def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')


# Open the JSON file containing quake data and load its content into a Python object
with open("30DayQuakes.json") as date_file:
    data = json.load(date_file)


# Function to retrieve the 'sig' (Significance) field from the quake data
# Replace None with 0
def get_sig(x):
    sig = x["properties"]["sig"]
    return 0 if sig is None else sig


# Sort the quakes by the 'sig' field in descending order
sorted_events = sorted(data["features"], key=get_sig, reverse=True)

# Take the top 40 most significant quakes
top_40_quakes = sorted_events[:40]

# Further sort the top 40 quakes by their timestamp in descending order (most recent first)
top_40_quakes.sort(key=lambda e: e["properties"]["time"], reverse=True)

# Define the headers for the output CSV file
headers = ["Magnitude", "Place", "Felt", "Reports", "Date", "Link"]

# Initialize an empty list to hold the rows for the CSV file
rows = []

# Populate the rows list with relevant data from each of the top 40 quakes
for quake in top_40_quakes:
    rows.append([
        quake["properties"]["mag"],  # Magnitude
        quake["properties"]["place"],  # Location
        quake["properties"]["sig"],  # Significance
        timestamp_to_date(quake["properties"]["time"]),  # Date
        f"https://www.google.com/maps?q={quake['geometry']['coordinates'][1]},{quake['geometry']['coordinates'][0]}"
        # Google Maps link
    ])

# Create and write the gathered data into a CSV file
with open("top_40_large_quakes.csv", "w", newline='') as csvfile:
    # Initialize the CSV writer
    writer = csv.writer(csvfile, delimiter=",")
    # Write the header row to the CSV
    writer.writerow(headers)
    # Write the individual rows of quake data to the CSV
    writer.writerows(rows)
