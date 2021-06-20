#%% İnheritance almayı öğrenelim. Hem propriety de hem de fonction
#%% tanımlı classlarda çalışmaktadır.
class Person:
     def __init__(self,firstName,lastName,age):
         self.firstName = firstName
         self.lastName = lastName
         self.age = age
         

person1 = Person("Engin","Demiroğ",33)
print(person1.firstName)
    
    
class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
class Customer(Person,Worker):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
#%% Daha yazarken noktaya basar basmaz çıkıyor zati
ahmet=Worker()
ahmet
mehmet=Customer()
mehmet.

#%% Workshop 
'''
if print(input("Operasyon: \n 1: Topla, 2 : Çıkar, 3 : Çarp, 4 : Böl"))


def topla(sayi1,sayi2):
    sayi1=input(int(print("Ne ile ? \n")))
    sayi2=input(int(print("Neyi ? \n")))    
    print("Sonuç = " + int(sayi1+sayi2))
#print(topla())
topla()
'''

def topla(sayi1,sayi2):
    return sayi1 + sayi2

def cikar(sayi1,sayi2):
    return sayi1 - sayi2

def carp(sayi1,sayi2):
    return sayi1 * sayi2

def bol(sayi1,sayi2):
    return sayi1 / sayi2

print("Operasyon:")
print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")
#İlk eylem burada
secenek = input("Operasyon seçiminiz?")

sayi1 = int(input("Birinci sayı?"))
sayi2 = int(input("İkinci sayı?"))
#Asıl olay da burada
if secenek == '1':
    print("Toplam : " +str(topla(sayi1,sayi2)))
elif secenek == '2':
    print("Çıkarma : " +str(cikar(sayi1,sayi2)))   
elif secenek == '3':
    print("Çarpma : " +str(carp(sayi1,sayi2))) 
elif secenek == '4':
    print("Bölme : " +str(bol(sayi1,sayi2)))
else:
    print("Geçersiz seçenek")

# Olmadı, yapamadım...
import json

data = '{"firstName":"engin","lastName":"demiroğ"}'

y = json.loads(data)

customer = {
        "firstName":"engin",
        "email":"engindemirog@gmail.com"
        }

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Engin"))







