# Import necessary modules: csv for reading CSV files and pprint for pretty-printing
import csv
import pprint

# Initialize an empty list to hold the parsed data from the CSV file
result = []

# Open the CSV file containing the large earthquake data
with open("large_quakes.csv", "r") as csvfile:
    # Initialize a CSV reader object
    reader = csv.reader(csvfile)

    # Initialize a CSV Sniffer object to infer the CSV dialect and detect headers
    sniffer = csv.Sniffer()

    # Read a sample from the file to use for sniffing
    sample = csvfile.read(1024)

    # Move back to the beginning of the file before we start reading rows
    csvfile.seek(0)

    # Check if the CSV file has a header and skip it if it does
    if sniffer.has_header(sample):
        next(reader)

    # Iterate through each row in the CSV
    for row in reader:
        # Append each row as a dictionary to the result list
        result.append(
            {
                "place": row[0],
                "magnitude": row[1],
                "date": row[2],
                "link": row[3]
            }
        )

# Pretty-print the list of dictionaries
pprint.pp(result)
