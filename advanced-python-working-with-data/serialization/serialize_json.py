import json
import datetime

with open("30DayQuakes.json", "r") as date_file:
    data = json.load(date_file)


def is_big(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 6


def simple_quake(q):
    return {
        "place": q["properties"]["place"],
        "mag": q["properties"]["mag"],
        "link": q["properties"]["url"],
        "date": str(datetime.date.fromtimestamp(int(q["properties"]["time"] / 1000)))
    }


large_quakes = list(filter(is_big, data["features"]))

large_quakes = list(map(simple_quake, large_quakes))

large_quakes_str = json.dumps(large_quakes, sort_keys=True, indent=4)
print(large_quakes_str)

with open("large_quakes.json", "w") as outfile:
    json.dump(large_quakes, outfile, sort_keys=True, indent=4)
