from lab5.grammar import Grammar
from lab5.parser import LL1Parser

grammar = Grammar()
grammar.read_grammar("../resources/lftc/g2.txt")

grammar.print_nonterminals()
grammar.print_terminals()
grammar.print_productions()
grammar.print_productions_for_nonterminal("S")

if grammar.is_cfg():
    print("Context-free grammar.")
else:
    print("Not a context-free grammar.")



parser = LL1Parser(grammar)
print(parser.parse_table)

input_seq = "a * ( a + a ) $"
parser.parse_sequence(input_seq)
