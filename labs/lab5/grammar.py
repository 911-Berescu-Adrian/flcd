class Grammar:
    def __init__(self):
        self.nonterminals = []
        self.terminals = set()
        self.productions = []
        self.is_production = False
        self.start_symbol = '0'

    def read_grammar(self, filename):
        with open(filename, "r") as file:
            for line in file:
                self.parse_grammar_line(line.strip())

    def parse_grammar_line(self, line):
        if not line:
            return
        if line.startswith('Start: '):
            self.start_symbol = line[7:]
        if line.startswith('Non-terminals:'):
            self.nonterminals = line[15:].split()
        elif line.startswith('Terminals:'):
            self.terminals.update(line[11:].split())
        elif line.startswith('Production:'):
            self.is_production = True
        elif self.is_production:
            parts = line.split(' ::= ')
            if len(parts) == 2:
                nonterminal, production = parts
                symbols = production.split(' | ')
                for symbol in symbols:
                    self.productions.append((nonterminal, symbol))

    def print_nonterminals(self):
        print("Nonterminals:", self.nonterminals)

    def print_productions_for_nonterminal(self, nonterminal):
        print("Productions for " + nonterminal)
        for nont, symb in self.productions:
            if nont == nonterminal:
                print(nont + " ::= " + symb)

    def print_terminals(self):
        print("Terminals:", self.terminals)

    def print_productions(self):
        print("Productions:")
        for nonterminal, symbol in self.productions:
            print(f"{nonterminal} ::= {symbol}")


    def is_cfg(self):
        for nonterminal, symbol in self.productions:
            if nonterminal not in self.nonterminals:
                return False
            for char in symbol:
                if char in self.terminals:
                    continue
        return True
