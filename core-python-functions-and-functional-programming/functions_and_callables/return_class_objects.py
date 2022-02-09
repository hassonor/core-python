"""
Conditional expression Evaluated to one of two expressions depending on a boolean.
e.g: result = true_value if condition else false_value
"""


def sequence_class(immutable):
    return tuple if immutable else list


seq = sequence_class(immutable=True)

t = seq("OrHasson")
print(t)
print(type(t))
