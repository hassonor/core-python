mylist = ["everybody", "in", "this", "group", "should", "be", "able", "to", "dance", "salsa", "but", "only", "some"
                                                                                                             "can",
          "dance", "bachata"]

my_length = dict()
for word in mylist:
    my_length[word] = len(word)

print(my_length)

my_length2 = {word: len(word) for word in mylist}
print(my_length2)

phrase = ""
for ind, word in enumerate(mylist):
    if ind == 0 or word[-1] == "a":
        phrase += word[0].capitalize() + word[1:]

    else:
        phrase += word

print(phrase)

names = ("Tom", "Daniel", "Ofir", "Ofri", "Andrea", "Silvia", "Manuel", "Jessica")

try:
    with open("file.txt", "w") as f:
        for i in range(0, len(names) - 1, 2):
            temp_tuple = (names[i], names[i + 1])
            f.write(temp_tuple.__repr__() + "\n")

except:
    print("Error...")

# Option 2:
couples = zip(*[iter(names)] * 2)
text = "\n".join(f"{couple[0]}-{couple[1]}" for couple in couples)
try:
    with open("file2.txt", "w") as f:
        f.write(text)
except:
    print("Error...")


def func_a(my_str):
    for _word in my_str.split():
        if _word and _word.endswith("ando"):
            print(_word.lower())


func_a("some word here fando and Fando and ando and PanaNando")


class University:
    def __init__(self, name, location, students):
        if type(name) is str:
            self.name = name
        if type(location) is str:
            self.location = location
        if type(students) is int:
            self.students = students


class OpenUniversity(University):
    def __init__(self, name, location, students, subjects):
        super().__init__(name, location, students)
        if type(subjects) is dict:
            self.subjects = subjects


def func_b(filename):
    all_lines = ""
    open_u = False
    temp_data = list()
    temp_subjects = dict()
    universities = list()

    try:
        with open(filename, "r") as f:
            all_lines = f.readlines()
    except:
        print("Error...")

    for line in all_lines:
        if open_u and "done courses" not in line:
            temp = line.split(",")
            temp_subjects[temp[0]] = int(temp[1].strip())
        elif open_u and "done courses" in line:
            open_u = False
            universities.append(OpenUniversity(temp_data[0], temp_data[1], temp_data[2], temp_subjects))
        elif not open_u and "courses:" in line:
            temp = line.split(",")
            temp_data = [temp[0], temp[1], int(temp[2].split()[0])]
            open_u = True
        else:
            temp = line.split(",")
            universities.append(University(temp[0], temp[1], int(temp[2].strip())))

    print(len(universities))
    print(sum(u.students for u in universities))

    major_count = 0
    major_name = ""

    for un in universities:
        if isinstance(un, OpenUniversity):
            for key, val in un.subjects.items():
                if val > major_count:
                    major_count = val
                    major_name = key
            print(f"{major_name}:{major_count}")
            major_count = 0
            major_name = ""


func_b("universities.txt")
