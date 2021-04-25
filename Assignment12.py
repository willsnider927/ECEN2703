from sympy import isprime
from mpmath import mp

decimalPlaces = 100
with mp.workdps(decimalPlaces):
    estring = str(mp.e).replace('.','')

for i in range(89): #find first 12 digit prime in e
    value = int(estring[i:i+12])
    if isprime(value):
        print(value, "is prime.")
        break