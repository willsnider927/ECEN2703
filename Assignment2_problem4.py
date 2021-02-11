#solution not unique, found a = F, m = T
from z3 import *

s = Solver()
a = Bool('a') #alex is truthful
m = Bool('m') #mom is truthful

def block_model(s):
   k = s.model()
   return a != k[a]

def print_model(s):
   k = s.model()
   print(', ' .join([str(x) + ' = ' +str(k[x]) for x in [a, m]]))

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

#a said that m said that they are different types
s.add(Implies(a, m == Xor(a,m)))
solve_and_print(s)

