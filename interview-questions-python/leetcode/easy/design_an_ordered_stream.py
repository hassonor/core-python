class OrderedStream(object):
    def __init__(self, n):
        self.values = [None] * n
        self.ptr = 0

    def insert(self, idKey, value):
        self.values[idKey - 1] = value

        if idKey - 1 != self.ptr:
            return []

        chunk = []
        while self.ptr < len(self.values) and self.values[self.ptr] is not None:
            chunk.append(self.values[self.ptr])
            self.ptr += 1

        return chunk
