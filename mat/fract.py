from fractions import Fraction
import math
Fraction(16,-10)
a = Fraction(24,10)
print(a.numerator)
print(a.denominator)
print(float(a))
print(a)


r = Fraction(1,2)
rr=float(1/2)
print(r,"  ", rr)
#%%
ı = Fraction(1,2)
p = Fraction(1,3)
o = Fraction(1,4)
soz = [ı,p,o]
print(soz.sort())
print(soz)

"""
if ı>=p and ı>=o:
    soz.append(ı)
elif p>=ı and p>=o:
    soz.append(p)
else o>=ı and o>=p:
    soz.append(o)
"""
#%%
a = Fraction.from_float(1.2)
print(a)
#Returns the greatest int <= self. 
a = Fraction.__ceil__(141134)
print(a)
#Returns the least int >= self. 
a = Fraction.__round__(1214, 10**3)
print(a)
#The first version returns the nearest int to self, rounding half to even. 
#The second version rounds self to the nearest multiple of Fraction(1, 10**ndigits) 
#(logically, if ndigits is negative), again rounding half toward even.
#%%
a = Fraction('1.2')
print(a)
a = Fraction(2,-3)
print(-a)
#%%
a = Fraction(5,4)
print(1/a)
#%%
a = Fraction(34,21)
b = Fraction(21,13)
print(a+b)
a = Fraction(32,7)
b = Fraction(7,2)
print(a%b)
a = Fraction(3,2)
print(a**12)
print(a)
print(a**(-1))
a = Fraction(9,4)
print(a**0.5)
#%%
def Farey(a,b):
    n = a.numerator+b.numerator
    d = a.denominator+b.denominator
    return Fraction(n,d)


a = Fraction(3,4)
b = Fraction(1,13)
print(Farey(a,b))
#%%
def farey_sequence(n: int, descending: bool = False) -> None:
    """Print the n'th Farey sequence. Allow for either ascending or descending."""
    (a, b, c, d) = (0, 1, 1, n)
    if descending:
        (a, c) = (1, n - 1)
    print("{0}/{1}".format(a, b))
    while (c <= n and not descending) or (a > 0 and descending):
        k = (n + b) // d
        (a, b, c, d) = (c, d, k * c - a, k * d - b)
        print("{0}/{1}".format(a, b))
farey_sequence(279)
#%%
def egypt(f):
    e = int(f)
    f -= e
    parts = [e]
    while(f.numerator>1):
        e = Fraction(1, int(ceil(1/f)))
        parts.append(e)
        f -= e
    parts.append(f)
    return parts
a = Fraction(21,13)
print(egypt(a))            # [1, Fraction(1, 2), Fraction(1, 9), Fraction(1, 234)]
print(sum(egypt(a))        # 21/13 (confirming that these fractions add up to the original value)
      
#%%
#!/usr/bin/python
from fractions import Fraction
import numpy as np





fractions_list=[Fraction(4,14),Fraction(8,14),Fraction(3,7),Fraction(21,14)]




lcm = np.lcm.reduce([fr.denominator for fr in fractions_list])

vals = [int(fr.numerator * lcm / fr.denominator) for fr in fractions_list]
vals.append(lcm)
print(np.gcd.reduce([2, 4, 2, 10]))
print(np.lcm.reduce([2, 4, 2, 10]))

#%%
print(np.lcm(-784,-671))
#%%
a = Fraction(2,10)
print(a)
#%%
#!/usr/bin/python
from SortFraction import ArrangeFraction

##
 # Sorting fractions
 ##
numerators = [1, 3, 5, 9]
denominators = [2, 4, 2, 10]
fractions = {'numerators':numerators, 'denominators':denominators}

print("\n    Sorting in ascending order the fractions:\n")
# Print as fraction
for numerator in fractions['numerators']: print('{:12d}'.format(numerator), end='')
print('{}{:>11}'.format('\n', ' '), end='')
for wasted in range(len(numerators)-1): print('{}'.format('-   ,       '), end='')
print('{:>1}'.format('-'))
for denominator in fractions['denominators']: print('{:12d}'.format(denominator), end='') 
print('\n\n')

# use the SortFraction class
sort_fract = ArrangeFraction(fractions)
fractions = sort_fract.sortAscending()

# Print as fraction
for numerator in fractions['numerators']: print('{:13d}'.format(numerator), end='')
print('{}{:>1}'.format('\nAnswer  =  ', ' '), end='')
for wasted in range(len(numerators)-1): print('{}'.format('-   ,        '), end='')
print('{:>1}'.format('-'))
for denominator in fractions['denominators']: print('{:13d}'.format(denominator), end='') 
print('\n\n')


print('\n\n')