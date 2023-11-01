import os
import re

from lab3.scanner import Scanner

current_dir = os.path.dirname(__file__)

program_file = os.path.join(current_dir, "../resources/lftc/p3.spl")
token_file = os.path.join(current_dir, "../resources/lftc/token.in")

regex = r'[.]+'
match = re.match(regex, "1234miau")

with open(program_file, "r") as f:
    program = f.read()

with open(token_file, "r") as f:
    tokens = f.read().split()

scanner = Scanner(program, tokens)
scanner.scan()
print(scanner.pif)
print(scanner.symbol_table)
