days_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
days_he = ["ראשון", "שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת"]

with open("testfile.txt", "r") as fp:
    for line in iter(fp.readline, ''):
        print(line)

for day in days_en:
    print(day)

for index, day in enumerate(days_en):
    print(index, day)

for index, day in enumerate(zip(days_en, days_he), start=1):
    print(index, day[0], "=", day[1], "in Hebrew")
