def func1(my_str):
    for word in my_str.split():
        if word and word.endswith("ando"):
            print(word.lower())


func1("Hello Fando and Kand Orange and andor and ando")


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


#
# def func2(filename):
#     all_lines = None
#     is_open_u = False
#     temp_open_u_data = list()
#     temp_subjects = dict()
#     universities = list()
#
#     try:
#         with open(filename, "r") as f:
#             all_lines = f.readlines()
#     except FileExistsError as e:
#         print("Error...")
#         exit(0)
#
#     for line in all_lines:
#         if is_open_u and "done courses" not in line:
#             temp_subject = line.split(",")
#             temp_subjects[temp_subject[0]] = int(temp_subject[1].strip())
#         elif is_open_u and "done courses" in line:
#             universities.append(
#                 OpenUniversity(temp_open_u_data[0], temp_open_u_data[1], temp_open_u_data[2], temp_subjects))
#             is_open_u = False
#         elif "courses:" in line:
#             temp = line.split(",")
#             temp_open_u_data = [temp[0], temp[1], int(temp[2].split()[0])]
#             is_open_u = True
#         else:
#             temp = line.split(",")
#             universities.append(University(temp[0], temp[1], int(temp[2].strip())))
#
#     print(len(universities))
#     print(sum(u.students for u in universities))
#     max_major_count = 0
#     max_major_name = ""
#     for u in universities:
#         if isinstance(u, OpenUniversity):
#             for key, val in u.subjects.items():
#                 if val > max_major_count:
#                     max_major_count = val
#                     max_major_name = key
#
#     print(f"{max_major_name}: {max_major_count}")


def fun_b(filename):
    all_lines = None
    is_openu = False
    temp_data_openu = list()
    temp_subjects_openu = dict()
    universities = list()

    try:
        with open(filename, "r") as f:
            all_lines = f.readlines()

    except:
        print("Error...")
        exit(1)

    for line in all_lines:
        if not is_openu and "courses:" in line:
            is_openu = True
            temp = line.split(",")
            temp_data_openu = [temp[0], temp[1], int(temp[2].split()[0])]
        elif is_openu and "done courses" not in line:
            temp = line.split(",")
            temp_subjects_openu[temp[0]] = int(temp[1].strip())
        elif is_openu and "done courses" in line:
            is_openu = False
            universities.append(
                OpenUniversity(temp_data_openu[0], temp_data_openu[1], temp_data_openu[2], temp_subjects_openu))
        else:
            temp = line.split(",")
            universities.append(University(temp[0], temp[1], int(temp[2].strip())))

    print(len(universities))
    print(sum(u.students for u in universities))
    max_major_subject = ""
    max_major_count = 0
    for u in universities:
        if isinstance(u, OpenUniversity):
            for key, val in u.subjects.items():
                if val > max_major_count:
                    max_major_count = val
                    max_major_subject = key

    print(f"{max_major_subject}:{max_major_count}")


fun_b("universities.txt")

my_list = ["everybody", "in", "this", "group", "should", "be", "able", "to", "dance", "salsa", "but", "only", "some",
           "can", "dance", "bachata"]

my_dict = {f"{word}:{len(word)}" for word in my_list if word}
print(my_dict)

phrase = ""
for index, word in enumerate(my_list):
    if (index == 0 or word[-1] == 'a') and word:
        phrase = phrase + word.capitalize()
    else:
        phrase = phrase + word

print(phrase)

names = ("Tom", "Daniel", "Ofir", "Ofri", "Andrea", "Silvia", "Manuel", "Jessica")

couples = []
for i in range(0, len(names) - 1, 2):
    couples.append((names[i], names[i + 1]))

try:
    with open("results.txt", "w") as f:
        for couple in couples:
            f.write(couple.__repr__() + "\n")

except:
    print("Error...")
    exit(1)

couples = zip(*[iter(names)] * 2)
text = "\n".join(f"{couple[0]}-{couple[1]}" for couple in couples)

try:
    with open("results2.txt", "w") as f:
        f.write(text)
except:
    print("Error...")
    exit(1)

s = "singing in the rain and playing in the rain are two entirely different situations"
vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for ch in s:
    for letter in vowels:
        if ch and letter in ch:
            count = count + 1

print(count)

print(sum(1 for ch in s if ch in vowels))

same_letter_count = 0
sentence = "students flock to the arb for a variety of outdoor activities such as  jogging"
for word in sentence.split():
    if word and word[0] == word[-1]:
        same_letter_count += 1

print(same_letter_count)

print(sum(1 for word in sentence.split() if word and word[0] == word[-1]))
