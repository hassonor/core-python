class Replicator:
    def deco(self, f):
        def ret(*args):
            print("=== Affected ===")
            for i in [len(args) - 1]:
                self.affect(args[i])
            f(*args)

        return ret

    def affect(self, obj):
        setattr(obj, "deco", self.deco)
        setattr(obj, "affect", self.affect)
        cls = obj.__class__
        for attr, item in cls.__dict__.items():
            if callable(item):
                setattr(cls, attr, self.deco(item))


class Tester:
    def first(self, obj):
        print("Tester:first " + str(obj))

    def second(self, obj):
        print("Tester:second " + str(obj))


class Checker:
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
