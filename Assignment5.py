from z3 import *


s=Solver()

x=Int('X')
y=Int('Y')
z=Int('Z')

sentence = ForAll([x], Exists([y], And(x<y, ForAll([z], Or(x >= z, z >= y)))))

def print_model(m):
    print ("x = %s" % str(m[x]))
    print ("y = %s" % str(m[y]))
    print ("z = %s" % str(m[z]))

def checkValidity(sentence):
   s=Solver()
   s.add(Not(sentence))
   result = s.check()
   if result == sat:
    print('Not valid. Model for the negation:')
    m=s.model
    print_model(m)
   elif result == unsat:
    print('Valid')
   else:
    print('unable to solve')
    
checkValidity(sentence)