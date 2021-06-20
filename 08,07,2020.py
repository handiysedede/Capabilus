#Ýlk harf halihazorda bulunan harf, Ýkincisi ise
#yerine gelmesini istediðimiz
selam="merhaba dünya"
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
#Bu method da gördüðü her boþluðu yeni variable
#haline getirir. Paranteze ne yazarsan
#ona göre ayýrýr
data="benim adým utku yaþým 34"
print(data.split())
#"böyle þeyler de yapýyoruz bak(Engin Demiröð);
print("Ýsmi " + data.split()[2] + " imiþ")
#Geçici deðiþken temp(deðer tip)
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
#Mil'i KM'ye çevir
oran=0.621371192
km= int(input("Kaç km? "))
mil = km*oran
print(str(km)+" km "+str(mil)+" mil eder")
'''
#(abim geldi)Lisstelere geçtik
my_list=[["a","b"],["datu"]]
print(my_list)

#Ünlü öðrenci kafasý
student=["Engin","Utku","Zeynep"]
print(student)
student.append("Ahmet")
print(student)
student[3]="Veli"
print(student[3])
print(student)
student.remove("Veli")
#list constructor
sehirler=list(("Ankara","Ýstanbul))"))
print(sehirler)
dayýlar=["Cengiz","Gafur","Genco"]
#diziler referans tiptir
sehirler=("Ankara"+"Ýstanbul")
print(str("Ankaralýlarýn sayýsý " + str(sehirler.count("Ankara"))))
#yerini söyler AMA ilk bulduðu yerde bitiriyor
print(str("Ankaralý indexi " + str(sehirler.index("Ankara"))))

#Bi deniycem
say=["jd","jje"]
print(say)
say.insert(6,3)
#buralar karýþýk
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
'''#"g" gelmeden önceki halini kopyalamýþtým
print(say3)
#eklemekmiþ yani bu
say.extend(say3)
print(say)'''
#Alfabetik kas
gat=["abo","cabo","zay"]
gat.sort()
print(gat)
gat.reverse()
print(gat)

#TUPLE SADECE PYTHON'A ÖZGÜDÜR!!!!!
#Listede tuplle, tuple da liste tanýmlanabilir ki ne var bunda
tap=(2,4,6,"Ankara",(2,3,4),["sayý"])
lis=[2,4,6,"Ankara",[3,4,5],("dayý")]
#tek eleman sýkýntýlý
tek=("bu")
print(type(tek))
#VÝRGÜL KOY
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
    print("Olcan sen kýz")

#Bunlara çok karýþamýyosun ama ekleme, günceleme, 'o var'
studentSet.add("Cengiz")
#update()'de tek olunca da sýkýntý
#studentSet.update("kuþ")
studentSet.update(tek)
print(len(studentSet))
print(studentSet)
studentSet.remove("bu")
print(studentSet)
#bulamazsa hata vermeden çýkar
studentSet.discard("dayým")

#Set durur ama hala
studentSet.clear()
#Komple kurtulmak
del studentSet






