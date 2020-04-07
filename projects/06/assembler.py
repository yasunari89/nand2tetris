from parser import Parser as P
from code import Code as C
from symbol_table import SymbolTable as S
import sys


def isint(string):
    try:
        int(string)
        return True
    except ValueError:
        return False



asm_file = sys.argv[1]
hack_file = asm_file.replace('.asm', '.hack')
s = S()
c = C()
p1 = P(asm_file)
op_address = 0

while True:

    if p1.command_type() == 'L_COMMAND':
        s.add_entry(p1.symbol(), op_address)
    else:
        op_address += 1
    
    if p1.has_more_commands():
        p1.advance()
    else:
        break


p2 = P(asm_file)

with open(hack_file, 'w') as f:
    while True:

        if p2.command_type() == 'A_COMMAND':
            if p2.symbol() in s.symbol_table:
                binary = '0' + bin(s.get_address(p2.symbol()))[2:].zfill(15)
            elif isint(p2.symbol()):
                binary = '0' + bin(int(p2.symbol()))[2:].zfill(15)
            else:
                s.add_variable(p2.symbol())
                binary = '0' + bin(s.get_address(p2.symbol()))[2:].zfill(15)
            f.write('{}\n'.format(binary))
            print(binary)

        elif p2.command_type() == 'C_COMMAND':
            dest = p2.dest()
            jump = p2.jump()
            comp = p2.comp()
            bin_dest = c.dest(dest)
            bin_jump = c.jump(jump)
            bin_comp = c.comp(comp)
            binary = '111' + bin_comp + bin_dest + bin_jump
            f.write('{}\n'.format(binary))
            print(binary)

        if p2.has_more_commands():
            p2.advance()
        else:
            break