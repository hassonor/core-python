# Import the OrderedDict class from the collections module
from collections import OrderedDict

# Initialize a list of tuples, each containing a team name and a tuple of wins and losses
sport_teams = [
    ("Royals", (18, 13)),
    ("Rockets", (25, 6)),
    ("Cardinals", (20, 10)),
    ("Dragons", (22, 8)),
    ("Kings", (15, 15)),
    ("Chargers", (20, 10)),
    ("Jets", (16, 14)),
    ("Warriors", (27, 7))
]

# Sort the teams by the number of wins in descending order
# The lambda function sorts the teams based on the first element (wins) of the second tuple (wins, losses)
sorted_teams = sorted(sport_teams, key=lambda t: t[1][0], reverse=True)

# Create an ordered dictionary with the sorted teams
teams = OrderedDict(sorted_teams)
print(teams)

# Remove and return the first item in the ordered dictionary (the team with the most wins)
tm, wl = teams.popitem(False)
print("Top team: ", tm, wl)

# Enumerate and print the remaining teams until the fourth position
for i, team in enumerate(teams, start=1):
    print(i, team)
    if i == 4:
        break

# Initialize two ordered dictionaries and test for equality (Order is important for OrderedDict)
a = OrderedDict({"a": 1, "b": 2, "c": 3})
b = OrderedDict({"a": 1, "c": 3, "b": 2})
print("Equality test:", a == b)

# Initialize two regular dictionaries and test for equality (Order is not important for regular dictionaries)
a = {"a": 1, "b": 2, "c": 3}
b = {"a": 1, "c": 3, "b": 2}
print("Equality test:", a == b)
