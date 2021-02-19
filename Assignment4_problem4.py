#Results @ N == 17: 17, 8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9, 16
from z3 import *
import math
#read optional command line argument
import sys

if len(sys.argv) > 2:
    raise SystemExit("There should be at most one argument")
elif len(sys.argv) == 2:
    try:
        N = int(sys.argv[1])
    except:
        raise SystemExit("N should be an integer")
    if N < 0:
        raise SystemExit("N should be non-negative")
else:
    N = 15 #default value

s=Solver()
x = [Int('x_%s' % (i))
     for i in range(1,N+1)]
S = [i for i in range(2*N) if (math.sqrt(i) == math.floor(math.sqrt(i)))]

for i in range (N):
    for j in range(N):
        if (i != j):
            s.add(Distinct(x[i], x[j]))
    s.add(And(x[i] >= 1, x[i] <= N))
for i in range (N-1):
    s.add(Or([x[i] + x[i+1] == S[j] for j in range(len(S))]))

def print_model(s):
   print(', '.join([str(s[x[i]]) for i in range(len(x))]))

def solve_and_print(s):
   result = s.check()
   if result == sat:
     print_model(s.model())
   elif result == unsat:
     print('unsatisfiable constraints')
   else:
     print('unable to solve')

solve_and_print(s)