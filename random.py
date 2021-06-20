# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 07:33:49 2020

@author: golge
"""
import random
n = random.random()
print(n)
a = ("şöyle pollkjdsf","sdışhf","asdf")
print(a)
randomlist = []
for i in range(0,5):
    n = random.randint(1,30)
    randomlist.append(n)
print(randomlist)
print(random.choices(a,k=2))