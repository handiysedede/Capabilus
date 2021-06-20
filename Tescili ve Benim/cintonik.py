'''
import time
cin=100
tonik=10
cinTonik=cin+tonik
gün = " gün"


print("İlk"+ gün)
cüzdan+=10
time.sleep(2)
print("İkinci"+ gün)
cüzdan+=10
time.sleep(2)
print("İlk"+ gün)
cüzdan+=10
time.sleep(2)
print("İlk"+ gün)
cüzdan+=10
time.sleep(2)
print("İlk"+ gün)
cüzdan+=10
time.sleep(2)
print("İlk"+ gün)
cüzdan+=10
time.sleep(2)print("İlk"+ gün)
cüzdan+=10
time.sleep(2)
'''

''''
cuzdan=0
def içmece():             #Neden olmadı bu bu arada????     
    for ay in range(30):
        cuzdan=cuzdan + 10
    if cuzdan==110:
        print("Oldu")
return cuzdan
print(içmece())'''

def ic(cinFiyat=float(input(print("Cinin litersi ne kadar hacıt?  "))),
tonikFiyat=float(input(print("Toniğin litersi ne kadar hacıt?  "))),
cinTonikArzusu=float(input(print("Kaç litre cin yeter sana?  "))),
garibanlıkOlcegi=float(input(print("Günlük kazancın ne kadar hacıt?  ")))
):
    cinArzusu= float(cinTonikArzusu/2)
    tonikArzusu = float(cinTonikArzusu/2)
    cinGİder = float(cinArzusu*cinFiyat)
    tonikGider = float(tonikArzusu*tonikFiyat)
    toplamGider = float(cinGİder+tonikGider)
    azim=int(toplamGider/garibanlıkOlcegi)
    return azim
global azim
print("İşin zor, "+azim+" gün çalışşcan vallaka...")




















