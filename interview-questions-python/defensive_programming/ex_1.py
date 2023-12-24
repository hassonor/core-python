import re

factor = 1 + 17 / 100

basic = input("Please enter the original price: ")
while basic != "quit":
    if re.search("^-?[0-9]+.?[0-9]+?$", basic):
        sum = float(basic) * factor
        print("Sum with VAT is ", sum)
    else:
        print("Non-numeric value, please try again")
    basic = input("Please enter the original price: ")
