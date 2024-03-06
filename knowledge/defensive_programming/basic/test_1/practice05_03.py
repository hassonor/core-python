mylist = ["everybody", "in", "this", "group", "should", "be", "able", "to", "dance", "salsa", "but", "only", "some",
          "can", "dance", "bachata"]

my_length = {word: len(word) for word in mylist}

print(my_length)

phrase = ""

for ind, word in enumerate(mylist):
    if ind == 0 or word[-1] == 'a':
        phrase += word[0].capitalize() + word[1:]
    else:
        phrase += word

print(phrase)

names = ("Tom", "Daniel", "Ofra", "Ofri", "Andrea", "Silvia", "Manuel", "Jessica")

couples = zip(*[iter(names)] * 2)

text = "\n".join(f"{couple[0]}-{couple[1]}" for couple in couples)

try:
    with open("test4.txt", "w") as f:
        f.write(text)
except:
    print("Error...")

try:
    with open("Test5.txt", "w") as f:
        for i in range(0, len(names) - 1, 2):
            f.write(f"({names[i]},{names[i + 1]})\n")

except:
    print("Error...")


def func_a(my_str):
    for word in my_str.split():
        if word.endswith("ando"):
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
    is_openu = False
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
        if is_openu and "done courses" not in line:
            temp = line.split(",")
            temp_subjects[temp[0]] = int(temp[1].strip())
        elif is_openu and "done courses" in line:
            is_openu = False
            universities.append(OpenUniversity(temp_data[0], temp_data[1], temp_data[2], temp_subjects))
        elif not is_openu and "courses:" in line:
            is_openu = True
            temp = line.split(",")
            temp_data = [temp[0], temp[1], int(temp[2].split()[0])]
        else:
            temp = line.split(",")
            universities.append(University(temp[0], temp[1], int(temp[2].strip())))

    print(len(universities))
    print(sum(u.students for u in universities))

    major_name = ""
    major_count = 0
    for un in universities:
        if isinstance(un, OpenUniversity):
            for key, val in un.subjects.items():
                if val > major_count:
                    major_count = val
                    major_name = key
            print(f"{major_name}:{major_count}")
            major_count = 0
            major_name = ""


func_a("some word here fando and Fando and ando and PanaNando")
func_b("universities.txt")


def func_c(my_str):
    for word in my_str.split():
        if word and word.endswith("ing"):
            print(word[0].capitalize() + word[1:])


func_c("lkdfjing \n df;askldsflkj algfdsjJing fsdl;kjfsdw;lkING   ;fdlk;\n\n flDsing")


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
    all_lines = list()
    investment_mode = False
    temp_investments_data = dict()
    temp_data = list()
    accounts = list()

    try:
        with open(filename, "r") as f:
            all_lines = f.readlines()
    except:
        print("Cannot open the file...")
        exit(1)

    for line in all_lines:
        if not investment_mode and "investments:" in line:
            temp = line.split()
            temp_data = [temp[0], float(temp[1])]
            investment_mode = True
        elif investment_mode and "done investments" not in line:
            temp = line.split()
            temp_investments_data[temp[0]] = float(temp[1].strip())
        elif investment_mode and "done investments" in line:
            accounts.append(InvestmentAccount(temp_data[0], temp_data[1], temp_investments_data))
            investment_mode = False
        else:
            temp = line.split()
            accounts.append(BankAccount(temp[0], float(temp[1].strip())))

    print(len(accounts))
    for account in accounts:
        print(account.name)
        print(account.balance)
        if isinstance(account, InvestmentAccount):
            print("")
            for key, val in account.investments.items():
                print(f"{key}:{val}")


func_d("bank.txt")


def func_d():
    index = 0
    all_text = ""
    while index < 4:
        line = input("Insert a line: ")
        all_text += line + " "
        index += 1

    words = list()
    for word in all_text.split():
        if word and word.lower() == 'war':
            words.append(word)

    print(words)


def find_keyword_after_war(file_path):
    keywords = ["Weapon", "Delivery"]
    found_war = False
    found_keyword = list()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if 'War' in line:
                    found_war = True
                if found_war:
                    for keyword in keywords:
                        if keyword in line:
                            found_keyword.append(keyword)
    except FileNotFoundError:
        print("File not found.")

    return found_keyword


class Base:
    def __init__(self, name, number_mk, cor_x, cor_y):
        if type(name) is str:
            self.name = name
        if type(number_mk) is str:
            self.number_mk = number_mk
        if type(cor_x) is float:
            self.cor_x = cor_x
        if type(cor_y) is float:
            self.cor_y = cor_y


class AttentionBase(Base):
    def __init__(self, name, number_mk, cor_x, cor_y, suspects=None):
        super().__init__(name, number_mk, cor_x, cor_y)
        self.suspects = find_keyword_after_war("report.txt")


test = AttentionBase("test", "1234124", 23.3, 45.4)
print(test.suspects)
