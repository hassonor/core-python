class Book:
    def __init__(self, title, author, year):
        if type(title) is str:
            self.title = title
        if type(author) is str:
            self.author = author
        if type(year) is int:
            self.year = year


# cls_name = input("Please give a class name")
cls_name = "CoolBook"


def new_init(self, title, author, year, openu_id):
    super(self.__class__, self).__init__(title, author, year)
    self.openu_id = openu_id


cls = type(cls_name, (Book,), {})

# Attach the init method properly to ensure super() works.
cls.__init__ = new_init

book_instance = cls("Some Book", "Some Author", 2023, 20955)
print(book_instance.title, book_instance.author, book_instance.year, book_instance.openu_id)


def func_a(my_str):
    for word in my_str.split():
        if word and word.startswith("pre"):
            print(word.upper())


func_a("Hello World\n prem\n preL my name is <NAME> preKa ApreKa")

mylist = ["everybody", "in", "this", "group", "should", "be", "able", "to", "dance", "salsa", "but", "only",
          "some", "can", "dance", "bachata"]

my_length = {word: len(word) for word in mylist}
print(my_length)

phrase = ""
for ind, word in enumerate(mylist):
    if ind == 0 or word[-1] == 'a':
        phrase += word[0].capitalize() + word[1:]
    else:
        phrase += word

print(phrase)

names = ("Tom", "Daniel", "Ofir", "Ofri", "Andrea", "Silvia", "Manuel", "Jessica")

couples = zip(*[iter(names)] * 2)

text = "\n".join(f"{couple[0]}-{couple[1]}" for couple in couples)

try:
    with open("73_test1.txt", "w") as f:
        f.write(text)
except:
    print("Error something went wrong...")

# Option 2

try:
    with open("73_test2.txt", "w") as f:
        for i in range(0, len(names) - 1, 2):
            f.write(f"({names[i]},{names[i + 1]})\n")

except:
    print("Error something wen wrong...")


def func_c(my_str):
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
    def __init__(self, name, location, students, subjetcs):
        super().__init__(name, location, students)
        if type(subjetcs) is dict:
            self.subjetcs = subjetcs


def func_d(filename):
    all_lines = list()
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
        if not open_u and "courses:" in line:
            temp = line.split(",")
            temp_data = [temp[0], temp[1], int(temp[2].split()[0])]
            open_u = True
        elif open_u and "done courses" not in line:
            temp = line.split(",")
            temp_subjects[temp[0]] = int(temp[1].strip())
        elif open_u and "done courses" in line:
            universities.append(OpenUniversity(temp_data[0], temp_data[1], temp_data[2], temp_subjects))
            open_u = False
        else:
            temp = line.split(",")
            universities.append(University(temp[0], temp[1], int(temp[2].strip())))

    print(len(universities))
    print(sum(u.students for u in universities))

    major_name = ""
    major_count = 0

    for un in universities:
        if isinstance(un, OpenUniversity):
            for key, val in un.subjetcs.items():
                if val > major_count:
                    major_count = val
                    major_name = key
            print(f"{major_name}:{major_count}")
            major_count = 0
            major_name = ""


func_d("universities.txt")


def func_f(my_str):
    for word in my_str.split():
        if word and word.endswith("ing"):
            print(word[0].upper() + word[1:])


func_f("lkdfjing \n df;askldsflkj algfdsjJing fsdl;kjfsdw;lkING   ;fdlk;\n\n flDsing")


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


def func_g(filename):
    lines = list()
    investments_account = False
    temp_data = list()
    temp_investments = dict()
    accounts = list()

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except:
        print("Error...")
        exit(1)

    for line in lines:
        if not investments_account and "investments:" in line:
            investments_account = True
            temp = line.split()
            temp_data = [temp[0], float(temp[1])]
        elif investments_account and "done investments" not in line:
            temp = line.split()
            temp_investments[temp[0]] = float(temp[1].strip())
        elif investments_account and "done investments" in line:
            investments_account = False
            accounts.append(InvestmentAccount(temp_data[0], temp_data[1], temp_investments))
        else:
            temp = line.split()
            accounts.append(BankAccount(temp[0], float(temp[1].strip())))

    print(len(accounts))
    print(sum(account.balance for account in accounts))
    for account in accounts:
        print(f"{account.name}   {account.balance}")
        if isinstance(account, InvestmentAccount):
            for key, val in account.investments.items():
                print(f"{key}  {val}")

            print("-----------")


func_g("bank.txt")
