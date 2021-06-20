import sys
from tkinter import *
import sounddevice
from scipy.io.wavfile import write
#%%
def mhello():
    pass
    return

mGui = Tk()
ment = StringVar()

mGui.geometry('450x45+500+300')
mGui.title('Olur mu olur?')

mlabel = Label(mGui,text='Kayıt').pack()

mbutton = Button(mGui, text='Onay',command = mhello,fg ='red', bg='blue').pack()
    
mEntry = Entry().pack()
#%%


print("klj")
