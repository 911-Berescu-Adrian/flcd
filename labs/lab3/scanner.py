from lab2.symbol_table import SymbolTable
from lab3.scanner_exception import ScannerException
import re


class Scanner:
    def __init__(self, program, tokens):
        self.program = program
        self.tokens = tokens
        self.symbol_table = SymbolTable()
        self.pif = []
        self.index = 0
        self.line = 1

    def scan(self):
        while self.index < len(self.program):
            self.next_token()
        print("Lexically correct")

    def next_token(self):
        self.skip_space()
        if self.index == len(self.program):
            return
        if self.treat_int_constant():
            return
        if self.treat_token():
            return
        if self.treat_identifier():
            return
        if self.treat_string_constant():
            return

        raise ScannerException("Lexical error: unknown token", self.line)

    def skip_space(self):
        while self.index < len(self.program) and self.program[self.index].isspace():
            if self.program[self.index] == '\n':
                self.line += 1
            self.index += 1

    def treat_string_constant(self):
        regex_pattern = r'^"[a-zA-Z0-9 ?:*^+=.!]*"'
        match = re.search(regex_pattern, self.program[self.index:])

        if match:
            string_constant = match.group()
            self.index += len(match.group())
            self.symbol_table.insert_string_constant(string_constant)
            position = self.symbol_table.find_position_string_constant(string_constant)
            self.pif.append(("const", position))
            return True

        return False

    def treat_int_constant(self):
        regex_pattern = r'^([+-]?[1-9][0-9]*|0(?![0-9]))'
        while self.index < len(self.program):
            match = re.match(regex_pattern, self.program[self.index:])
            if match:
                int_constant = match.group()
                self.index += len(match.group())
                parsed_int_constant = int(int_constant)
                self.symbol_table.insert_int_constant(parsed_int_constant)
                parsed_int_constant = int(int_constant)
                position = self.symbol_table.find_position_int_constant(parsed_int_constant)
                self.pif.append(("const", position))

                while self.index < len(self.program) and self.program[self.index].isspace():
                    self.index += 1

                if self.index < len(self.program) and self.program[self.index] == '-':
                    self.pif.append(("-", -1))
                    self.index += 1
                    continue

                if self.index < len(self.program) and self.program[self.index] == '+':
                    self.pif.append(("+", -1))
                    self.index += 1
                    continue

                return True

            return False

    def treat_token(self):
        combined_tokens = ['<=', '>=', '!=', '==']
        for token in combined_tokens:
            if self.program[self.index:].startswith(token):
                self.pif.append((token, -1))
                self.index += len(token)
                return True

        for token in self.tokens:
            if self.program[self.index:].startswith(token):
                self.pif.append((token, -1))
                self.index += len(token)
                return True

        return False

    def treat_identifier(self):
        regex_pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9]*')
        match = regex_pattern.search(self.program[self.index:])

        if match:
            identifier = match.group()
            self.index += len(identifier)

            if identifier not in self.tokens:
                self.symbol_table.insert_identifier(identifier)

            position = self.symbol_table.find_position_identifier(identifier)
            self.pif.append(("id", position))
            return True

        return False

