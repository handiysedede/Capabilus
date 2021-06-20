# -*- coding: utf-8 -*-
class User:
    def __init__(self,first,last):
        self.first= first
        self.last=last
    def full_name(self):
        return '{} {}'.format(self.first, self.last)


emp_1= User(str(input("İsminiz")),str(input("Soyisminiz"))
print(User.full_name(emp_1))
#%%Bu da Olur