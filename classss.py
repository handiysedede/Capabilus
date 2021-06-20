# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:24:16 2020

@author: golge
"""
import datetime
class User:
        """Kullanıcı bilgileri almaya yarayan class bir işlem
        Bilgiler elbette daha sonra insanlığın sonunu getirmek 
        için kullanılacaktır"""
    def __init__(self,full_name,birthday):
        self.name = full_name
        self.birthday = birthday #ggaayyyy
        # İsmi; İsim, Soyisim olarak ayırıyoruz
        name_pieces = full_name_split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    def age(self):
        '''Returns the age of the user in years.
        ------'''
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) #Date of birth
        age_in_days =  (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)
    
user = User("Dave Bowman", "135165165")
print(user.age())