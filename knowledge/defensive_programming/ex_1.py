import re

factor = 1 + 17 / 100

basic = input("Please enter the original price: ")
while basic != "quit":
    if re.search("^-?[0-9]*(\.[0-9]+)?$", basic):
        sum = float(basic) * factor
        print("Sum with VAT is ", sum)
    else:
        print("Non-numeric value, please try again")
    basic = input("Please enter the original price: ")


# Class example
class NumberBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def set(self, x, y, value):
        if 0 <= x < self.size and 0 <= y < self.size and 0 <= value <= 9:
            self.board[y][x] = value
        else:
            print("Invalid input. Please ensure x, y are within range [0, {}] and value is between 0 and 9.".format(
                self.size - 1))

    def print(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    print("NONE", end="\t")
                else:
                    print(cell, end="\t")
            print("\n")

    def magic(self):
        # בדיקת סכומי השורות והעמודות
        row_sums = [sum(row) for row in self.board]
        col_sums = [sum(row[i] for row in self.board) for i in range(self.size)]

        # בדיקת סכום האלכסונים
        diagonal1_sum = sum(self.board[i][i] for i in range(self.size))
        diagonal2_sum = sum(self.board[i][self.size - 1 - i] for i in range(self.size))

        # הכנסת כל הסכומים לרשימה אחת לבדיקת אם הם זהים
        all_sums = row_sums + col_sums + [diagonal1_sum, diagonal2_sum]

        # בדיקה אם כל הסכומים זהים (ריבוע קסם)
        return all(s == all_sums[0] for s in all_sums)


# יצירת מופע של המחלקה עם לוח בגודל 4x4
board = NumberBoard(9)

# הצבת מספרים בלוח
board.set(0, 0, 1)
board.set(1, 1, 5)
board.set(2, 2, 9)
board.set(3, 3, 3)

# הדפסת הלוח
board.print()
