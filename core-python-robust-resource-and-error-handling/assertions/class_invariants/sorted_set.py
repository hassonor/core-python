from bisect import bisect_left


class SortedSet:
    def __init__(self, xs):
        self._set = []
        for x in xs:
            self.add(x)

    def add(self, x):
        self._set.append(x)
        self._set = sorted(set(self._set))
        assert self._is_unique_and_sorted()

    def contains(self, x):
        assert self._is_unique_and_sorted()
        index = bisect_left(self._set, x)
        return index != len(self._set) and self._set[index] == x

    def _is_unique_and_sorted(self):
        return all(self._set[i] < self._set[i + 1] for i in range(len(self._set) - 1))

    @property
    def set(self):
        return self._set


s = SortedSet([4, 3, 2, 1, 4, 3, 2, 1])
print(s.set)
s.add(11)
s.add(-14)
print(s.set)
