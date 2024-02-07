# Define a class called Person
class Person:
    # Initialize attributes for Person objects
    def __init__(self):
        self.first_name = "John"
        self.last_name = "Doe"
        self.age = 25

    # Define the __repr__ method for a formal string representation of the object
    def __repr__(self):
        return "<Person Class - first_name:{0}, last_name:{1}, age:{2}>".format(
            self.first_name, self.last_name, self.age)

    # Define the __str__ method for an informal string representation of the object
    def __str__(self):
        return "Person ({0} {1} is {2} years old.)".format(
            self.first_name, self.last_name, self.age)

    # Define the __bytes__ method for byte-string representation of the object
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.first_name, self.last_name, self.age)
        return bytes(val.encode('utf-8'))  # Encoding the string to bytes


# Create an object of the Person class
cls1 = Person()

# Print the formal representation of the object
print(repr(cls1))

# Print the informal representation of the object
print(str(cls1))

# Print the byte-string representation of the object
print(bytes(cls1))

# Print the object using Python's built-in formatting (which will call __str__)
print("Formatted: {0}".format(cls1))
