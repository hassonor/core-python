import functools
import inspect


def auto_repr(cls):
    members = vars(cls)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")

    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]

    if not all(
            isinstance(members.get(name, None), property)
            for name in parameter_names
    ):
        raise TypeError(
            f"Cannot apply auto_repr {cls.__name__} because not all "
            "__init__ parameters have matching properties"
        )

    def synthesized_repr(self):
        return "{typename}({args})".format(
            typename=typename(self),
            args=", ".join(
                "{name}={value!r}".format(
                    name=name,
                    value=getattr(self, name)
                ) for name in parameter_names
            )
        )

    setattr(cls, "__repr__", synthesized_repr)

    return cls


def postcondtion(predicate):
    def function_decorator(f):
        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            result = f(self, *args, **kwargs)
            if not predicate(self):
                raise RuntimeError(
                    f"Post-condition {predicate.__name__} not "
                    f"maintained for {self!r}"
                )
            return result

        return wrapper

    return function_decorator


def invariant(predicate):
    function_decorator = postcondtion(predicate)

    def class_decorator(cls):
        members = list(vars(cls).items())
        for name, member in members:
            if inspect.isfunction(member):
                decorated_member = function_decorator(member)
                setattr(cls, name, decorated_member)
        return cls

    return class_decorator


def at_least_two_locations(itinerary):
    return len(itinerary._locations) >= 2


def no_duplicates(itinerary):
    already_seen = set()
    for location in itinerary._locations:
        if location in already_seen:
            return False
        already_seen.add(location)
    return True


@auto_repr
@invariant(no_duplicates)
@invariant(at_least_two_locations)
class Itinerary:
    @classmethod
    def from_location(cls, *locations):
        return cls(locations)

    @postcondtion(at_least_two_locations)
    def __init__(self, locations):
        self._locations = list(locations)

    def __str__(self):
        return "\n".join(location.name for location in self._locations)

    @property
    def locations(self):
        return tuple(self._locations)

    @property
    def origin(self):
        return self._locations[0]

    @property
    def destination(self):
        return self._locations[-1]

    def add(self, location):
        self._locations.append(location)

    def remove(self, name):
        removal_indexes = [
            index for index, location in enumerate(self._locations)
            if location.name == name
        ]
        for index in reversed(removal_indexes):
            del self._locations[index]

    def truncate_at(self, name):
        stop = None
        for index, location in enumerate(self._locations):
            if location.name == name:
                stop = index + 1

        self._locations = self._locations[:stop]


def typename(obj):
    return type(obj).__name__
