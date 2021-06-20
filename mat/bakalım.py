from tkinter import *
from ttkthemes import ThemedTk
master = Tk()
master.title("Böler")

Label(master, text="Bölünen:").grid(row=0)
Label(master, text="Bölen:").grid(row=1)
Label(master, text="Bölüm:").grid(row=2)
Label(master, text="Kalan:").grid(row=3)

e1 = Entry(master)
e1.grid(row=0, column=1)
e2 = Entry(master)
e2.grid(row=1, column=1)
K = Entry(master, state=DISABLED)
K.grid(row=2, column=1)
Cn = Entry(master, state=DISABLED)
Cn.grid(row=3, column=1)
"""
def bol(K,Cn):
    C0 = float(e1.get())
    p = float(e2.get())
    kalan=float(bolunen%bolen)
    bolum=float(bolunen/bolen)
    sonuc = print("Bölünen: " , float(bolunen), "\nBölen:    " , float(bolen),"\nBölüm:    ", float(bolum),  "\nKalan:    ", float(kalan))
"""

def calc(K, Cn):
    # get the user input as floats
    C0 = float(e1.get())
    p = float(e2.get())
    # < put your input validation here >

    #Amount of interest for repayment:
    K.configure(state=NORMAL) # make the field editable
    K.delete(0, 'end') # remove old content
    K.insert(0, float(C0/p)) # write new content
    K.configure(state=DISABLED) # make the field read only

    #Final Debt Amount:
    Cn.configure(state=NORMAL) # make the field editable
    Cn.delete(0, 'end') # remove old content
    Cn.insert(0, float(C0%p)) # write new content
    Cn.configure(state=DISABLED) # make the field read only


Button(master, text='Çık', command=master.quit).grid(row=5, column=0, sticky=E, pady=4)
Button(master, text='Hesapla', command=lambda: calc(K, Cn)).grid(row=5, column=1, sticky=W, pady=4)

mainloop()
