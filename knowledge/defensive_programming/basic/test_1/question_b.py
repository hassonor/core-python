import re


class University:
    def __init__(self, _name, _location, _students):
        if type(_name) is str:
            self.name = _name
        if type(_location) is str:
            self.location = _location
        if type(_students) is int:
            self.students = _students


class OpenUniversity(University):
    def __init__(self, _name, _location, _students, _subjects):
        super().__init__(_name, _location, _students)

        if type(_subjects) is not dict:
            raise ValueError("")

        self.subjects = _subjects


u = University("Or", "Tel Aviv", 23)


def read_univ_list(filename):
    lines = []
    current_subjects = dict()
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except:
        print("Could not read from file:", filename)
        exit(1)

    openu = False
    current_subjects, current_name, current_location, current_students = {}, "", "", ""
    universities = list()
    for line in lines:
        if line.startswith("done courses") and openu:
            universities.append(OpenUniversity(current_name, current_location, current_students, current_subjects))
            current_subjects = {}
            continue
        elif "courses:" in line and not openu:
            openu = True
            line = line.replace("courses:", "")
            data_fields = re.split(r', \s*', line)
            current_name = data_fields[0]
            current_location = data_fields[1]
            current_students = data_fields[2]
        elif openu:
            students = line.split(",")
            current_subjects[students[0]] = int(students[1])
        else:
            uni = re.split(r',\s*', line)
            universities.append(University(uni[0], uni[1], uni[2]))


def func_f(filename):
    universities_list = []
    open_university_data = []
    subjects = {}
    all_lines = []
    flag = False
    try:
        with open(filename, "r") as f:
            all_lines = f.readlines()
    except:
        print("Could not read from file:", filename)
        exit(1)
    for line in all_lines:
        if flag is False:
            data_to_add = line.split(",")
            if data_to_add[0] == "Open University":
                open_university_data.extend([data_to_add[0], data_to_add[1], int(data_to_add[2].split()[0])])
            else:
                universities_list.append(University(data_to_add[0], data_to_add[1], int(data_to_add[2].strip())))
        if flag is True and "done courses" not in line:
            info_subject = line.split(",")
            subjects[info_subject[0]] = info_subject[1].strip()
        if flag is True and "done courses" in line:
            universities_list.append(
                OpenUniversity(open_university_data[0], open_university_data[1], open_university_data[2],
                               subjects))
            flag = False
        if flag is False and "courses:" in line:
            flag = True

    # Number of Universities
    print(len(universities_list) + 1)

    # Number of Students
    number_of_students = 0
    for university in universities_list:
        number_of_students += university.students

    print(number_of_students)

    # Max Major
    biggest_major = ""
    max_number_of_students = 0
    open_u = None

    for university in universities_list:
        if isinstance(university, OpenUniversity):
            open_u = university
            break
    for major, students in open_u.subjects.items():
        if len(students) > max_number_of_students:
            biggest_major = major
            max_number_of_students = len(students)

    print(biggest_major)


func_f("universities.txt")
# read_univ_list("universities.txt")
