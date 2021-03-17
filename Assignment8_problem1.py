from z3 import *

def set_cover(C):
	opt = Optimize()
	xSet = set()
	for i in C:
		xSet = xSet | i
	x = [Bool('x_%s' % i) 
	  for i in range(len(xSet))]
	for i in C:
		opt.add(Or([x[v] for v in i]))
	opt.minimize(Sum([If(v, 1, 0) for v in x]))
	opt.check()
	result = opt.model()
	return([x[v] for v in range(len(x)) if opt.model()[x[v]]])

Ca = [{0,10}, {0,1,4}, {1,2,4,5,6,7}, {0,1,3,5,9}, 
	  {0,3}, {2,6,8,11}, {2,7,8,10}, {3,9}] 
print(set_cover(Ca))