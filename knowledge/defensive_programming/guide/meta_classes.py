def decprotect(f):
    def ret(*args):
        for arg in args:
            for attr in dir(arg):
                if callable(getattr(arg, attr)) and attr not in arg.__originalDir__:
                    print("Warning: additional method: " + str(attr) + " in object " + str(arg))
        f(*args)

    return ret


class ClsProtector(type):
    def __new__(cls, name, bases, _dict):
        newcls = type.__new__(cls, name, bases, _dict)
        newcls.__originalDir__ = dir(newcls)
        for attr, item in newcls.__dict__.items():
            if callable(item):
                setattr(newcls, attr, decprotect(item))
        return newcls


class SampleMetaClass(type):
    def __new__(cls, name, bases, _dict):
        newcls = type.__new__(cls, name, bases, _dict)
        newcls.value = 110
        newcls.title = "This is an example"
        return newcls


if __name__ == '__main__':
    # cls = type('ExampleClass', (), {'value': 110, 'title': 'This is an example'})
    cls = SampleMetaClass('ExampleClass', (), {'value': 110, 'title': 'This is an example'})
    print(cls.value)
    print(dir(cls))
    print(cls)
