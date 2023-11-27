from lab5.grammar import Grammar
from lab5.parser import LL1Parser

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



parser = LL1Parser(grammar)
parser.build_parse_table()

input_str = "your_input_string"
output_steps = parser.parse(input_str)

for step in output_steps:
    print(step)