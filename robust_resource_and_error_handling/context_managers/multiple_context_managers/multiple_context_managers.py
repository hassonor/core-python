import contextlib


@contextlib.contextmanager
def nest_test(name):
    print('Entering', name)
    yield name
    print('Exiting', name)


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception!')
        if propagate:
            raise


with nest_test('outer'), nest_test('inner'):
    print('BODY')

# The Same...
with nest_test('outer'):
    with nest_test('inner'):
        print('BODY')

with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
    print('BODY')

print("")
print("")

with propagater('outer', True), propagater('inner', False):
    raise TypeError()

print("")

with propagater('outer', False), propagater('inner', True):
    raise TypeError()
