# Define the Employee class
class Employee:
    # Initialize an Employee object with first_name, last_name, level, and years_service
    def __init__(self, first_name, last_name, level, years_service):
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.seniority = years_service

    # Define greater than or equal to comparison based on level and seniority
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    # Define greater than comparison based on level and seniority
    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    # Define less than comparison based on level and seniority
    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    # Define less than or equal to comparison based on level and seniority
    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level


# Create a department list
dept = []

# Add Employee objects to the department list
dept.append(Employee("Jane", "Smith", 6, 6))
dept.append(Employee("Tyler", "Durden", 5, 11))
dept.append(Employee("Rebecca", "Robinson", 5, 12))
dept.append(Employee("John", "Doe", 4, 11))
dept.append(Employee("Or", "Hasson", 5, 9))

# Test the greater than and less than comparison methods
print(dept[0] > dept[2])
print(dept[4] < dept[3])

# Sort the Employee objects and print their last names
emps = sorted(dept)
for emp in emps:
    print(emp.last_name)
