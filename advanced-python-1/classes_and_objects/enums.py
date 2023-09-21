# Import Enum, unique, and auto from the enum module
from enum import Enum, unique, auto


# Define an Enum class named Fruit, ensuring all enum names are unique with the @unique decorator
@unique
class Fruit(Enum):
    APPLE = 1  # Define APPLE with an explicit value of 1
    BANANA = 2  # Define BANANA with an explicit value of 2
    ORANGE = 3  # Define ORANGE with an explicit value of 3
    TOMATO = 4  # Define TOMATO with an explicit value of 4
    PEAR = auto()  # Define PEAR with an automatically assigned value


# Print the APPLE enum
print(Fruit.APPLE)
# Print the type of the APPLE enum
print(type(Fruit.APPLE))
# Print the representation of the APPLE enum
print(repr(Fruit.APPLE))

# Print the name and value of the APPLE enum
print(Fruit.APPLE.name, Fruit.APPLE.value)
# Print the automatically assigned value of the PEAR enum
print(Fruit.PEAR.value)

# Create a dictionary with a Fruit enum (BANANA) as the key and a string as the value
my_fruits = {Fruit.BANANA: "Or Hasson was here :)"}
# Print the value associated with the BANANA key
print(my_fruits[Fruit.BANANA])
