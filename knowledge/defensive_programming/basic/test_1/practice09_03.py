my_list = ["everybody", "in", "this", "group", "should", "be", "able", "to", "dance", "salsa"
    , "but", "only", "some", "can", "dance", "bachata"]

my_length = {word: len(word) for word in my_list}
print(my_length)

phrase = ""
for ind, word in enumerate(my_list):
    if ind == 0 or word[-1] == 'a':
        phrase += word[0].upper() + word[1:]
    else:
        phrase += word

print(phrase)

names = ("Tom", "Daniel", "Ofir", "Ofri", "Andrea", "Silvia", "Manuel", "Jessica")

couples = zip(*[iter(names)] * 2)

text = "\n".join(f"{couple[0]}-{couple[1]}" for couple in couples)

try:
    with open("test93_1.txt", "w") as f:
        f.write(text)
except:
    print("Error...")

# Second Way
try:
    with open("test93_2.txt", "w") as f:
        for i in range(0, len(names) - 1, 2):
            f.write(f"({names[i]},{names[i + 1]})\n")

except:
    print("Error...")


def func_a(my_str):
    for word in my_str.split():
        if word and word.endswith("ando"):
            print(word.lower())


func_a("Hello FwAando and Kand Orange and andor and ando")


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
    lines = list()
    openu = False
    temp_data = list()
    temp_subjects = dict()
    universities = list()

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except:
        print("Error...")
        exit(1)

    for line in lines:
        if not openu and "courses:" in line:
            openu = True
            temp = line.split(",")
            temp_data = [temp[0], temp[1], int(temp[2].split()[0])]
        elif openu and "done courses" not in line:
            temp = line.split(",")
            temp_subjects[temp[0]] = int(temp[1].strip())
        elif openu and "done courses" in line:
            openu = False
            universities.append(OpenUniversity(temp_data[0], temp_data[1], temp_data[2], temp_subjects))
        else:
            temp = line.split(",")
            universities.append(University(temp[0], temp[1], int(temp[2].strip())))

    print(len(universities))
    print(sum(u.students for u in universities))

    major = ""
    max_val = 0
    for un in universities:
        if isinstance(un, OpenUniversity):
            for key, val in un.subjects.items():
                if val > max_val:
                    max_val = val
                    major = key
            print(f"{major}:{max_val}")
            major = ""
            max_val = 0


func_b("universities.txt")


def func_c(my_str):
    for word in my_str.split():
        if word and word.endswith("ing"):
            print(word[0].upper() + word[1:])


func_c("lkdfjing \n df;askldsflkj algfdsjJing fsdl;kjfsdw;lkING   ;fdlk;\n\n flds")


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


def func_d(filename):
    lines = list()
    temp_data = list()
    temp_investments = dict()
    investment_account = False
    accounts = list()

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

    except:
        print("Error....")
        exit(1)

    for line in lines:
        if not investment_account and "investments:" in line:
            investment_account = True
            temp = line.split()
            temp_data = [temp[0], float(temp[1])]
        elif investment_account and "done investments" not in line:
            temp = line.split()
            temp_investments[temp[0]] = float(temp[1].strip())
        elif investment_account and "done investments" in line:
            investment_account = False
            accounts.append(InvestmentAccount(temp_data[0], temp_data[1], temp_investments))
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


func_d("bank.txt")


def func_e():
    words = list()
    for _ in range(5):
        line = input(f"Insert a line {_}:")
        for word in line.split():
            if word and "WarWorld2" in word.lower():
                words.append(word)

    print(words)


# func_e()


def func_f(filename):
    found = False
    keywords = ["Weapon", "Delivery"]
    words = list()

    try:
        with open(filename, "r") as f:
            for line in f:
                if "WarWorld2" in line:
                    found = True
                if found:
                    for keyword in keywords:
                        if keyword in line:
                            words.append(keyword)
                            found = False
    except:
        print("Error...")
        exit(1)

    return words


print(func_f("report.txt"))


class Base:
    def __init__(self, name, mk, cor_x, cor_y):
        if type(name) is str:
            self.name = name
        if type(mk) is str:
            self.mk = mk
        if type(cor_x) is float:
            self.cor_x = cor_x
        if type(cor_y) is float:
            self.cor_y = cor_y


class AttentionBase(Base):
    def __init__(self, name, mk, cor_x, cor_y, suspects):
        super().__init__(name, mk, cor_x, cor_y)
        self.suspects = func_f("reports.txt")
