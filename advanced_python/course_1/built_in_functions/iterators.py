# Initialize two lists for days of the week in English and Hebrew
days_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
days_he = ["ראשון", "שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת"]

# Open the file "testfile.txt" in read mode and read its contents line by line
with open("testfile.txt", "r") as fp:
    # Loop through each line in the file until an empty line is encountered
    for line in iter(fp.readline, ''):
        # Print the current line
        print(line)

# Loop through and print each day in the English list
for day in days_en:
    print(day)

# Loop through and print each day in the English list along with its index
for index, day in enumerate(days_en):
    print(index, day)

# Loop through and print each day in both the English and Hebrew lists, along with their index, starting from 1
for index, day in enumerate(zip(days_en, days_he), start=1):
    # The variable 'day' is a tuple where day[0] is the day in English and day[1] is the day in Hebrew
    print(index, day[0], "=", day[1], "in Hebrew")
