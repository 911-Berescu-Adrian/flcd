class LL1Parser:
    def __init__(self, grammar):
        self.follow_sets = {}
        self.grammar = grammar
        self.parse_table = {}
        for nont in self.grammar.nonterminals:
            self.follow_sets[nont] = set()
        self.build_parse_table()

    def build_parse_table(self):
        for t in self.grammar.nonterminals:
            self.follow(t)
        terminals =  self.grammar.terminals.union({'$'})
        nonterminals_and_terminals = self.grammar.nonterminals.copy()
        nonterminals_and_terminals.extend(terminals)
        for nonterminal in nonterminals_and_terminals:
            for terminal in terminals:
                self.parse_table[(nonterminal, terminal)] = self.find_production(nonterminal, terminal)

    def find_production(self, nonterminal, terminal):
        if nonterminal in self.grammar.terminals.union('$'):
            if nonterminal == terminal:
                if terminal == '$':
                    return "except"
                return "pop"
        elif nonterminal in self.grammar.nonterminals:
            result = self.first(nonterminal, " ")
            for terms in result:
                if terminal == terms or terms == 'epsilon':
                    if terms != 'epsilon':
                        rule, number = self.find_rule_for_firsts(nonterminal, terms)
                        return rule, number
                    else:
                        result = self.follow_sets[nonterminal]
                        for _terms in result:
                            if _terms == terminal:
                                rule, number = self.find_rule_for_follows(nonterminal, _terms)
                                return rule, number
        return None

    def find_rule_for_firsts(self, nonterminal, terminal):
        for i, (nont, term) in enumerate(self.grammar.productions):
            if nont == nonterminal:
                if terminal in self.first(term.split(" ")[0], term):
                    return term, i + 1
        return None, None


    def find_rule_for_follows(self, nonterminal, terminal):
        for i, (nont, term) in enumerate(self.grammar.productions):
            if nont == nonterminal and term == 'epsilon':
                return term, i+1
        return None, None


    def first(self, symbol, from_term):
        result = set()

        if symbol in self.grammar.terminals or symbol == "epsilon":
            result.add(symbol)
        elif symbol in self.grammar.nonterminals:
            for nont, term in self.grammar.productions:
                if nont == symbol:
                    result.update(self.first(term.split(" ")[0], term))
                    if 'epsilon' in self.first(term.split(" ")[0], term):
                        result.update(self.first(self.first_if_epsilon(from_term, symbol), term))
        return result

    def first_if_epsilon(self, term, symbol):
        for i in range(len(term.split(" ")) - 1):
            if term.split(" ")[i] == symbol:
                return term.split(" ")[i + 1]
        return None

    def follow(self, nonterminal):
        result = set()

        if nonterminal == self.grammar.start_symbol:
            result.add('$')

        for nont, term in self.grammar.productions:
            if nonterminal in term.split(" "):
                next = self.first_if_epsilon(term, nonterminal)
                if next != 'epsilon':
                    if next in self.grammar.terminals:
                        result.update(next)
                    elif next in self.grammar.nonterminals:
                        first_of_follow = self.first(next, term)
                        for firsts in first_of_follow:
                            if firsts != 'epsilon':
                                result.update(firsts)
                            else:
                                result.update(self.follow_sets[nont])

                    elif next is None:
                        result.update(self.follow_sets[nont])

        self.follow_sets[nonterminal].update(result)
        return result

    def parse_sequence(self, sequence):
        rules_used = ""
        input_stack = sequence
        working_stack = "S $"
        while input_stack != working_stack != "$":
            first_symbol = input_stack.split(" ")[0]
            first_working_symbol = working_stack.split(" ")[0]
            if first_working_symbol in self.grammar.nonterminals:
                working_stack = working_stack.split(" ", 1)[1]
                rule, number = self.parse_table[(first_working_symbol, first_symbol)]
                rules_used += str(number)
                working_stack = rule + " " + working_stack
                print(self.parse_table[(first_working_symbol, first_symbol)])
            else:
                if first_working_symbol == first_symbol:
                    working_stack = working_stack.split(" ", 1)[1]
                    input_stack = input_stack.split(" ", 1)[1]
                else:
                    working_stack = working_stack.split(" ", 1)[1]
        print(rules_used)


