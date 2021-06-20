import time
import sys
import datetime
import locale
import pyglet
import os
locale.setlocale(locale.LC_ALL, '')
negle="İlgilenmiyorum"
fak=["f","F","siktir","Siktir","ff","FF"]
kapa="Pekala, zaman ayırdığınız için teşekkür ederim. Sizlere iyi günler dilerim."
s = time.strftime("%d %b %Y %H:%M:%S ,%A")
print(s)
print("Kolay gelsin...")

iyi_günler = pyglet.media.load(r"C:\Users\golge\Desktop\BaşlamasaQ\Memo\ses\iyi_günler.mp3")
iyi_günler.play()
pyglet.app.run()
#time.sleep(4)
sizi = pyglet.media.load(r"C:\Users\golge\Desktop\BaşlamasaQ\Memo\ses\sizi_digitürkten_arıyorum.mp3")
sizi.play()
pyglet.app.run()
#sys.exit()