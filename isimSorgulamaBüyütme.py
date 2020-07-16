# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:07:54 2020

@author: golge
"""


liste=[]
def isimSorgula():
    isim=input(str("İsim giriniz... "))
    isim=isim.title()
    liste.append(isim)
    print("İsminiz \'"+isim+"\' olarak kaydedildi")
isimSorgula()
print("Kayıtlı isimler: ")
print(liste)