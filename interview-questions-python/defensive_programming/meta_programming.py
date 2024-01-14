"""
Method Decoration
הרעיון הוא לעטוף בקוד מסוים בלי לפגוע בקוד המקורי. כלומר להפעיל קוד נוסף לקוד המקורי.
"""


def decotitle(f):
    def ret(*args):
        print("Now this function is executed " + str(f))

        f(*args)

    return ret


def square(num):
    print(num * num)


square = decotitle(square)

square(10)


# Classes
class Person:
    i = 22222
    j = 11111

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.i = 1241234241124124412


p1 = Person("John", 30)
print(p1.name)
print(p1.age)
print(p1.i)  # will print  1241234241124124412 -> instance var
print(p1.j)  # will print 11111 -> class var (instance var of j not exist so print the class var)
print(Person.i)  # will print 22222 -> class var
print(Person.j)  # will print 11111 -> class var
"""
משתני מחלקה ומשתני מופע
________________________
ניתן להגדיר במחלקה משתנים כלליים שאינם חלק ממופע (instance) מסויים, הם בדרך כלל יוגדרו מחוץ לשיטה:
Class Point:
    printed_rep = "*"
    
    def __init__(self,initX, initY):
    
    בקריאה למשתנה בתוך מחלקה
    <obj>.<varname>
    המפרש יחפש ראשית משתנה מופע בשם זה, ואם לא הוא יחפש משתנה מחלקה, אם גם לא קיים -- תתקבל שגיאה
    
    בהשמה לתוך משתנה, הוא יגדיר משתנה חדש עבור המופע.
"""


class Point:
    def __init__(self, x_color, y_color):
        self.x = x_color
        self.y = y_color

    def move(self, add_x, add_y):
        self.x += add_x
        self.y += add_y

    def __str__(self):
        return f"({self.x},{self.y})"


p1 = Point(3, 4)
p1.move(10, 21)
print(p1)

"""
ייצוג מחלקה בתור מילון
* לכל מחלקה בפייתון יש בעצם מילון, המגדיר את המשתנים הפנימיים ואת השיטות על המחלקה. יש להבחין בין המילון 
של טיפוס המחלקה (שניתן לגשל אליו בתור Point.__dict__) לבין המילון של המופע של המחלקה,
p1.__dict__
* משמעות: בניגוד ל C++, לא ניתן לבצע העמסה (overloading) של יותר מפונקציה וירטואלית אחת באותו שם עם ארגומנטים שונים. בחלק מהמקרים, ניתן לעקוף זאת בעזרת ערכי ברירת מחדל
"""

print(Point.__dict__)
print(p1.__dict__)
