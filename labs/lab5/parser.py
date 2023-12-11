class LL1Parser:
    def __init__(self, grammar):
        self.follow_sets = {}
        self.grammar = grammar
        self.parse_table = {}
        self.build_parse_table()

    def build_parse_table(self):
        terminals =  self.grammar.terminals.union({'$'})
        for nonterminal in self.grammar.nonterminals.union(terminals):
            for terminal in terminals:
                self.parse_table[(nonterminal, terminal)] = self.find_production(nonterminal, terminal)

    def find_production(self, nonterminal, terminal):
        if nonterminal in self.grammar.terminals.union('$'):
            if nonterminal == terminal:
                if terminal == '$': return "except"
                return "pop"
        else:
            if nonterminal == "S":
                pass# print(self.grammar.productions[nonterminal])
            # for production in self.grammar.productions[nonterminal]:
            #     if terminal in self.first(production):
            #         return production
            return None

    def first(self, symbol):
        result = set()

        if symbol in self.grammar.terminals:
            result.add(symbol)
        elif symbol in self.grammar.nonterminals:
            for nont, term in self.grammar.productions:
                if nont == symbol:
                    result.update(self.first(term.split(" ")[0]))
        return result

    def follow(self, nonterminal):
        if nonterminal in self.follow_sets:
            return self.follow_sets[nonterminal]

        result = set()

        if nonterminal == next(iter(self.grammar.nonterminals), None):
            result.add('$')


        for nt, productions in self.grammar.productions:
            for production in productions:
                symbols = production.split(" ")
                if nonterminal in symbols:
                    index = symbols.index(nonterminal)
                    if index < len(symbols) - 1:
                        result.update(self.first(' '.join(symbols[index + 1:])))
                        if 'epsilon' in self.first(' '.join(symbols[index + 1:])):
                            result.update(self.follow(nt))
                    elif index == len(symbols) - 1:
                        result.update(self.follow(nt))

        self.follow_sets[nonterminal] = result
        return result