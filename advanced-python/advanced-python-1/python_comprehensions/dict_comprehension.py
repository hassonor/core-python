# Define a list of temperatures in Celsius
ctemps = [0, 12, 34, 100]

# Create a dictionary that maps Celsius to Fahrenheit for temperatures less than 100
temp_dict = {t: (t * 9 / 5) + 32 for t in ctemps if t < 100}
print(temp_dict)
print(temp_dict[34])  # Output the Fahrenheit equivalent of 34C

# Define two dictionaries representing two teams
team1 = {"Jones": 25, "Jameson": 18, "Smith": 57, "Burns": 7}
team2 = {"White": 12, "Macke": 87, "Perce": 3}

# Create a new dictionary by merging team1 and team2
new_team = {k: v for team in (team1, team2) for k, v in team.items()}
print(new_team)
