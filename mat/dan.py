# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 12:11:42 2020

@author: golge
"""

from tkinter import ttk
from ttkthemes import ThemedTk

app = ThemedTk(theme="radiance")

            


ttk.Label(app, text="Bölünen:").grid(row=0)
ttk.Label(app, text="Bölen:").grid(row=1)
ttk.Label(app, text="Bölüm:").grid(row=2)
ttk.Label(app, text="Kalan:").grid(row=3)
e1 = Entry(app)
e1.grid(row=0, column=1)

ttk.Button(app,text="Check").grid(row=0,column=2)
ttk.Label(app,text = "Adınız:").grid(row=0,column=1,ipady=5,ipadx=5)











app.mainloop()
