def func_a(my_str):
    for word in my_str.split():
        if word and word.endswith("ing"):
            print(word[0].capitalize() + word[1:])


func_a("lkdfjing \n df;askldsflkj algfdsjJing fsdl;kjfsdw;lkING   ;fdlk;\n\n flds")


class BankAccount:
    def __init__(self, name, balance):
        if type(name) is str:
            self.name = name
        if type(balance) is float:
            self.balance = balance


class InvestmentAccount(BankAccount):
    def __init__(self, name, balance, investments):
        super().__init__(name, balance)
        if type(investments) is dict:
            self.investments = investments


def func_b(filename):
    all_lines = ""
    is_investment_account = False
    accounts = list()
    temp_data = list()
    temp_investments = dict()

    try:
        with open(filename, "r") as f:
            all_lines = f.readlines()
    except:
        print("Error...")

    for line in all_lines:
        if is_investment_account and "done investments" not in line:
            temp = line.split()
            temp_investments[temp[0]] = float(temp[1].strip())
        elif is_investment_account and "done investments" in line:
            is_investment_account = False
            accounts.append(InvestmentAccount(temp_data[0], temp_data[1], temp_investments))
        elif not is_investment_account and "investments:" in line:
            temp = line.split()
            temp_data = [temp[0], float(temp[1])]
            is_investment_account = True
        else:
            temp = line.split()
            accounts.append(BankAccount(temp[0], float(temp[1].strip())))

    for ac in accounts:
        print(ac.name, end=" ")
        print(ac.balance)
        if isinstance(ac, InvestmentAccount):
            print(ac.name, end=" investments:\n")
            for key, val in ac.investments.items():
                print(f"{key}:{val}")


func_b("bank.txt")


def func_a(my_str):
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
    all_lines = ""
    universities = list()
    temp_data = list()
    temp_subjects = dict()
    is_openu = False

    try:
        with open(filename, "r") as f:
            all_lines = f.readlines()
    except:
        print("Error when opening the file...")
        exit(1)

    for line in all_lines:
        if is_openu and "done courses" not in line:
            temp = line.split(",")
            temp_subjects[temp[0]] = int(temp[1].strip())
        elif is_openu and "done courses" in line:
            universities.append(OpenUniversity(temp_data[0], temp_data[1], temp_data[2], temp_subjects))
            is_openu = False
        elif not is_openu and "courses:" in line:
            temp = line.split(",")
            temp_data = [temp[0], temp[1], int(temp[2].split()[0])]
            is_openu = True
        else:
            temp = line.split(",")
            universities.append(University(temp[0], temp[1], int(temp[2].strip())))

    print(len(universities))
    print(sum(u.students for u in universities))

    major_name = ""
    major_max = 0
    for un in universities:
        if isinstance(un, OpenUniversity):
            for key, val in un.subjects.items():
                if val > major_max:
                    major_name = key
                    major_max = val
            print(f"{major_name}:{major_max}")
            major_max = 0
            major_name = ""


func_b("universities.txt")

mylist = ["everybody", "in", "this", "group", "should", "be", "able", "to", "dance", "salsa", "but",
          "only", "some", "can", "dance", "bachata"]

my_length = {word: len(word) for word in mylist}

print(my_length)

phrase = ""

for ind, val in enumerate(mylist):
    if ind == 0 or val[-1] == 'a':
        phrase += val[0].capitalize() + val[1:]
    else:
        phrase += val

print(phrase)

names = ("Tom", "Daniel", "Ofir", "Ofri", "Andrea", "Silvia", "Manuel", "Jessica")

couples = list()

try:
    with open("Test.txt", "w") as f:
        for i in range(0, len(names) - 1, 2):
            f.write(f"({names[i]},{names[i + 1]})\n")

except:
    print("Error...")
    exit(1)

# Way 2:

couples = zip(*[iter(names)] * 2)

text = "\n".join(f"{couple[0]}-{couple[1]}" for couple in couples)
try:
    with open("Test2.txt", "w") as f:
        f.write(text)

except:
    print("Error...")
    exit(1)
