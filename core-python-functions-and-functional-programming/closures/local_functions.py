"""
Local Functions
->  Defined when def is executed
-> New copy made for each enclosing invocation
-> Separate name binding each time

-> Defining on-off functions close to their use
-> Code organization and readability
-> Similar to lambdas
-> More general than lambdas
-> Local functions are no different from other objects defined in a function
-> New instances are created for each execution of the enclosing function
-> These instance can be returned from the enclosing function
"""


def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]

    print(last_letter)
    return sorted(strings, key=last_letter)


print(sort_by_last_letter(['hello', 'from', 'a', 'local', 'function']))

"""Scoping Rules
1. Local
2. Enclosing
3. Global
4. Built-in
"""

"""
Name resolution for local function
-> Starts with name in the local function
-> Then checks enclosing scope(s)
-> Finally module-level and built-in name are checked
"""

g = 'global'


def outer(p='param'):
    l = 'local'

    def inner():
        print(g, p, l)

    inner()


print(outer())

"""
Returning Local Functions
"""

"""
First-class functions
-> Functions can be passed to and returned from functions
-> More generally, they can be treated like any other data
-> A powerful concept that becomes even more powerful when combined with closures
"""


def enclosing():
    def local_func():
        print('local func')

    return local_func


lf = enclosing()
lf()
