import os
from lab3.scanner import Scanner

current_dir = os.path.dirname(__file__)

program_file = os.path.join(current_dir, "../resources/lftc/p3.spl")
token_file = os.path.join(current_dir, "../resources/lftc/token.in")

with open(program_file, "r") as f:
    program = f.read()

with open(token_file, "r") as f:
    tokens = f.read().split()

scanner = Scanner(program, tokens)
scanner.scan()

output_pif_file = os.path.join(current_dir, "../resources/lftc/PIF.out")
output_st_file = os.path.join(current_dir, "../resources/lftc/ST.out")

with open(output_pif_file, "w") as f:
    for item in scanner.pif:
        f.write(str(item)+'\n')

with open(output_st_file, "w") as f:
    f.write(str(scanner.symbol_table))

print(scanner.pif)
print(scanner.symbol_table)
