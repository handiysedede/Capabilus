a = {'id' : 5, 'username':'PythonUser'}
b = {'id': 5 , 'username': 'Dayınlarlı'}

print({**b,**a})
print(a,b)
""" 3.9'da böyle oldu
print(a|b)
ya da 
a |= b
"""
b.update(a)
print(a)

#%%
from datetime import datetime
from pytz import timezone

current_time = datetime.now()
print(current_time)
current_time_amsterdam = datetime.now()
print(current_time.astimezone(timezone('Europe/Amsterdam')))
#%%3.9'da böyle
#from zoneinfo import ZoneInfo
#%% ???
from typing import List

my_list: List[int] = [1,2,3,4]
print(my_list)

my_list:'1234'
print(my_list)
#%% 
doctors = ['Dr. Cenk Demir','Dr. Faruk ECZANESİ']
names = []
#
for doctor in doctors:
    if doctor.startswith('Dr. '):
        names.append(doctor[4:])
    else:
        names.append(doctor)
    names.append(doctor.removeprefix('Dr. '))
""" Yerine;
names = [] 
names= [doctor.removeprefix('Dr. ')for doctor in doctors]
"""
print(names)
