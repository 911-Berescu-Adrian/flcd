from lab5.grammar import Grammar

grammar = Grammar()
grammar.read_grammar("../resources/lftc/g1.txt")

grammar.print_nonterminals()
grammar.print_terminals()
grammar.print_productions()
grammar.print_productions_for_nonterminal("S")

if grammar.is_cfg():
    print("It's a context-free grammar.")
else:
    print("It's not a context-free grammar.")