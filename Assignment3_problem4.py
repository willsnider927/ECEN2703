
#Both are guilty, unique solution
from z3 import *

s=Solver()
a, b, c, d, e, f, g, h, v, w = [Bool(name) for name in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'v', 'w']]

def block_model(s):
   k = s.model()
   return Or([p != k[p] for p in [v, w]])

def print_model(s):
   k = s.model()
   print(', ' .join([str(x) + ' = ' +str(k[x]) for x in [a, b, c, d, e, f, g, h, v , w]]))

def solve_and_print(s):
   result = s.check()
   if result == sat:
     print_model(s)
     if s.check(block_model(s)) == unsat:
        print('solution unique')
     else:
        print('solution not unique')
   elif result == unsat:
     print('unsatisfiable constraints')
   else:
     print('unable to solve')

#A says, “I am a knight.”
s.add(a == a)
#C says, “A is a knave.”
s.add(c == Not(a))
#D says, “B is a knave.”
s.add(d == Not(b))
#E says, “C and D are both knights.”
s.add(e == And(c,d))
#F says, “A and B are not both knaves.”
s.add(f == Not(And(Not(a),Not(b))))
#G says, “E and F are either both knights or both knaves.”
s.add(g == Or(And(e,f),And(Not(e),Not(f))))
#H says, “G and I are either both knights or both knaves, and V and W are not both guilty.”
s.add(h == And(Or(And(g,h),And(Not(g),Not(h))), Not(And(v,w))))
solve_and_print(s)