### Table 1-1. Special method names (operators excluded)

| Category                          | Method Names                                                               |
|-----------------------------------|----------------------------------------------------------------------------|
| String/bytes representation       | `__repr__`, `__str__`, `__format__`, `__bytes__`, `__fspath__`             |
| Conversion to number              | `__bool__`, `__complex__`, `__int__`, `__float__`, `__hash__`, `__index__` |
| Emulating collections             | `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`     |
| Iteration                         | `__iter__`, `__aiter__`, `__next__`, `__anext__`, `__reversed__`           |
| Callable or coroutine execution   | `__call__`, `__await__`                                                    |
| Context management                | `__enter__`, `__exit__`, `__aexit__`, `__aenter__`                         |
| Instance creation and destruction | `__new__`, `__init__`, `__del__`                                           |
| Attribute management              | `__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`, `__dir__` |
| Attribute descriptors             | `__get__`, `__set__`, `__delete__`, `__set_name__`                         |
| Abstract base classes             | `__instancecheck__`, `__subclasscheck__`                                   |
| Class metaprogramming             | `__prepare__`, `__init_subclass__`, `__class_getitem__`, `__mro_entries__` |

### Table 1-2. Special method names and symbols for operators

| Operator category               | Symbols                                          | Method Names                                                                                                              |
|---------------------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Unary numeric                   | `-`, `+`, `abs()`                                | `__neg__`, `__pos__`, `__abs__`                                                                                           |
| Rich comparison                 | `<`, `<=`, `==`, `!=`, `>`, `>=`                 | `__lt__`, `__le__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`                                                                |
| Arithmetic                      | `+`, `-`, `*`, `/`, `//`, `%`, `@`               | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__matmul__`, `__pow__`                        |
|                                 | `divmod()`, `round()`, `**`, `pow()`             | `__divmod__`, `__round__`, `__pow__`                                                                                      |
| Reversed arithmetic             | arithmetic operators with swapped operands       | `__radd__`, `__rsub__`, `__rmul__`, `__rtruediv__`, `__rfloordiv__`, `__rmod__`, `__rmatmul__`, `__rdivmod__`, `__rpow__` |
| Augmented assignment arithmetic | `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `@=`, `**=` | `__iadd__`, `__isub__`, `__imul__`, `__itruediv__`, `__ifloordiv__`, `__imod__`, `__imatmul__`, `__ipow__`                |
| Bitwise                         | `&`, `\|`, `^`, `<<`, `>>`, `~`                  | `__and__`, `__or__`, `__xor__`, `__lshift__`, `__rshift__`, `__invert__`                                                  |
| Reversed bitwise                | bitwise operators with swapped operands          | `__rand__`, `__ror__`, `__rxor__`, `__rlshift__`, `__rrshift__`                                                           |
| Augmented assignment bitwise    | `&=`, `\|=`, `^=`, `<<=`, `>>=`                  | `__iand__`, `__ior__`, `__ixor__`, `__ilshift__`, `__irshift__`                                                           |