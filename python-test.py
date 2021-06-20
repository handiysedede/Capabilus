"""
Aşşağıda ki looplar, whilelar belki bir gün bir bilgisayarı gerçekten 
yormak istersem diye konmuştur. Kendileri birer testtir.
Her biri ayrı bir amaç doğrultusunda işe yaramaktadır.
"""
#%% simple assignment	

for i in range(1000000):
    a = 1
a = 0
#%% augmented assignment	

for i in range(1000000):
    a += 1
t = []
i = 0
#%% augmented assignment and list append	

while i < 100000:
    t.append(i)
    i += 1
#%% simple assignment to float	

for i in range(1000000):
    a = 1.0
n = 60
#%% big integers	

for i in range(10000):
    2 ** n
#%% build dictionary	

for i in range(1000000):
    a = {0: 0}
d = {}
#%% build dictionary 2	

for i in range(100000):
    d[i] = i
a = {0: 0}
#%% set dictionary item	

for i in range(1000000):
    a[0] = i
#%% build set	

for i in range(1000000):
    a = {0, 2.7, "x"}
#%% build list	

for i in range(1000000):
    a = [1, 2, 3]
#%% set list item	

a = [0]
for i in range(1000000):
    a[0] = i
#%% list slice	

a = [1, 2, 3]
for i in range(100000):
    a[:]
#%% integer addition	

a, b, c = 1, 2, 3
for i in range(1000000):
    a + b + c
#%% string addition	

a, b, c = 'a', 'b', 'c'
for i in range(1000000):
    a + b + c
#%% cast int to string	

for i in range(100000):
    str(i)
#%% create function without arguments	

for i in range(1000000):
    def f():
        pass
#%% create function, single positional argument	

for i in range(1000000):
    def f(x):
        pass
#%% create function, complex arguments	

for i in range(1000000):
    def f(x, y=1, *args, **kw):
        pass

#%% function call	

def f(x):
    return x
for i in range(1000000):
    f(i)
#%%function call, complex arguments	

def f(x, y=0, *args, **kw):
    return x
for i in range(100000):
    f(i, 5, 6, a=8)
#%% create simple class	

for i in range(10000):
    class A:
        pass
#%% create class with init	

for i in range(10000):
    class A:
        def __init__(self, x):
            self.x = x
#%% create instance of simple class	

class A:
    pass
for i in range(1000000):
    A()

#%% create instance of class with init	
class A:
    def __init__(self, x):
        self.x = x
for i in range(100000):
    A(i)

#%% call instance method	
class A:
    def __init__(self, x):
        self.x = x

    def f(self):
        return self.x
a = A(1)
for i in range(100000):
    a.f()