# Define a decorator function decprotect.
def decprotect(f):
    # Define a wrapper function ret that will replace the original function f.
    def ret(*args):
        # Iterate through each argument passed to the function.
        for arg in args:
            # Iterate through the directory of attributes of the argument.
            for attr in dir(arg):
                # Check if the attribute is callable (a method) and not in the original directory of the class.
                if callable(getattr(arg, attr)) and attr not in arg.__originalDir__:
                    # Print a warning if a new method has been added that wasn't in the original class definition.
                    print("Warning: additional method: " + str(attr) + " in object " + str(arg))
        # Call the original function with its arguments.
        f(*args)

    # Return the wrapper function.
    return ret


# Define a metaclass ClsProtector, inheriting from the default metaclass 'type'.
class ClsProtector(type):
    # Override the __new__ method, which is called when creating a new class.
    def __new__(cls, name, bases, _dict):
        # Create a new class using the standard mechanism.
        newcls = type.__new__(cls, name, bases, _dict)
        # Store the original directory of the class for future comparison.
        newcls.__originalDir__ = dir(newcls)
        # Iterate through the dictionary of the new class.
        for attr, item in newcls.__dict__.items():
            # If the item is a callable (usually methods), wrap it with the decprotect decorator.
            if callable(item):
                setattr(newcls, attr, decprotect(item))
        # Return the newly created class.
        return newcls

        # Override the __call__ method, which is called when an instance of the class is created.

    def __call__(cls, *args, **kwargs):
        # Check for any new methods that weren't in the original class definition.
        currentDir = dir(cls)
        for attr in currentDir:
            if callable(getattr(cls, attr)) and attr not in cls.__originalDir__:
                # Raise an error or print a warning if a new method has been added.
                raise TypeError(f"New method {attr} added to class {cls.__name__} after its definition.")
        # Create an instance of the class if no new methods were added.
        return super(ClsProtector, cls).__call__(*args, **kwargs)


class Replicator:
    # deco is a decorator method. It takes a function 'f' as input.
    def deco(self, f):
        # It defines and returns a new function 'ret'.
        def ret(*args):
            print("=== Affected  ===")
            # For each argument in the function call,
            # it prints a message and applies the 'affect' method.
            # However, note that [len(args) - 1] is not iterating through all args,
            # but only takes the last element in args due to the list notation.
            for i in [len(args) - 1]:
                self.affect(args[i])
            # Then it calls the original function 'f' with its arguments.
            f(*args)

        # The new function 'ret' is returned.
        return ret

    # The affect method is used to modify an object.
    def affect(self, obj):
        # It adds the 'deco' method to the object.
        setattr(obj, "deco", self.deco)
        # It adds the 'affect' method to the object.
        setattr(obj, "affect", self.affect)
        # It gets the class of the object.
        cls = obj.__class__
        # For each attribute in the class's dictionary,
        # if the attribute is callable (i.e., it is a method),
        # it wraps the method with the 'deco' decorator.
        for attr, item in cls.__dict__.items():
            if callable(item):
                setattr(cls, attr, self.deco(item))


class Tester(metaclass=ClsProtector):
    def first(self, obj):
        print("Tester:first " + str(obj))

    def second(self, obj):
        print("Tester:second " + str(obj))


class Checker(metaclass=ClsProtector):
    def go(self, obj):
        print("Checker:go " + str(obj))

    def run(self, obj):
        print("Checker:run " + str(obj))


if __name__ == '__main__':
    r = Replicator()
    t = Tester()
    c1 = Checker()
    c2 = Checker()

    print("\n Before affect")
    t.first(c1)
    c1.go(c2)

    r.affect(t)

    print("\n After affect")
    t.first(c1)
    c1.go(c2)
