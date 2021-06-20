#%%
import time
secs = int(input("Saniyeyi yazınız  "))
for i in range(secs):
    print((secs-1)-i , "saniye geçti")
    time.sleep(1)
#%%
import threading
def a():
    for i in range(1,1000):
        print("AaAaAa", end=" ")
def b():
    for i in range(1,1000):
        print("bBbBbB", end=" ")
t1 = threading.Thread(target=a)
t2 = threading.Thread(target=b)
t1.start()
t2.start()
#%%
a = 19
b = 0
try:
    a/b
except ArithmeticError:
    print("Olmadı")
finally:
    print("Oldu herhal")
#%%
x = -1
if x<0:
    raise Exception("bişi")
#%%
l = [35,312,352,1533,31,3,21,615]
nl = list(map(lambda x:"çift" if x%2==0 else "tek", l ))
print(nl)