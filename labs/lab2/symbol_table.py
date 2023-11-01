class SymbolTable:
    def __init__(self, size=100):
        self.size = size
        self.string_constant_table = [None] * size
        self.int_constant_table = [None] * size
        self.identifier_table = [None] * size

    def hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert_identifier(self, key):
        index = self.hash(key)
        if self.identifier_table[index] is None:
            self.identifier_table[index] = []
        for i in range(len(self.identifier_table[index])):
            k = self.identifier_table[index][i]
            if k == key:
                return
        self.identifier_table[index].append(key)

    def insert_int_constant(self, key):
        index = self.hash(str(key))
        if self.int_constant_table[index] is None:
            self.int_constant_table[index] = []
        for i in range(len(self.int_constant_table[index])):
            k = self.int_constant_table[index][i]
            if k == key:
                return
        self.int_constant_table[index].append(key)

    def insert_string_constant(self, key):
        index = self.hash(key)
        if self.string_constant_table[index] is None:
            self.string_constant_table[index] = []
        for i in range(len(self.string_constant_table[index])):
            k = self.string_constant_table[index][i]
            if k == key:
                return
        self.string_constant_table[index].append(key)

    def lookup_identifier(self, key):
        index = self.hash(key)
        if self.identifier_table[index] is not None:
            if key in self.identifier_table[index]:
                return key
        return None

    def lookup_int_constant(self, key):
        index = self.hash(str(key))
        if self.int_constant_table[index] is not None:
            if key in self.int_constant_table[index]:
                return key
        return None

    def lookup_string_constant(self, key):
        index = self.hash(key)
        if self.string_constant_table[index] is not None:
            if key in self.string_constant_table[index]:
                return key
        return None

    def find_position_identifier(self, key):
        index = self.hash(key)
        if self.identifier_table[index] is not None:
            if key in self.identifier_table[index]:
                position = self.identifier_table[index].index(key)
                return [index, position]
        return None

    def find_position_int_constant(self, key):
        index = self.hash(str(key))
        if self.int_constant_table[index] is not None:
            if key in self.int_constant_table[index]:
                position = self.int_constant_table[index].index(key)
                return [index, position]
        return None

    def find_position_string_constant(self, key):
        index = self.hash(key)
        if self.string_constant_table[index] is not None:
            if key in self.string_constant_table[index]:
                position = self.string_constant_table[index].index(key)
                return [index, position]
        return None

    def __str__(self):
        result = ""
        for index in self.identifier_table:
            if index is not None:
                for key in index:
                    result += str(key) + " -> " + self.find_position_identifier(key).__str__() + '\n'
        for index in self.string_constant_table:
            if index is not None:
                for key in index:
                    result += str(key) + " -> " + self.find_position_string_constant(key).__str__() + '\n'
        for index in self.int_constant_table:
            if index is not None:
                for key in index:
                    result += str(key) + " -> " + self.find_position_int_constant(key).__str__() + '\n'
        return result
