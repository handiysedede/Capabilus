#%% Sadece burayı çalıştırmak için
for x in range(2,10,2):
    print(x)

#%% İnput
sayı = int(input("kaç yıldız ?"))
yildiz="-"
for x in range(1,sayı+1):
    yildiz= yildiz+"*"
    print(yildiz)
    
#%% ASAL SAYI BULMA
'''Sadece kendisine-ve 1'e- bölünen sayı'''
sayi=int(input("Sayı lütfen "))
i=0
asalMi=True
for x in range(2,sayi):
    if (sayi%x) ==0:
        asalMi=False
        break
#Buranın defaultu True
#if asalMi:  ('de olurdu)
if asalMi==True:
    print("ASAL")
else:
    print("ASAL DEĞİL")
