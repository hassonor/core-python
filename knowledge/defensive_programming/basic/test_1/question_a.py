my_str = "the quick brown fox jumps\n   oandover the \nFando and this\n is the smart brown fox jumps over the"


def func1(theString):
    for word in theString.split():
        if word and word[-4:] == "ando":
            print(word.casefold())


def func2(theString):
    for word in theString.split():
        if word.endswith("ando"):
            print(word.lower())


func1(my_str)
func2(my_str)
