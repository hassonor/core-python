import json
import datetime

with open("30DayQuakes.json", "r") as date_file:
    data = json.load(date_file)


def is_big(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 6
