from parser import Parser as P
from code import Code as C

p = P('add/Add.asm')
c = C()
p.advance()
dest = p.dest()
comp = p.comp()
print(c.dest(dest))
print(c.comp(comp))