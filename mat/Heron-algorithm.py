import math
from random import random
import numpy as np
x = np.random.randint(1,1000)
y = int(math.sqrt(x))
print(x)
print(y)

g=int(np.random.randint(1,1000))
def heron():
    a = (((g*g)/g)+g)*1/2
    return a    
if (g * g) == x:
    print("Oldu bu iş!")
else:
    print(heron())
    
    
    