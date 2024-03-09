def func_a(my_str):
    for word in my_str.split():
        if word and word.endswith("ing"):
            print(word[0].upper() + word[1:])


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
    lines = list()
    investment_account = False
    data_temp = list()
    investments_temp = dict()
    accounts = list()

    try:
        with open(filename, "r") as f:
            lines = f.readlines()

    except:
        print("Error....")
        exit(1)

    for line in lines:
        if not investment_account and "investments:" in line:
            investment_account = True
            temp = line.split()
            data_temp = [temp[0], float(temp[1])]
        elif investment_account and "done investments" not in line:
            temp = line.split()
            investments_temp[temp[0]] = float(temp[1].strip())
        elif investment_account and "done investments" in line:
            investment_account = False
            accounts.append(InvestmentAccount(data_temp[0], data_temp[1], investments_temp))
        else:
            temp = line.split()
            accounts.append(BankAccount(temp[0], float(temp[1].strip())))

    print(len(accounts))
    print(sum(ac.balance for ac in accounts))

    for account in accounts:
        print(f"{account.name} - {account.balance}")
        if isinstance(account, InvestmentAccount):
            for key, val in account.investments.items():
                print(f"{key}:{val}")


func_b("bank.txt")


def func_c(my_str):
    for word in my_str.split():
        if word and word.endswith("ando"):
            print(word.lower())


func_c("some word here fando and Fando and ando and PanaNando")


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


def func_d(filename):
    lines = list()
    universities = list()
    temp_data = list()
    temp_subjects = dict()
    is_openu = False

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except:
        print("Error...")
        exit(1)

    for line in lines:
        if not is_openu and "courses:" in line:
            is_openu = True
            temp = line.split(",")
            temp_data = [temp[0], temp[1], int(temp[2].split()[0])]
        elif is_openu and "done courses" not in line:
            temp = line.split(",")
            temp_subjects[temp[0]] = int(temp[1].strip())
        elif is_openu and "done courses" in line:
            is_openu = False
            universities.append(OpenUniversity(temp_data[0], temp_data[1], temp_data[2], temp_subjects))
        else:
            temp = line.split(",")
            universities.append(University(temp[0], temp[1], int(temp[2].strip())))

    print(len(universities))
    print(sum(u.students for u in universities))

    major = ""
    max_major = 0

    for un in universities:
        if isinstance(un, OpenUniversity):
            for key, val in un.subjects.items():
                if val > max_major:
                    max_major = val
                    major = key
            print(f"{major}:{max_major}")
            max_major = 0
            major = ""


func_d("universities.txt")


class Book:
    def __init__(self, name, author, year):
        if type(name) is str:
            self.name = name
        if type(author) is str:
            self.author = author
        if type(year) is int:
            self.year = year


def new_init(self, name, author, year, openu_id):
    Book.__init__(self, name, author, year)
    if type(openu_id) is int:
        self.openu_id = openu_id


# cls = input("Insert a classname")
cls = "newClassBook"

new_cls = type(cls, (Book,), {"__init__": new_init})

instance_new_class = new_cls("Some book", "Some author", 2000, 20535)

print(instance_new_class.openu_id)

mylist = ["everybody", "in", "this", "group", "should", "be", "able", "to", "dance", "salsa", "but", "only"
    , "some", "can", "dance", "bachata"]

my_length = {word: len(word) for word in mylist}

phrase = ""

for ind, word in enumerate(mylist):
    if ind == 0 or word[-1] == 'a':
        phrase += word[0].upper() + word[1:]
    else:
        phrase += word

print(phrase)


def func_e(my_str):
    for word in my_str.split():
        if word and word.startswith("pre"):
            print(word.upper())


func_e("Hello World\n prem\n preL my name is <NAME> preKa ApreKa")

names = ("Tom", "Daniel", "Ofir", "Ofri", "Andrea", "Silvia", "Manuel", "Jessica")

couples = zip(*[iter(names)] * 2)

text = "\n".join(f"{couple[0]}-{couple[1]}" for couple in couples)

with open("test93.txt", "w") as f:
    f.write(text)

names = ("Tom", "Daniel", "ofir", "Ofri", "Andrea", "Silvia", "Manuel", "Jessica")

with open("test93_2.txt", "w") as f:
    for i in range(0, len(names) - 1, 2):
        f.write(f"({names[i]},{names[i + 1]})\n")
