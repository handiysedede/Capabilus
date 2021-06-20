
#Bunlar işlem yapıyor ama göstermiyor
sehir= "ankara"
sonuc =sehir.upper()
#Bu ise hesabı yapıp sonucu veriyor
print(sehir.endswith("a"))
#%%""
def dikUcgenAlanıHesapla(a,b):
    return a*b/2

alan =dikUcgenAlanıHesapla(2,3)
print(alan)
#%% Pythonunun lambda büyüsü!!! 
dikUcgenAlanıHesapla2 = lambda a,b : a*b/2
print(dikUcgenAlanıHesapla2(3,6))
type(dikUcgenAlanıHesapla2)
x = dikUcgenAlanıHesapla2
print(x(4,5))
#%% Faktoriyel Hesap
sayi =int(input("Sayı: "))
fak=1
if sayi<0:
    print("olmaz öyle")
elif sayi == 0:
    print("Cevap = 1 ")
else:
    for i in range(1,sayi+1):
        fak = fak*1
    print("Sonuç: ", fak)
#%%Matris toplama DENEME
'''BURASI OLMADI HACIT
x=(" 1"," 3"," 5\n","2"," 4"," 1\n","1"," 5"," 7\n")
y=( "3"," 3"," 4\n","2"," 4"," 1\n","3"," 5"," 4\n")
def matrisTopla(x,y):
    z=x[0]+y[0]+x[1]+y[1]+x[2]+y[2]
    return int(z)
matrisTopla()'''
#%%MATRİS TOPLAMA CEVAP

x= [[1,3,5],[2,4,1],[1,5,7]]
y= [[3,3,4],[2,4,1],[3,5,4]]
matrisSonuc= [[0,0,0],[0,0,0],[0,0,0]]
sonuc[0][0]=x[0][0]+y[0][0]
sonuc[][]=x[][]+y[][]















