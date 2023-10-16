class SymbolTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i in range(len(self.table[index])):
            k = self.table[index][i]
            if k == key:
                return
        self.table[index].append(key)

    def lookup(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            if key in self.table[index]:
                return key
        return None

    # TODO position in chaining list
    def find_position(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            if key in self.table[index]:
                return index
        return None
