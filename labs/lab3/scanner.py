from lab2.symbol_table import SymbolTable
from lab3.scanner_exception import ScannerException


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

        def next_token(self):
            self.skip_whitespace()
            self.skip_comment()
            if self.index == len(self.program):
                return
            if self.treat_string_constant():
                return
            if self.treat_int_constant():
                return
            if self.treat_from_token_list():
                return
            if self.treat_identifier():
                return
            raise ScannerException("Lexical error: unknown token", self.current_line)

        def skip_whitespace(self):
            while self.index < len(self.program) and self.program[self.index].isspace():
                if self.program[self.index] == '\n':
                    self.current_line += 1
                self.index += 1

        def skip_comment(self):
            if self.program.startswith("//", self.index):
                while self.index < len(self.program) and self.program[self.index] != '\n':
                    self.index += 1
                return

        def treat_string_constant(self):
            return True

        def treat_int_constant(self):
            return True

        def treat_from_token_list(self):
            return True

        def treat_identifier(self):
            return True








