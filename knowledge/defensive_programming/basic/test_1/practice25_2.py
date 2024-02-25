test_str = "Hello World! and Fando and lolando"


def fun(my_str):
    for word in my_str.split():
        if word and word.endswith("ando"):
            print(word.lower())


fun(test_str)


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


def read_file(file_name):
    all_lines = None
    is_open_u = False
    temp_subjects = dict()
    universities = list()
    temp_open_u_data = list()

    try:
        with(open(file_name, "r")) as f:
            all_lines = f.readlines()
    except:
        print("Failed")
        exit(0)

    for line in all_lines:
        if is_open_u and "done courses" not in line and "courses:" not in line:
            subject = line.split(",")
            temp_subjects[subject[0]] = int(subject[1].strip())
        elif is_open_u and "done courses" in line:
            universities.append(
                OpenUniversity(temp_open_u_data[0], temp_open_u_data[1], temp_open_u_data[2], temp_subjects))
            is_open_u = False
        elif not is_open_u and "courses:" in line:
            temp_line = line.split(",")
            temp_open_u_data = [temp_line[0], temp_line[1], int(temp_line[2].split()[0])]
            is_open_u = True
        else:
            temp_line = line.split(",")
            universities.append(University(temp_line[0], temp_line[1], int(temp_line[2].strip())))

    max_count_major = 0
    max_major = ""
    print(len(universities))
    print(sum(u.students for u in universities))

    for u in universities:
        if isinstance(u, OpenUniversity):
            for key, val in u.subjects.items():
                if val > max_count_major:
                    max_count_major = val
                    max_major = key

    print(f"{max_major}: {max_count_major}")


read_file("universities.txt")
