"""
-> In many cases anonymous callable objects will suffice.
-> lambda allows you to create such anonymous callable objects.
-> Use lambda with care to avoid creating inscrutable code.
"""

list_of_scientists = ['Marie Curie', 'Albert Einstein', 'Rosalind Franklin', 'Niels Bohr', 'Dian Fossey',
                      'Isaac Newton', 'Grace Hopper', 'Charles Darwin', 'Lise Meitner']

print(sorted(list_of_scientists, key=lambda name: name.split()[-1]))

last_name = lambda name: name.split()[-1]
print(last_name("Or Hasson"))


def first_name(name):
    return name.split()[0]


def is_even(x):
    return x % 2 == 0


print(callable(is_even))

is_odd = lambda x: x % 2 == 1
print(callable(is_odd))
