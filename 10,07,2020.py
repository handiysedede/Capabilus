#%%İki set'i birleştirip, ortaklarıyla bir tutmak
a ={1,2,3,4,5,6,7}
b={6,7,8,9}
print(a | b)
print(a)
print(b)
#%%Ya da ...
print(a.union(b))
print(a)
print(b)
#Intersection (kesişim) 
#%%ortak olan elemanları gösterir
print(a & b)
print(a.intersection(b))
#%% a'nın b 'den farkını
print(b - a)
print(a.difference(b))
#Shift+3 space == ^
#%%Simetrik fark
print(a ^ b)
print(b.symmetric_difference(a))

#%%Dictionnaries( sözlük)
sözlük={
        "book":"kipat","table":"masa"
        }
print(sözlük["book"])
sözlük["book"]="kitap"
#%%Yukarıyı yanlış yazarsan yeni eleman ekler
frSozluk=dict(livre="kitap", attitude="tutum")
print(frSozluk)
#bir değeri silmek
#%%listelerde .remove idi ama
del(sözlük["book"])
print(sözlük)
#%%del sözlük
print(sözlük)

#%%Trafik ışıklarıyla kara kalıplarını öğren
'''lights=["red","yellow","green"]
currentLight=lights[1]
print(currentLight)
if currentLight=="red":
    print("stop")
if currentLight=="yellow":
    print("get ready")
if currentLight=="green":
    print("go")'''
#Böyle daha iyi ama
lights=["red","yellow","green"]
currentLight=lights[0]
if currentLight=="red":
    print("stop")
elif currentLight=="yellow":
    print("get ready")
    #buraya dikkat, başka şansı yok zaten
else:
    print("go")

#ÖDEV
'''
say=int(input("sayı"))

if say==0:
    print("e sıfır bu")
elif say<0:
    print("Eksili la bu")
else:
    print("Bu olur işte")
    
    #ÖDEV 2
buy1=int(input("sayıları yaz bakalım..."))
buy2=int(input("ver daha"))
buy3=int(input("ve son"))    
uf=0
if (buy1>=buy2) and (buy1>=buy3):
    uf=buy1
    print(uf)
elif (buy2>=buy1) and (buy2>=buy3):
    uf=buy2
    print(uf)
else:
    uf=buy3
    print("En büyük sayı" , uf)
'''
#%%FOR (for'un içiyle if'in içi farklı ?=stop)
sehirler=["Ankara","İstanbul","İzmir"]
for sehir in sehirler:
    if sehir!="Ankara":
        print(sehir + " için kod : " +sehir[:3])
    print("****")
 #%%



#WHİLEE
sayac=1
sonuc=0
while sayac<=10:
    sonuc=sonuc+sayac
    sayac=sayac+1
print(sonuc)








  