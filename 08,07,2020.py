#�lk harf halihazorda bulunan harf, �kincisi ise
#yerine gelmesini istedi�imiz
selam="merhaba d�nya"
print(selam.replace('m','M'))
print(selam)
selam=selam.replace('m','M')
print(selam)
#Ama sadece variable'larda oluyor
'''
data=[3,4,1,2,44,523,"dat"]
print(data.replace[1,"hoba"])
print(data)
'''
#Bu method da g�rd��� her bo�lu�u yeni variable
#haline getirir. Paranteze ne yazarsan
#ona g�re ay�r�r
data="benim ad�m utku ya��m 34"
print(data.split())
#"b�yle �eyler de yap�yoruz bak(Engin Demir��);
print("�smi " + data.split()[2] + " imi�")
#Ge�ici de�i�ken temp(de�er tip)
x=10
y=20
print(str(x))
print(str(y))
''' Olmuyor
y==x
print(str(y)) '''
temp=x
x=y
y=temp
print(str(x))
print(str(y))
'''
#Mil'i KM'ye �evir
oran=0.621371192
km= int(input("Ka� km? "))
mil = km*oran
print(str(km)+" km "+str(mil)+" mil eder")
'''
#(abim geldi)Lisstelere ge�tik
my_list=[["a","b"],["datu"]]
print(my_list)

#�nl� ��renci kafas�
student=["Engin","Utku","Zeynep"]
print(student)
student.append("Ahmet")
print(student)
student[3]="Veli"
print(student[3])
print(student)
student.remove("Veli")
#list constructor
sehirler=list(("Ankara","�stanbul))"))
print(sehirler)
day�lar=["Cengiz","Gafur","Genco"]
#diziler referans tiptir
sehirler=("Ankara"+"�stanbul")
print(str("Ankaral�lar�n say�s� " + str(sehirler.count("Ankara"))))
#yerini s�yler AMA ilk buldu�u yerde bitiriyor
print(str("Ankaral� indexi " + str(sehirler.index("Ankara"))))

#Bi deniycem
say=["jd","jje"]
print(say)
say.insert(6,3)
#buralar kar���k
say.extend(say)
print(say)
 #devam edelim
say.pop(1)
print(say)
#Diziler referans tiptir, arraylar
say3=say.copy()
say1=say
say1[0]="g"
print(say)
print(say1)
'''#"g" gelmeden �nceki halini kopyalam��t�m
print(say3)
#eklemekmi� yani bu
say.extend(say3)
print(say)'''
#Alfabetik kas
gat=["abo","cabo","zay"]
gat.sort()
print(gat)
gat.reverse()
print(gat)

#TUPLE SADECE PYTHON'A �ZG�D�R!!!!!
#Listede tuplle, tuple da liste tan�mlanabilir ki ne var bunda
tap=(2,4,6,"Ankara",(2,3,4),["say�"])
lis=[2,4,6,"Ankara",[3,4,5],("day�")]
#tek eleman s�k�nt�l�
tek=("bu")
print(type(tek))
#V�RG�L KOY
tek=("bu",)
print(type(tek))

#Dictionnaries
studentSet={"Engin","Utku","Melda"}
studentSetFonksiyonlusu= set("Engin","....")
print(studentSet)
for i in studentSet:
    print(i)
print("Utku" in studentSet)
if "Melda" in studentSet:
    print("Olcan sen k�z")

#Bunlara �ok kar��am�yosun ama ekleme, g�nceleme, 'o var'
studentSet.add("Cengiz")
#update()'de tek olunca da s�k�nt�
#studentSet.update("ku�")
studentSet.update(tek)
print(len(studentSet))
print(studentSet)
studentSet.remove("bu")
print(studentSet)
#bulamazsa hata vermeden ��kar
studentSet.discard("day�m")

#Set durur ama hala
studentSet.clear()
#Komple kurtulmak
del studentSet






