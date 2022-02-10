"""
Closure
-> Records objects from enclosing scopes
-> Keeps recorded objects alive for use after the enclosing scope is gone
-> Implemented with the __closure__ attribute
"""
"""
Functions Factories
-> Functions that return other functions
-> Returned functions use both heir own arguments as well as arguments to the factory
-> Combination of runtime function definition and closures
"""


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)

    return raise_to_exp


square = raise_to(2)
print(square.__closure__)

print(square(5))
