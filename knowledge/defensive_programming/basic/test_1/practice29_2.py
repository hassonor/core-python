def func(my_str):
    for word in my_str.split():
        if word and word.endswith("ando"):
            print(word.lower())


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
    all_lines = None
    is_open_u = False
    temp_data = list()
    temp_subjects = dict()
    universities = list()

    try:
        with open(filename, "r") as f:
            all_lines = f.readlines()
    except:
        print("Error...")
        exit(1)

    for line in all_lines:
        if not is_open_u and "courses:" in line:
            is_open_u = True
            temp_line = line.split(",")
            temp_data = [temp_line[0], temp_line[1], int(temp_line[2].split()[0])]
        elif is_open_u and "done courses" not in line:
            temp_line = line.split(",")
            temp_subjects[temp_line[0]] = int(temp_line[1].strip())
        elif is_open_u and "done courses" in line:
            is_open_u = False
            universities.append(OpenUniversity(temp_data[0], temp_data[1], temp_data[2], temp_subjects))
        else:
            temp_line = line.split(",")
            universities.append(University(temp_line[0], temp_line[1], int(temp_line[2].strip())))

    print(len(universities))
    print(sum(u.students for u in universities))
    max_major_name = ""
    max_major_count = 0
    all_max_major = list()
    for univ in universities:
        if isinstance(univ, OpenUniversity):
            for key, val in univ.subjects.items():
                if val > max_major_count:
                    max_major_count = val
                    max_major_name = key

            print(f"{max_major_name}:{max_major_count}")

            max_major_count = 0
            max_major_name = ""


func("Hello Fando and Kand Orange and andor and ando")
func_b("universities.txt")

my_list = ["everybody", "in", "this", "group", "should", "be", "able", "to", "dance", "salsa", "but", "only", "some",
           "can", "dance", "bachata"]

my_dict = {f"{word}:{len(word)}" for word in my_list}

print(my_dict)

phrase = ""
for ind, val in enumerate(my_list):
    if ind == 0 or val[-1] == "a":
        phrase += val[0].capitalize() + val[1:]
    else:
        phrase += val

print(phrase)

names = ("Tom", "Daniel", "Ofir", "Ofri", "Andrea", "Silvia", "Manuel", "Jessica")

couples = zip(*[iter(names)] * 2)

text = "\n".join(f"{couple[0]}-{couple[1]}" for couple in couples)

try:
    with open("test1.txt", "w") as f:
        f.write(text)
except:
    print("Error in open/write the file")
    exit(1)

couples = list()
for ind in range(0, len(names) - 1, 2):
    couples.append((names[ind], names[ind + 1]))

try:
    with open("test2.txt", "w") as f:
        for couple in couples:
            f.write(couple.__repr__() + "\n")

except:
    print("Error in open/write the file")
    exit(1)
